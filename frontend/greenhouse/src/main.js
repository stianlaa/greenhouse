import Vue from 'vue'
import App from './App.vue'
import store from './store'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  components: {
    store,
  }
}).$mount('#app')

var vm = new Vue({
  // options
})
