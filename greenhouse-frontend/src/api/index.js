import axios from 'axios'

export function getCurrentWeather() {
  return axios.get(`${process.env.ROOT_API}/getweather`)
}

export function getAllTrays() {
  return axios.get(`${process.env.ROOT_API}/gettrayswithplants`)
}