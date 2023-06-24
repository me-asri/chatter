<script setup>
import ChatCard from './components/ChatCard.vue'

import { ref, computed } from 'vue'
import { useDisplay } from 'vuetify'

import { resumeAuth } from './api'

const snackbar = ref(false)
const snackbarText = ref('')

// Resume authentication if possible
resumeAuth()?.catch((error) => {
  snackbar.value = true
  snackbarText.value = error.message
})

const { name } = useDisplay()
const height = computed(() => {
  switch (name.value) {
    case 'xs':
    case 'sm':
      return '100%'
    default:
      return null
  }
})
const width = computed(() => {
  switch (name.value) {
    case 'xs':
    case 'sm':
      return '100%'
    default:
      return 800
  }
})
const max_width = computed(() => {
  switch (name.value) {
    case 'xs':
    case 'sm':
      return null
    default:
      return '650'
  }
})
</script>

<template>
  <v-app>
    <v-main>
      <v-sheet
        class="d-flex flex-column justify-center align-center fill-height"
        color="secondary">
        <chat-card
          :width="width"
          :height="height"
          :max-width="max_width"
          min-height="90%" />
      </v-sheet>
    </v-main>
    <v-snackbar
      v-model="snackbar"
      timeout="2000"
      color="error"
      @click="snackbar = false"
      close-on-content-click>
      <p>{{ snackbarText }}</p>
    </v-snackbar>
  </v-app>
</template>