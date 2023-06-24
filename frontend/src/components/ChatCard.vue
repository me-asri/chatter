<script setup>
import { provide, reactive } from 'vue'

import MessageInput from './MessageInput.vue';
import LoginDialog from './dialogs/LoginDialog.vue';
import RegisterDialog from './dialogs/RegisterDialog.vue';
import MessageList from './MessageList.vue';

import { store } from '../store';

provide('messages-sent', reactive([]))

</script>

<template>
  <v-card
    class="d-flex flex-column elevation-7">
    <v-toolbar
      color="primary">
      <v-toolbar-title>Chatter</v-toolbar-title>
    </v-toolbar>
    <v-banner
      v-show="!store.logged_in"
      class="flex-grow-0 flex-shrink-0"
      icon="mdi-account-outline"
      color="warning"
      min-height="115">
      <template #text>
        <p>Login in order to chat with others!</p>
      </template>
      <template #actions>
        <login-dialog color="warning" />
        <register-dialog color="warning" />
      </template>
    </v-banner>
    <v-card-text class="d-flex flex-column flex-grow-1 pa-0">
      <v-sheet
        class="d-flex flex-column flex-grow-1"
        min-height="100"
        color="grey-lighten-3">
        <message-list />
      </v-sheet>
      <message-input />
    </v-card-text>
  </v-card>
</template>