<script setup>
import AccountMenu from './menus/AccountMenu.vue'

import { ref, computed } from 'vue'

import { store } from '../store'
import { sendMessage } from '../api'

const form = ref(null)

const snackbar = ref(false)
const snackbarText = ref('')

const loading = ref(false)

const message = ref('')

const sendButtonDisabled = computed(() => (message.value) ? false : true)
const inputDisabled = computed(() => (store.logged_in) ? false : true)

function showSnackbar(message) {
  snackbar.value = true
  snackbarText.value = message
}

function send() {
  message.value = message.value?.trim()
  if (!message.value) {
    return
  }

  loading.value = true

  sendMessage(message.value).then(() => {
    form.value.reset()
  }).catch((error) => {
    showSnackbar(error.message)
  }).finally(() => {
    loading.value = false
  })
}
</script>

<template>
  <v-form
    class="mx-2 my-2"
    ref="form"
    @submit.prevent="send">
    <v-text-field
      v-model="message"
      :disabled="inputDisabled"
      color="primary"
      hide-details
      clearable
      single-line
      autocomplete="off"
      density="compact"
      label="Write a message…"
      required
      @click:append="send">
      <template #prepend>
        <account-menu />
      </template>
      <template #append>
        <v-btn
          icon="mdi-send"
          size="28"
          variant="text"
          color="primary"
          :loading="loading"
          :disabled="sendButtonDisabled"
          @click="send">
        </v-btn>
      </template>
    </v-text-field>
  </v-form>
  <v-snackbar
    v-model="snackbar"
    timeout="1500"
    color="error">
    <p>{{ snackbarText }}</p>
  </v-snackbar>
</template>