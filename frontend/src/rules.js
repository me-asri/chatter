const usernameRules = [
  v => !!v || 'Username is required',
  v => (v && /^[a-z0-9]+$/i.test(v)) || 'Only a-z, 0-9 allowed',
  v => (v && v.length >= 4) || 'Username is too short',
  v => (v && v.length <= 16) || 'Username is too long',
]
const passwordRules = [
  v => !!v || 'Password is required',
  v => (v && v.length >= 8) || 'Password must be more than 8 characters'
]
const nameRules = [
  v => (v.length <= 30) || 'Name is too long',
]

export { usernameRules, passwordRules, nameRules }