module.exports = {
  webpackDevMiddleware: config =>{
    config.watchOptions.poll = 300; 
    return config; 
  },
  serverRuntimeConfig: {
    GOOGLE_API_KEY: process.env.GOOGLE_API_KEY,
    API_SERVER_URL: process.env.BACKEND_SERVER_API,
  },
  publicRuntimeConfig: {
    API_URL: process.env.BACKEND_API,
  }
}