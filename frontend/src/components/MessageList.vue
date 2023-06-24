<script setup>
import { ref, reactive, watch, onMounted, onUnmounted, nextTick } from 'vue'

import { getMessages } from '../api'
import { store } from '../store'

const AUTOSCROLL_THRESHOLD = 100

const chat = ref(null)
let chatScrollPos = -1

const messages = reactive([])

const snackbar = ref(false)
const snackbarText = ref('')

let loadingMessages = false
let loadingPastMessages = false

function loadNewMessages() {
  const since = messages.at(-1)?.id

  if (loadingMessages) {
    return
  } else {
    loadingMessages = true
  }

  getMessages(since).then((result) => {
    if (result) {
      chatScrollPos = -1

      messages.push(...result)
    }
  }).catch((error) => {
    snackbarText.value = `Failed to load messages (${error.message})`
    snackbar.value = true
  }).finally(() => {
    loadingMessages = false
  })
}

function loadPastMessages() {
  if (loadingPastMessages) {
    return
  } else {
    loadingPastMessages = true
  }

  const until = messages.at(0)?.id
  if (until == null) {
    throw new Error('Empty chat')
  }

  return getMessages(until, true).then((result) => {
    if (result.length == 0)
      return 0

    messages.unshift(...result)
    chatScrollPos = chat.value.scrollHeight

    return result.length
  }).catch(() => {
    snackbarText.value = `Failed to load past messages (${error.message})`
    snackbar.value = true
  }).finally(() => {
    loadingPastMessages = false
  })
}

function formatDate(timestamp) {
  const date = new Date(timestamp * 1000)

  return date.toLocaleDateString('en-US', {
    weekday: 'short',
    month: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    year: 'numeric',
    hour12: true,
  })
}

function onChatScroll() {
  if (chat.value.scrollTop == 0) {
    loadPastMessages()
  }
}

loadNewMessages()
const fetchInterval = setInterval(() => {
  loadNewMessages()
}, 500)

onMounted(() => {
  let firstScroll = true
  let loadPast = true

  watch(messages, () => {
    nextTick(() => {
      const el = chat.value

      // Automatically load past messages if no scrollbar is present
      if (el.scrollHeight == el.clientHeight && loadPast) {
        loadPastMessages().then((length) => {
          if (length == 0) {
            loadPast = false
          }
        })
      }

      if (chatScrollPos < 0) {
        if (Math.abs(el.scrollHeight - el.scrollTop - el.clientHeight) < AUTOSCROLL_THRESHOLD || firstScroll) {
          // Reposition scroll to the bottom if already at the bottom
          el.scrollTop = el.scrollHeight
          firstScroll = false
        }
      } else {
        // Reposition scroll to previous item position
        el.scrollTop = (el.scrollHeight - chatScrollPos - 1)
      }
    })
  })

  onUnmounted(() => {
    clearInterval(fetchInterval)
  })
})

</script>

<template>
  <div
    ref="chat"
    @scroll="onChatScroll"
    class="chat">
    <v-card
      class="message"
      v-for="message in messages"
      :key="message.id"
      :style="(message.sender.id == store.user.id) ? { 'margin-left': 'auto' } : {}">
      <p>{{ message.text }}</p>
      <v-divider class="my-1" />
      <div class="text-wrap d-flex flex-row">
        <p class="text-caption text-grey d-inline-block">
          {{ formatDate(message.date) }}
        </p>
        <div class="spacer"></div>
        <p class="text-right text-caption text-primary d-inline-block">
          {{ (message.sender.name) ? `${message.sender.name} (${message.sender.username})` : message.sender.username }}
        </p>
      </div>
    </v-card>
  </div>
  <v-snackbar
    v-model="snackbar"
    timeout="1500"
    color="error"
    @click="snackbar = false"
    close-on-content-click>
    <p>{{ snackbarText }}</p>
  </v-snackbar>
</template>

<style scoped>
.chat {
  flex-grow: 1;
  height: 0;
  min-height: 0;

  overflow-y: auto;
  overflow-x: hidden;

  padding: 5px;
  padding-right: 10px;
}

.message {
  width: fit-content;
  height: fit-content;

  max-width: 100%;

  padding: 5px;
  margin-bottom: 5px;

  white-space: pre;
}

.spacer {
  flex-grow: 1;

  min-width: 50px;
}
</style>