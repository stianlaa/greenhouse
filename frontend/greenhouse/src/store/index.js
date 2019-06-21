// src/store/index.js

import Vue from 'vue'  
import Vuex from 'vuex'
import { getCurrentWeather } from '@/api'

Vue.use(Vuex)

const state = {  
  // single source of data
  weather: {},
}

const actions = {  
  // asynchronous operations
  loadCurrentWeather(context) {
    return getCurrentWeather()
    .then((response) => {
      context.commit('setCurrentWeather', {weather: response.data})
    })
  }
}

const mutations = {  
  // isolated data mutations
}

const getters = {  
  // reusable data accessors
}

const store = new Vuex.Store({  
  state,
  actions,
  mutations,
  getters
})

export default store  