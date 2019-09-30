import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.VUE_APP_SERVER_URL,
  withCredentials: true,
  crossdomain: true
})

export default instance
