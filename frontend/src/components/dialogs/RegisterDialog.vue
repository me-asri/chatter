<script setup>
import { ref, watch } from 'vue'

import { registerUser } from '../../api'
import { usernameRules, passwordRules, nameRules } from '../../rules'

defineProps({
  color: String
})

const dialog = ref(false)
const loading = ref(false)

const form = ref(null)

const name = ref('')
const username = ref('')
const password = ref('')
const confirmPassword = ref('')

const snackbar = ref(false)
const snackbarHtml = ref('')
const snackbarColor = ref('')

const confirmPasswordRules = [
  v => (!!v) || 'Password is required',
  v => (v === password.value) || 'Passwords do not match'
]

watch(dialog, (state, prevState) => {
  if (state == false) {
    form.value.reset()
  }
})

function register() {
  name.value = name.value?.replace(/\s+/g, ' ').trim()

  form.value.validate().then((result) => {
    if (!result.valid)
      return

    loading.value = true

    registerUser(name.value, username.value, password.value).then(() => {
      dialog.value = false

      snackbarHtml.value = '<p>User registered successfully!</p><p>You may now login.</p>'
      snackbarColor.value = 'success'
    }).catch((error) => {
      snackbarHtml.value = `<p>${error.message}</p>`
      snackbarColor.value = 'error'
    }).finally(() => {
      snackbar.value = true
      loading.value = false
    })
  })
}

</script>

<template>
  <v-dialog
    v-model="dialog"
    max-width="300"
    :persistent="loading">
    <template #activator="{ props }">
      <v-btn :color="color" v-bind="props">
        Register
      </v-btn>
    </template>

    <v-card
      title="Register"
      subtitle="Register a new account">
      <v-card-text>
        <v-form
          ref="form"
          :disabled="loading">
          <v-text-field
            v-model="username"
            label="Username"
            clearable
            :rules="usernameRules"
            prepend-inner-icon="mdi-account" />
          <v-text-field
            v-model="name"
            label="Display name"
            clearable
            :rules="nameRules"
            prepend-inner-icon="mdi-card-account-details" />
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            clearable
            :rules="passwordRules"
            prepend-inner-icon="mdi-lock" />
          <v-text-field
            v-model="confirmPassword"
            label="Confirm password"
            type="password"
            clearable
            :rules="confirmPasswordRules"
            prepend-inner-icon="mdi-lock" />
        </v-form>
      </v-card-text>
      <v-card-actions class="pt-0">
        <v-spacer />
        <v-btn
          v-show="!loading"
          color="grey-darken-2"
          @click="dialog = false">
          Cancel
        </v-btn>
        <v-btn
          color="primary"
          :loading="loading"
          @click="register">
          Register
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <v-snackbar
    v-model="snackbar"
    timeout="2000"
    :color="snackbarColor"
    close-on-content-click>
    <span v-html="snackbarHtml"></span>
  </v-snackbar>
</template>