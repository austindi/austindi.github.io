// nuxt.config.ts
export default defineNuxtConfig({
  ssr: false, // Disable server-side rendering for static hosting
  nitro: {
    preset: "github-pages", // Simplifies GitHub Pages deployment
  },
  app: {
    baseURL: "/austindi.github.io/", // Root-level site (since repo name = austindi.github.io)
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
