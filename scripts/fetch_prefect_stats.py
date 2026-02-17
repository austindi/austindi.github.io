#!/usr/bin/env python3
"""
Fetch Prefect task/flow run statistics and write to JSON for the portfolio page.

Uses the Prefect Python SDK. Reads config from your Prefect profile (prefect.yaml, etc.).

Output: public/prefect-stats.json
Schema: updated_at, reliability (success_rate, p95_runtime_minutes), operations (runs_monitored, active_flows).
All values are fetched from the Prefect API.
"""

from __future__ import annotations

import asyncio
import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from typing import Optional

try:
    from prefect.client.orchestration import get_client
    from prefect.client.schemas.filters import (
        FlowRunFilter,
        FlowRunFilterState,
        FlowRunFilterStateType,
        TaskRunFilter,
        TaskRunFilterState,
        TaskRunFilterStateType,
    )
    from prefect.client.schemas.sorting import FlowRunSort
    from prefect.states import StateType
except ImportError as e:
    print("Install prefect: pip install prefect", file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "public" / "prefect-stats.json"

# Max flow runs to fetch for P95 (API often caps at 200)
FLOW_RUNS_LIMIT = 200

# Schema: only API-derived fields
DEFAULT_STATS = {
    "updated_at": "",
    "reliability": {
        "success_rate": 0.0,
        "p95_runtime_minutes": 0,
    },
    "operations": {
        "runs_monitored": 0,
        "active_flows": 0,
    },
}


def load_existing() -> dict:
    """Load prefect-stats.json and return only the current schema (extra keys stripped)."""
    result = deepcopy(DEFAULT_STATS)
    if not OUTPUT_PATH.exists():
        return result
    try:
        data = json.loads(OUTPUT_PATH.read_text())
        for key in DEFAULT_STATS:
            if key not in data:
                continue
            if isinstance(DEFAULT_STATS[key], dict):
                for subkey in DEFAULT_STATS[key]:
                    if subkey in data.get(key, {}):
                        result[key][subkey] = data[key][subkey]
            else:
                result[key] = data[key]
        return result
    except (json.JSONDecodeError, TypeError):
        return result


async def _task_runs_count(client, task_run_filter: Optional[TaskRunFilter]) -> int:
    """Call POST /task_runs/count and return the integer count."""
    body = {
        "flows": None,
        "flow_runs": None,
        "task_runs": (
            task_run_filter.model_dump(mode="json", exclude_unset=True)
            if task_run_filter
            else None
        ),
        "deployments": None,
    }
    response = await client.request("POST", "/task_runs/count", json=body)
    return response.json()


async def get_task_run_counts(client) -> tuple[int, int, int]:
    """Return (total, completed, failed) task run counts."""
    total = await _task_runs_count(client, None)
    completed = await _task_runs_count(
        client,
        TaskRunFilter(
            state=TaskRunFilterState(
                type=TaskRunFilterStateType(any_=[StateType.COMPLETED]),
                name=None,
            ),
        ),
    )
    failed = await _task_runs_count(
        client,
        TaskRunFilter(
            state=TaskRunFilterState(
                type=TaskRunFilterStateType(any_=[StateType.FAILED]),
                name=None,
            ),
        ),
    )
    return total, completed, failed


async def get_flow_run_metrics(client) -> tuple[list[float], int]:
    """
    Fetch recent completed flow runs and return:
    - List of run durations in seconds (for P95)
    - Count of deployments (active flows)
    """
    completed_filter = FlowRunFilter(
        state=FlowRunFilterState(
            type=FlowRunFilterStateType(any_=[StateType.COMPLETED]),
        ),
    )
    flow_runs = await client.read_flow_runs(
        flow_run_filter=completed_filter,
        sort=FlowRunSort.END_TIME_DESC,
        limit=FLOW_RUNS_LIMIT,
    )
    durations_seconds: list[float] = []
    for run in flow_runs:
        if run.total_run_time is not None and run.total_run_time.total_seconds() > 0:
            durations_seconds.append(run.total_run_time.total_seconds())

    deployments = await client.read_deployments(limit=200)
    active_flows = len(deployments) if deployments else 0

    return durations_seconds, active_flows


def p95_minutes(durations_seconds: list[float]) -> int:
    """Return 95th percentile duration in minutes (rounded)."""
    if not durations_seconds:
        return 0
    sorted_sec = sorted(durations_seconds)
    idx = max(0, int(len(sorted_sec) * 0.95) - 1)
    sec = sorted_sec[idx]
    return round(sec / 60.0)


def main() -> None:
    existing = load_existing()

    async def run() -> None:
        async with get_client() as client:
            task_total, task_completed, _ = await get_task_run_counts(client)
            durations_sec, active_flows = await get_flow_run_metrics(client)

        success_rate = (
            round(task_completed / task_total, 3) if task_total else 0.0
        )
        p95_min = p95_minutes(durations_sec)

        now_utc = datetime.now(timezone.utc).replace(microsecond=0)
        now_est = now_utc.astimezone(ZoneInfo("America/New_York"))
        existing["updated_at"] = now_est.isoformat()
        existing["reliability"]["success_rate"] = success_rate
        existing["reliability"]["p95_runtime_minutes"] = p95_min
        existing["operations"]["runs_monitored"] = task_total
        existing["operations"]["active_flows"] = active_flows

    asyncio.run(run())

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(existing, indent=2))

    r = existing["reliability"]
    o = existing["operations"]
    print(f"Wrote {OUTPUT_PATH}")
    print(
        f"  Success rate: {r['success_rate']:.1%}, Runs monitored: {o['runs_monitored']}, "
        f"P95 runtime: {r['p95_runtime_minutes']} min, Active flows: {o['active_flows']}"
    )


if __name__ == "__main__":
    main()
