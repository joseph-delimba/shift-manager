import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import firebase from 'firebase'


const firebaseConfig = {  
  'apiKey': "AIzaSyAyrcPx1O7lS2lvBMWIFL-9TY06ZMiACjI",
  'authDomain': "shift-manager-e30cf.firebaseapp.com",
  'projectId': "shift-manager-e30cf",
  'storageBucket': "shift-manager-e30cf.appspot.com",
  'messagingSenderId': "283448715505",
  'appId': "1:283448715505:web:4ba35d0605486df3ace150",
  'measurementId': "G-9Y52X0KKX7",
  'databaseURL': "https://shift-manager-e30cf.firebaseio.com"
};

export const firebase_app = firebase.initializeApp(firebaseConfig);
export const db = firebase.firestore();


Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
