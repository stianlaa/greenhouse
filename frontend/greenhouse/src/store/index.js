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
      console.log("response")
      console.log(response)
      console.log(response.data)
      context.commit('setCurrentWeather', {weather: response.data})
    })
  }
}

const mutations = {  
  setCurrentWeather(state, payload) {
    console.log("payload")
    console.log(payload)
    state.weather = payload.weather
  }
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