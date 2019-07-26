import Vue from 'vue'  
import Vuex from 'vuex'

import { getCurrentWeather, getAllTrays, getAllPlants } from '@/api'

Vue.use(Vuex)

const state = {  
  weather: {},
  trays: {},
  plants: {},
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
  },
  loadAllPlants(context) {
    return getAllPlants()
    .then((response) => {
      context.commit('setAllPlants', {plants: response.data})
    })
  }
}

const mutations = {  
  setCurrentWeather(state, payload) {
    state.weather = payload.weather
  },
  setAllTrays(state, payload) {
    state.trays = payload.trays
  },
  setAllPlants(state, payload) {
    state.plants = payload.plants
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