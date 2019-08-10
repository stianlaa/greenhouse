import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index.vue'
import FullInfoPanel from '@/components/FullInfoPanel.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/plants/:id',
      name: 'FullInfoPanel',
      component: FullInfoPanel
    },
    {
      path: '/',
      name: 'Index',
      component: Index
    }
  ]
})
