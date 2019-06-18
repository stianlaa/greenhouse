import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api'

export function getStatus() {  
  return axios.get(`${API_URL}/surveys/`)
}

export function getStatusFromTo(from, to) {  
    return axios.get(`${API_URL}/surveys/${from}/${to}`)
  }

// export function saveSurveyResponse(surveyResponse) {  
//   return axios.put(`${API_URL}/surveys/${surveyResponse.id}/`, surveyResponse)
// }

// export function postNewSurvey(survey) {  
//   return axios.post(`${API_URL}/surveys/`, survey)
// }