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
    },
  },
};
