<script setup>
import { ref, watch } from 'vue'

import { store } from '../../store'
import { updateUser } from '../../api'
import { passwordRules, nameRules } from '../../rules'

defineProps({
  color: String,
  variant: String,
  rounded: Boolean
})

const dialog = ref(false)
const loading = ref(false)

const form = ref(null)
const passForm = ref(null)

const username = ref('')
const name = ref('')

const changePassword = ref(false)
const oldPassword = ref('')
const newPassword = ref('')
const confirmNewPassword = ref('')

const snackbar = ref(false)
const snackbarHtml = ref('')
const snackbarColor = ref('')

const confirmPasswordRules = [
  v => (!!v) || 'Password is required',
  v => (v === newPassword.value) || 'Passwords do not match'
]

watch(dialog, (state, prevState) => {
  if (state) {
    username.value = store.user.username
    name.value = store.user.name
  }
  else {
    form.value.reset()
    changePassword.value = false
  }
})

watch(changePassword, (state, prevState) => {
  if (!state) {
    passForm.value.reset()
  }
})

function update() {
  name.value = name.value?.replace(/\s+/g, ' ').trim()

  form.value.validate().then((result) => {
    if (!result.valid) {
      return
    }
    passForm.value.validate().then((result) => {
      if (!result.valid && changePassword.value) {
        return;
      }

      loading.value = true

      updateUser(name.value, oldPassword.value, newPassword.value).then(() => {
        dialog.value = false

        snackbarHtml.value = '<p>User updated successfully!</p><p>You may have to refresh to apply changes.</p>'
        snackbarColor.value = 'success'
      }).catch((error) => {
        snackbarHtml.value = `<p>${error.message}</p>`
        snackbarColor.value = 'error'
      }).finally(() => {
        snackbar.value = true
        loading.value = false
      })
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
      <v-btn
        :color="color"
        :variant="variant"
        :rounded="rounded"
        v-bind="props">
        Edit Account
      </v-btn>
    </template>

    <v-card
      title="Update Information"
      subtitle="Update user information">
      <v-card-text>
        <v-form
          ref="form"
          :disabled="loading">
          <v-text-field
            v-model="username"
            label="Username"
            disabled
            prepend-inner-icon="mdi-account" />
          <v-text-field
            v-model="name"
            label="Display name"
            clearable
            :rules="nameRules"
            prepend-inner-icon="mdi-card-account-details" />
          <v-checkbox
            v-model="changePassword"
            label="Change password">
          </v-checkbox>
          <v-form
            ref="passForm"
            v-show="changePassword">
            <v-text-field
              v-model="oldPassword"
              label="Current password"
              type="password"
              clearable
              :rules="passwordRules"
              prepend-inner-icon="mdi-lock" />
            <v-text-field
              v-model="newPassword"
              label="New password"
              type="password"
              clearable
              :rules="passwordRules"
              prepend-inner-icon="mdi-lock" />
            <v-text-field
              v-model="confirmNewPassword"
              label="Confirm new password"
              type="password"
              clearable
              :rules="confirmPasswordRules"
              prepend-inner-icon="mdi-lock" />
          </v-form>
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
          @click="update">
          Update
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