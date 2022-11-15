<template>
    <v-btn
    :disabled="loading"
    class="ma-1"
    color="blue"
    plain
    @click="logout()"
    >
    Log Out
    </v-btn>
</template>

<script>
  import {firebase_app} from '../main.js'
  export default {
    data () {
      return {
      }
    },
    methods: {
        logout() {
            firebase_app
            .auth()
            .signOut()
            .then(() => {
                alert('Successfully logged out');
                this.$router.push('/login');
            })
            .catch(error => {
                alert(error.message);
                this.$router.push('/login');
            });
        },
        },
  }
</script>