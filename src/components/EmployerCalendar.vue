<template>
    <div> 

        <v-banner class="pb-6">
            Shift Manager
        </v-banner>


        <v-row class="fill-height">
            <v-col>
                <v-sheet height = "64">
                    <v-toolbar
                        flat
                    >

                    <v-row>

                        <v-col
                            cols = "10"
                            sm = "2"
                        >
                            <v-text-field
                                class = "pl-6"
                                value = ' '
                                label = "Employer Code"
                                readonly
                                filled
                                dense
                                id = "code-text-field"
                                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :type="show1 ? setCode() : ' '"
                                @click:append="show1 = !show1"
                            ></v-text-field>

                        </v-col>

                        <v-spacer></v-spacer>
                        <v-spacer></v-spacer>
                        <v-spacer></v-spacer>
                        <v-spacer></v-spacer>
                        <v-spacer></v-spacer>
                        <v-spacer></v-spacer>

                        <v-col>
                            <v-dialog
                                v-model = "dialog"
                                max-width = "400px"
                            >

                            <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                large
                                elevation = "2"
                                class="ma-1"
                                color="blue"
                                plain
                                v-bind = "attrs"
                                v-on= "on"
                                @click="getEmployees()"
                            >
                            Add Shift
                            </v-btn>
                            </template>
                            <v-card>
                                <v-card-title>Add Shift</v-card-title>
                                <v-card-text>
                                    <v-select
                                        :items="employees"
                                        label="Employee"
                                        v-model = "shiftTo"
                                    ></v-select>
                                    <v-card-actions>
                                        <v-btn
                                        :disabled="loading"
                                        class="ma-1"
                                        color="green"
                                        plain
                                        @click="register()"
                                        >
                                        Add
                                        </v-btn>

                                        <v-btn
                                        :disabled="loading"
                                        class="ma-1"
                                        color="red"
                                        plain
                                        @click="dialog = false"
                                        >
                                        Cancel
                                        </v-btn>

                                    </v-card-actions>
                                </v-card-text>
                            </v-card>
                            </v-dialog>
                        </v-col>

                    </v-row>

                    </v-toolbar>
                </v-sheet>
                <v-sheet height = "500">
                    <v-calendar
                        ref = "calendar"
                    >

                    </v-calendar>

                </v-sheet>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import {firebase_app} from '../main.js';
import {db} from '../main.js';
export default {
    data () {
      return {
        show1: false,
        dialog: false,
        employees:[],
        shiftTo: ''
      }
    },
    methods: {
            async setCode(){
                var user = firebase_app.auth().currentUser;
                var doc = db.collection('users').where('email','==',user.email);
                var code = (await doc.get()).docs[0]._delegate._document.data.value.mapValue.fields.code.stringValue;
                console.log(code);
                document.getElementById("code-text-field").value = code;
            },
            async getEmployees(){
                var user = firebase_app.auth().currentUser;
                var doc = db.collection('users').where('email','==',user.email);
                var code = (await doc.get()).docs[0]._delegate._document.data.value.mapValue.fields.code.stringValue;
                var doc2 = db.collection('users').where('code','==',code).where('role','==','Employee');
                var employeeElements = (await doc2.get()).docs
                this.employees = [];
                for(let i = 0; i<employeeElements.length; i++){
                    this.employees.push(employeeElements[i]._delegate._document.data.value.mapValue.fields.firstname.stringValue + ' ' + employeeElements[i]._delegate._document.data.value.mapValue.fields.lastname.stringValue)
                }
            }
        },
  }
</script>
