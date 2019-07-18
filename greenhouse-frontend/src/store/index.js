import Vue from 'vue'  
import Vuex from 'vuex'

import { getCurrentWeather } from '@/api'

Vue.use(Vuex)

const state = {  
  weather: {},
}

const actions = {  
  loadCurrentWeather(context) {
    return getCurrentWeather()
    .then((response) => {
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
}

const getters = {  
}

const store = new Vuex.Store({  
  state,
  actions,
  mutations,
  getters
})

export default store  