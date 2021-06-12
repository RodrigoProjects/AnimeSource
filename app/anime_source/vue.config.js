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
      "/googleapis": {
        target: "https://www.googleapis.com",
        //secure: true,
        changeOrigin: true,
        pathRewrite: {
          "^/googleapis": "",
        },
      },
    },
  },
};
