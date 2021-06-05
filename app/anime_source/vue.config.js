module.exports = {
  devServer: {
    proxy: {
      "/graphdb": {
        target: "http://localhost:7200",
        secure: true,
        changeOrigin: true,
        pathRewrite: {
          "^/graphdb": "",
        },
      },
      "/serpapi": {
        target: "https://serpapi.com",
        secure: true,
        changeOrigin: true,
        pathRewrite: {
          "^/serpapi": "",
        },
      },
    },
  },
};
