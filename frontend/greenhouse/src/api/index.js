import axios from 'axios'

export function getCurrentWeather() {
  return axios.get(`${process.env.ROOT_API}/get_current_weather/`)
}

export function getWeatherFromTo(from, to) { 
    return axios.get(`${process.env.ROOT_API}/get_weather/${from}/${to}`)
}