const { defineConfig } = require('@vue/cli-service');
const path = require('path');
module.exports = defineConfig({
  lintOnSave: false,
  transpileDependencies: true,
  configureWebpack: {
    resolve: {
      alias: {
        sileo: path.resolve(__dirname, './src/lib/sileo/restmodel.js'),
      },
    },
  },
});