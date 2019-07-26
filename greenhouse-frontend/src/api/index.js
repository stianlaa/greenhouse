import axios from 'axios'

export function getCurrentWeather() {
  return axios.get(`${process.env.ROOT_API}/getweather`)
}

export function getAllPlants() {
  return axios.get(`${process.env.ROOT_API}/getplants`)
}

export function getAllTrays() {
  return axios.get(`${process.env.ROOT_API}/gettrayswithplants`)
}