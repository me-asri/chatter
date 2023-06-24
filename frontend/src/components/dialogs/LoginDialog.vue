<script setup>
import { ref, watch } from 'vue'

import { loginUser } from '../../api'
import { usernameRules, passwordRules } from '../../rules'

defineProps({
  color: String
})

const dialog = ref(false)
const loading = ref(false)

const form = ref(null)

const username = ref('')
const password = ref('')

const snackbar = ref(false)
const snackbarText = ref('')
const snackbarColor = ref('')

watch(dialog, (state, prevState) => {
  if (state == false) {
    form.value.reset()
  }
})

function login() {
  form.value.validate().then((result) => {
    if (!result.valid)
      return

    loading.value = true

    loginUser(username.value, password.value).then(() => {
      snackbarText.value = 'Logged in successfully!'
      snackbarColor.value = 'success'

      dialog.value = false
    }).catch((error) => {
      snackbarText.value = error.message
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
        Login
      </v-btn>
    </template>

    <v-card
      title="Login"
      subtitle="Login into your account">
      <v-card-text>
        <v-form
          ref="form"
          :disabled="loading"
          @submit.prevent="login">
          <v-text-field
            v-model="username"
            label="Username"
            clearable
            required
            :rules="usernameRules"
            prepend-inner-icon="mdi-account" />
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            clearable
            required
            :rules="passwordRules"
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
          @click="login">
          Login
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <v-snackbar
    v-model="snackbar"
    timeout="2000"
    :color="snackbarColor"
    close-on-content-click>
    <p>{{ snackbarText }}</p>
  </v-snackbar>
</template>