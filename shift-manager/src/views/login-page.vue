<template>
  <v-app>
    <v-app-bar app color="blue lighten-2" dark>
      <v-toolbar-title>Shift Manager Pro XL</v-toolbar-title>

    </v-app-bar>

    <v-content>
      <v-card class="mx-auto mt-10" width="500" >
        <v-card-title>Login Area</v-card-title>
        <v-card-text>
          <v-text-field
            prepend-icon="mdi-account-circle" 
            label="User Name"
          ></v-text-field>
          <v-text-field 
            prepend-icon="mdi-lock"
            v-bind:append-icon="password ? 'mdi-eye': 'mdi-eye-off' "
            v-on:click:append="password = !password"
            v-bind:type="password ? 'text' :'password' " 
            label="Password"
          ></v-text-field>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn to='/home-page' color="info">Login</v-btn>
          <v-btn color="info">Register</v-btn>
        </v-card-actions>
      </v-card>
    </v-content>
    <template>
      <v-footer padless dark color="light-blue darken-1">
        <v-col
          class="text-center"
          cols="12"
        >
          {{ new Date().getFullYear() }} — <strong>Shift Manager</strong>
        </v-col>
      </v-footer>
    </template>
  </v-app>
</template>
<script>
export default {
  data(){
    return{
      password: false
    }
  }
}
</script>
