'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  // ROOT_API: '"http://192.168.10.173:8081/rest"'
  ROOT_API: '"http://localhost:8081/rest"'
})