module.exports = {
    devServer: {
      proxy: {
          '/ontobud': {
              target: 'http://localhost:7200',
              secure: true,
              changeOrigin: true,
              pathRewrite: {
                  '^/graphdb': ''
              }
          },
      }
    }
  };