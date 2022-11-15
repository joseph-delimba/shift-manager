<template>
    <v-card 
    class="mx-auto mt-10" 
    width="500" 
    elevation="10"
    >
        <v-card-title>Sign Up</v-card-title>

        <v-card-text>

            <v-text-field
                prepend-icon="mdi-account-circle" 
                label = "First Name"
                v-model = "firstname"
            ></v-text-field>

            <v-text-field
                prepend-icon="mdi-account-circle" 
                label = "Last Name"
                v-model = "lastname"
            ></v-text-field>

            <v-text-field
                prepend-icon="mdi-account-circle" 
                label = "Email"
                v-model = "email"
            ></v-text-field>

            <v-text-field
                prepend-icon="mdi-lock"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text' : 'password'"
                name="input-10-1"
                label="Password"
                hint="At least 6 characters"
                counter
                @click:append="show1 = !show1"
                v-model = "password"
            ></v-text-field>

            <v-select
                :items="roles"
                label="Role"
                v-model = "role"
            ></v-select>

            <v-text-field
                label = "Employer Code"
                hint = "* Required for employees"
                persistent-hint
                v-model = "code"
            ></v-text-field>
    
        </v-card-text>

        <v-divider> </v-divider>
        
        <v-card-actions>

            <v-btn
            :disabled="loading"
            class="ma-1"
            color="green"
            plain
            @click="register()"
            >
            Sign Up
            </v-btn>

            <v-btn
            :disabled="loading"
            class="ma-1"
            color="blue"
            plain
            to='/login'
            >
            Back to Log In
            </v-btn>

        </v-card-actions>
    </v-card>
</template>

<script>
    //NEED TO SEND A POST REQUEST TO API TO PUT NEW USER IN THE DATABASE
    //FIREBASE UNIQUE ID FOR THE EMPLOYER AS EMPLOYER CODE?
  import {firebase_app} from '../main.js';
  import axios from 'axios';
  import {uid} from 'uid';
  import {db} from '../main.js';
  //import { doc, setDoc } from 'firebase/compat/firestore';
  export default {
    data () {
      return {
        show1: false,
        password: '',
        email: '',
        role: '',
        roles: ['Employer','Employee'],
        code: '',
        firstname: '',
        lastname:''
      }
    },
    methods: {
        //Function to register a user with the given inputs
    register() {
        
        //If the user hasn't selected a role
        if(this.role == ''){
            alert('You must select your role.');
            return;
        }

        //If a user is an employee, but hasn't given an employer code
        if(this.role == 'Employee' && this.code == ''){
            alert('You must include an employer code.');
            return;
        }

        //Try to create a user using firebase
        firebase_app
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then(() => {
            //Success, need to post user to database
            if(this.role == 'Employee'){
                var u_id = uid();
                db.collection('users').doc(u_id).set({
                    id: u_id,
                    firstname: this.firstname,
                    lastname: this.lastname,
                    code: this.code, //when employee, code should be given
                    email: this.email,
                    role: this.role
                });
            }
            if(this.role == 'Employer'){
                var u_id = uid();
                db.collection('users').doc(u_id).set({
                    id: u_id,
                    firstname: this.firstname,
                    lastname: this.lastname,
                    code: u_id, //when employer, code should be generated
                    email: this.email,
                    role: this.role
                });
            }
            alert('Successfully registered! Please login.');
            this.$router.push('/login');
        })
        .catch(error => {
            //Failure
            alert(error.message);
        });
    },
    },
  }
</script>