export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "CarRanker",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Environment variables: https://nuxtjs.org/docs/2.x/configuration-glossary/configuration-env/
  env: {
    webApiHost: process.env.WEB_API_HOST || "localhost",
    webApiPort: process.env.WEB_API_PORT || 3000,
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    "@nuxt/typescript-build",
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/chakra
    "@chakra-ui/nuxt",
    // https://go.nuxtjs.dev/emotion
    "@nuxtjs/emotion",
    // https://go.nuxtjs.dev/pwa
    "@nuxtjs/pwa",
    // https://github.com/nuxt-community/apollo-module
    "@nuxtjs/apollo",
  ],

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: "en",
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  // Watch Configuration: https://nuxtjs.org/docs/2.x/configuration-glossary/configuration-watchers
  watchers: {
    webpack: {
      poll: true,
    },
  },

  // Apollo Configuration: https://github.com/nuxt-community/apollo-module
  apollo: {
    clientConfigs: {
      default: "~/plugins/apollo-config.ts",
    },
  },
};
