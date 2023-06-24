import axios from "axios"

import { store } from "./store"

const API_URL = 'http://127.0.0.1:8000/api'

let authData = {
  token: ''
}

function getErrorMessage(error) {
  return error.response?.data?.detail[0]?.msg ?? error.response?.data?.detail ?? error?.message ?? 'Unknown error'
}

function registerUser(name, username, password) {
  return axios({
    method: 'post',
    url: `${API_URL}/user/`,
    data: {
      name: name,
      username: username,
      password: password
    }
  }).then().catch((error) => {
    throw new Error(getErrorMessage(error))
  })
}

function loginUser(username, password) {
  let data = new FormData()
  data.append('grant_type', 'password')
  data.append('username', username)
  data.append('password', password)

  return axios({
    method: 'post',
    url: `${API_URL}/user/token`,
    data: data
  }).then((resp) => {
    const token = resp.data?.access_token
    if (token == null) {
      throw new Error('Invalid response')
    }

    $cookies.set('token', token)
    resumeAuth()
  }).catch((error) => {
    store.logged_in = false
    throw new Error(getErrorMessage(error))
  })
}

function logoutUser() {
  authData.token = ''
  $cookies.remove('token')

  store.logged_in = false
  store.user = {
    id: -1,
    username: '',
    name: ''
  }
}

function getUserInfo() {
  if (!authData.token) {
    throw new Error('Not authenticated')
  }

  return axios({
    method: 'get',
    url: `${API_URL}/user/me`,
    headers: {
      Authorization: `Bearer ${authData.token}`
    }
  }).then((resp) => {
    return resp.data
  }).catch((error) => {
    throw new Error(getErrorMessage(error))
  })
}

function resumeAuth() {
  if (!$cookies.isKey('token')) {
    return null
  }

  authData.token = $cookies.get('token')

  return getUserInfo().then((info) => {
    store.user = info
    store.logged_in = true
  }).catch((error) => {
    $cookies.remove('token')
    throw error;
  })
}

function updateUser(name = null, old_password = null, new_password = null) {
  if (!authData.token) {
    throw new Error('Not authenticated')
  }

  return axios({
    method: 'put',
    url: `${API_URL}/user/`,
    headers: {
      Authorization: `Bearer ${authData.token}`
    },
    data: {
      name: name,
      old_password: old_password,
      new_password: new_password
    }
  }).then((resp) => {
    store.user = resp.data
  }).catch((error) => {
    throw new Error(getErrorMessage(error))
  })
}

function sendMessage(message) {
  if (!authData.token) {
    throw new Error('Not authenticated')
  }

  return axios({
    method: 'post',
    url: `${API_URL}/message/`,
    data: {
      text: message
    },
    headers: {
      Authorization: `Bearer ${authData.token}`
    }
  }).then((resp) => {
    return resp.data
  }).catch((error) => {
    throw new Error(getErrorMessage(error))
  })
}

function getMessages(since = null, backwards = false) {
  const params = {
    limit: 10,
  }
  if (since != null) {
    if (backwards) {
      params.until = since
    } else {
      params.since = since
    }
  }

  return axios({
    method: 'get',
    url: `${API_URL}/message/`,
    params: params
  }).then((resp) => {
    return resp.data
  }).catch((error) => {
    throw new Error(getErrorMessage(error))
  })
}

export { registerUser, loginUser, logoutUser, resumeAuth, updateUser, sendMessage, getMessages }