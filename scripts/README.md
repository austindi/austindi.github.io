# Prefect Stats Script

Fetches task run statistics from Prefect and writes them to `public/prefect-stats.json` for display on the portfolio page.

## Setup

1. Install dependencies:
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. Configure Prefect (uses your existing profile from `prefect.yaml` or `~/.prefect/prefect.yaml`):
   - Ensure your profile has `PREFECT_API_URL` and auth (`PREFECT_API_KEY` or `PREFECT_API_AUTH_STRING`)
   - Run `prefect profile use <your-profile>` if needed

## Run

```bash
python scripts/fetch_prefect_stats.py
```

This writes `public/prefect-stats.json` with success rate, runs monitored, and automated recovery status.

## Schedule (optional)

Add a cron job or GitHub Action to run the script periodically (e.g., daily):

```yaml
# .github/workflows/update-prefect-stats.yml
name: Update Prefect Stats
on:
  schedule:
    - cron: "0 */6 * * *"  # Every 6 hours
  workflow_dispatch:
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r scripts/requirements.txt
      - run: python scripts/fetch_prefect_stats.py
        env:
          # For CI, set these as repo secrets if not using a config file:
          PREFECT_API_URL: ${{ secrets.PREFECT_API_URL }}
          PREFECT_API_KEY: ${{ secrets.PREFECT_API_KEY }}
      - uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update prefect stats"
          file_pattern: public/prefect-stats.json
```
