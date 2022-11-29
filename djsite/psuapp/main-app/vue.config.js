const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})


const webpack = require('webpack')
module.exports = defineConfig({
  transpileDependencies : true,
  "publicPath":"/",
  "assetsDir":"static",
  "indexPath":"templetes/index.html",
  configureWebpack:{
    plugins:[
      new webpack.IgnorePlugin({
        resourceRegExp:/^\.\/locales/,
        contextRegExp:/moments/
      }),
    ]
  },
  "filenameHashing":true,

  "devServer":{
    "proxy":{
      "^/api":{
        'target':"http://127.0.0.1:8000", 
        'ws':true,
        'changeOrigin':true
      },
      "^/admin":{
        "target":"http://127.0.0.1:8000",
        "ws":true,
        "changeOrigin":true
      },
    },
  }
})