import Vue from 'vue'  
import Vuex from 'vuex'

import { getCurrentWeather, getAllTrays } from '@/api'

Vue.use(Vuex)

const state = {  
  weather: {},
  trays: {},
}

const actions = {  
  loadCurrentWeather(context) {
    return getCurrentWeather()
    .then((response) => {
      context.commit('setCurrentWeather', {weather: response.data})
    })
  },
  loadAllTrays(context) {
    return getAllTrays()
    .then((response) => {
      context.commit('setAllTrays', {trays: response.data})
    })
  }
}

const mutations = {  
  setCurrentWeather(state, payload) {
    state.weather = payload.weather
  },
  setAllTrays(state, payload) {
    state.trays = payload.trays
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