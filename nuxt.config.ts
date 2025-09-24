// nuxt.config.ts
export default defineNuxtConfig({
  app: {
    head: {
      title: "Dave Austin — Software & Data Engineer",
      meta: [
        { name: "viewport", content: "width=device-width, initial-scale=1" },
        {
          name: "description",
          content:
            "Portfolio of software and data engineering projects by Dave Austin.",
        },
      ],
    },
  },
  css: ["@/assets/styles/main.css"],
});
