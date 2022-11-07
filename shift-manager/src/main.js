import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import VCalendar from "v-calendar"
import axios from "axios"

axios.defaults.withCredentials = true
VueElement.use(VCalendar)
axios.defaults.baseURL = 'http://localhost:8000/'
createApp(App).use(router).mount('#app')
