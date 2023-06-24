import { createApp } from 'vue'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
// Vuetify icons
import '@mdi/font/css/materialdesignicons.css'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
// Vuetify colors
import colors from 'vuetify/lib/util/colors'


// vue-cookies plugin
import VueCookies from 'vue-cookies'

const vuetify = createVuetify({
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    }
  },
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
          primary: colors.brown.darken1,
          secondary: colors.brown.lighten4
        }
      }
    }
  }
})

createApp(App)
  .use(vuetify)
  .use(VueCookies, { expires: '7d' })
  .mount('#app')
