// vue.config.js

const path = require("path");

module.exports = {
    chainWebpack: config => {
      const svgRule = config.module.rule('svg')
  
      // clear all existing loaders.
      // if you don't do this, the loader below will be appended to
      // existing loaders of the rule.
      svgRule.uses.clear()
  
      // add replacement loader(s)
      svgRule
        .use('vue-svg-loader')
          .loader('vue-svg-loader')
    },
    pluginOptions: {
        "style-resources-loader": {
          preProcessor: "scss",
          patterns: [path.resolve(__dirname, "./src/styles/global.scss")]
        }
      }
  }
