import axios from 'axios'

export function getCurrentWeather() {
  return axios.get(`${process.env.ROOT_API}/getweather`)
}