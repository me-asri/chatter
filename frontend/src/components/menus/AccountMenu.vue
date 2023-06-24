<script setup>
import EditAccountDialog from '../dialogs/EditAccountDialog.vue'

import { store } from '../../store'
import { logoutUser } from '../../api'

</script>

<template>
  <v-menu
    rounded>
    <template v-slot:activator="{ props }">
      <v-btn
        icon
        size="29"
        v-bind="props">
        <v-avatar
          size="29"
          color="brown">
          <v-icon icon="mdi-account" />
        </v-avatar>
      </v-btn>
    </template>
    <v-card>
      <v-card-text class="mx-auto text-center">
        <v-avatar
          class="mb-1"
          color="brown">
          <v-icon icon="mdi-account" />
        </v-avatar>
        <h3>{{ (store.user.name) ? store.user.name : store.user.username }}</h3>
        <p
          v-if="store.user.name"
          class="mt-1">
          {{ store.user.username }}
        </p>
        <v-divider class="my-3" />
        <edit-account-dialog
          variant="text"
          rounded>

        </edit-account-dialog>
        <v-divider class="my-2" />
        <v-btn
          color="error"
          rounded
          variant="text"
          @click="logoutUser">
          Logout
        </v-btn>
      </v-card-text>
    </v-card>
  </v-menu>
</template>