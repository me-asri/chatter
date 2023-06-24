import { reactive } from 'vue'

const store = reactive({
  logged_in: false,
  loading: false,

  user: {
    id: -1,
    username: '',
    name: ''
  }
})

export { store }