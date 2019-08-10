import axios from 'axios'

// todo: split up modules

// weather

export function getCurrentWeather() {
  return axios.get(`${process.env.ROOT_API}/rest/weather/getweather`)
}

// greenhouse 

export function getAllPlants() {
  return axios.get(`${process.env.ROOT_API}/rest/greenhouse/getplants`)
}

export function getAllTrays() {
  return axios.get(`${process.env.ROOT_API}/rest/greenhouse/gettrayswithplants`)
}

// watering

export function getNextWatering() {
  return axios.get(`${process.env.ROOT_API}/rest/watering/nextwatering`)
}

export function startWateringSchedule() {
  return axios.get(`${process.env.ROOT_API}/rest/watering/start`)
}

export function stopWateringSchedule() {
  return axios.get(`${process.env.ROOT_API}/rest/watering/stop`)
}

export function waterTrayManually(trayId, mlVolume) {
  // return axios.get(`${process.env.ROOT_API}/rest/watering/watertray/{}/{}`)
  return axios.get(`${process.env.ROOT_API}/rest/watering/watertray/`, {
    params: {
      trayid: trayId,
      mlvolume: mlVolume
    }
  })
}

