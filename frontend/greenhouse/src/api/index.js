import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api'

export function getCurrentWeather() {  
  console.log("at api!")
  return axios.get(`${API_URL}/get_current_weather/`)
}

export function getWeatherFromTo(from, to) { 
    return axios.get(`${API_URL}/surveys/${from}/${to}`)
  }