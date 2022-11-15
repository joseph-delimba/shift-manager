<template>
    <v-card 
    class="mx-auto mt-10" 
    width="500" 
    elevation="10"
    >
        <v-card-title>Shift Manager</v-card-title>

        <v-card-text>

            <v-text-field
                prepend-icon="mdi-account-circle" 
                label = "Email"
                v-model="email"
            ></v-text-field>

            <v-text-field
                prepend-icon="mdi-lock"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text' : 'password'"
                name="input-10-1"
                label="Password"
                hint="At least 6 characters"
                counter
                v-model="password"
                @click:append="show1 = !show1"
            ></v-text-field>
    
        </v-card-text>

        <v-divider> </v-divider>
        
        <v-card-actions>

            <v-btn
            :disabled="loading"
            class="ma-1"
            color="blue"
            plain
            @click="login()"
            >
            Log In
            </v-btn>
            
            <v-btn
            :disabled="loading"
            class="ma-1"
            color="green"
            plain
            to='/register'
            >
            Create new account
            </v-btn>

        </v-card-actions>
    </v-card>
</template>

<script>
  import {firebase_app} from '../main.js'
  import {db} from '../main.js';
  export default {
    data () {
      return {
        show1: false,
        password: '',
        email: ''
      }
    },
    methods: {
        login() {
            firebase_app
            .auth()
            .signInWithEmailAndPassword(this.email, this.password)
            .then(async () => {
                alert('Successfully logged in');
                var user = firebase_app.auth().currentUser;
                var doc = db.collection('users').where('email','==',user.email);
                var currentRole = (await doc.get()).docs[0]._delegate._document.data.value.mapValue.fields.role.stringValue;
                if(currentRole == 'Employer'){
                    this.$router.push('/employer-calendar');
                }
                if(currentRole == 'Employee'){
                    this.$router.push('/employee-calendar');
                }
            })
            .catch(error => {
                alert(error.message);
            });
        },
        },
  }
</script>