<template>
  <div>
    <v-app-bar>
      <v-app-bar-title>Shift Manager</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field
        class="mt-7 ml-16"
        value=""
        outlined
        disabled
        readonly
        dense
        id="code-text-field"
      ></v-text-field>
    </v-app-bar>

    <v-row class="fill-height">
      <v-col>
        <!--Dialog to add shifts-->
        <v-dialog v-model="dialog" max-width="500">
          <v-card>
            <v-container>
              <v-form @submit.prevent="addEvent">
                <v-text-field
                  v-model="name"
                  type="text"
                  label="Name (required)"
                >
                </v-text-field>
                <v-text-field v-model="details" type="text" label="Details">
                </v-text-field>
                <v-text-field
                  v-model="start"
                  type="date"
                  label="Day (required)"
                >
                </v-text-field>
                <v-text-field
                  v-model="startTime"
                  type="text"
                  label="Start time (0:00-24:00)"
                >
                </v-text-field>
                <v-text-field
                  v-model="endTime"
                  type="text"
                  label="End time (0:00-24:00)"
                >
                </v-text-field>
                <v-text-field
                  v-model="color"
                  type="color"
                  label="Color (click to open menu)"
                >
                </v-text-field>
                <v-select
                  :items="employees"
                  label="Employee"
                  v-model="shiftTo"
                ></v-select>
                <v-btn
                  type="submit"
                  color="primary"
                  class="mr-4"
                  @click="dialog = false"
                >
                  Add Shift
                </v-btn>
              </v-form>
            </v-container>
          </v-card>
        </v-dialog>

        <template>
          <v-row class="fill-height">
            <v-col>
              <v-sheet height="64">
                <v-toolbar flat>
                  <v-btn
                    outlined
                    class="mr-4"
                    color="grey darken-2"
                    @click="setToday"
                  >
                    Today
                  </v-btn>
                  <v-btn
                    color="primary"
                    class="mr-4"
                    @click="
                      dialog = true;
                      getEmployees();
                    "
                    dark
                  >
                    Add Shift
                  </v-btn>
                  <v-btn fab text small color="grey darken-2" @click="prev">
                    <v-icon small> mdi-chevron-left </v-icon>
                  </v-btn>
                  <v-btn fab text small color="grey darken-2" @click="next">
                    <v-icon small> mdi-chevron-right </v-icon>
                  </v-btn>
                  <v-toolbar-title v-if="$refs.calendar">
                    {{ $refs.calendar.title }}
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-menu bottom right>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        outlined
                        color="grey darken-2"
                        v-bind="attrs"
                        v-on="on"
                      >
                        <span>{{ typeToLabel[type] }}</span>
                        <v-icon right> mdi-menu-down </v-icon>
                      </v-btn>
                    </template>
                    <v-list>
                      <v-list-item @click="type = 'day'">
                        <v-list-item-title>Day</v-list-item-title>
                      </v-list-item>
                      <v-list-item @click="type = 'week'">
                        <v-list-item-title>Week</v-list-item-title>
                      </v-list-item>
                      <v-list-item @click="type = 'month'">
                        <v-list-item-title>Month</v-list-item-title>
                      </v-list-item>
                      <v-list-item @click="type = '4day'">
                        <v-list-item-title>4 days</v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-menu>
                </v-toolbar>
              </v-sheet>
              <v-sheet height="445">
                <v-calendar
                  ref="calendar"
                  v-model="focus"
                  color="primary"
                  :events="events"
                  :event-color="getEventColor"
                  :type="type"
                  @click:event="showEvent"
                  @click:more="viewDay"
                  @click:date="viewDay"
                  @change="updateRange"
                ></v-calendar>
                <v-menu
                  v-model="selectedOpen"
                  :close-on-content-click="false"
                  :activator="selectedElement"
                  offset-x
                >
                  <v-card color="grey lighten-4" min-width="350px" flat>
                    <v-toolbar :color="selectedEvent.color" dark>
                      <v-btn @click="deleteEvent(selectedEvent.id)" icon>
                        <v-icon>mdi-delete</v-icon>
                      </v-btn>
                      <v-toolbar-title
                        v-html="selectedEvent.name"
                      ></v-toolbar-title>
                      <v-spacer></v-spacer>
                    </v-toolbar>
                    <v-card-text>
                      <form v-if="currentlyEditing !== selectedEvent.id">
                        {{ selectedEvent.details }}
                      </form>
                      <form v-else>
                        <textarea
                          v-model="selectedEvent.details"
                          type="text"
                          style="width: 100%"
                          :min-height="100"
                          placeholder="add note"
                        ></textarea>
                      </form>
                    </v-card-text>
                    <v-card-actions>
                      <v-btn
                        text
                        color="secondary"
                        @click="selectedOpen = false"
                      >
                        Close
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-menu>
              </v-sheet>
            </v-col>
          </v-row>
        </template></v-col
      ></v-row
    >
  </div>
</template>



<script>
import { firebase_app } from "../main.js";
import { db } from "../main.js";
export default {
  data() {
    return {
      show1: false,
      dialog: false,
      employees: [],
      shiftTo: "",
      today: new Date().toISOString().substr(0, 10),
      focus: new Date().toISOString().substr(0, 10),
      type: "month",
      typeToLabel: {
        month: "Month",
        week: "Week",
        day: "Day",
        "4day": "4 Days",
      },
      name: null,
      details: null,
      start: null,
      end: null,
      color: "#1976D2",
      endTime: "",
      startTime: "",
      currentlyEditing: null,
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
    };
  },
  mounted() {
    this.getEvents();
    this.setCode();
  },
  methods: {
    async setCode() {
      var user = firebase_app.auth().currentUser;
      var doc = db.collection("users").where("email", "==", user.email);
      var code = (await doc.get()).docs[0]._delegate._document.data.value
        .mapValue.fields.code.stringValue;
      document.getElementById("code-text-field").value =
        "Employer Code: " + code;
    },
    async getEmployees() {
      var user = firebase_app.auth().currentUser;
      var doc = db.collection("users").where("email", "==", user.email);
      var code = (await doc.get()).docs[0]._delegate._document.data.value
        .mapValue.fields.code.stringValue;
      var doc2 = db
        .collection("users")
        .where("code", "==", code)
        .where("role", "==", "Employee");
      var employeeElements = (await doc2.get()).docs;
      this.employees = [];
      for (let i = 0; i < employeeElements.length; i++) {
        this.employees.push(
          employeeElements[i]._delegate._document.data.value.mapValue.fields
            .firstname.stringValue +
            " " +
            employeeElements[i]._delegate._document.data.value.mapValue.fields
              .lastname.stringValue
        );
      }
    },
    async getEvents() {
      var user = firebase_app.auth().currentUser;
      let snapshot = await db
        .collection("events")
        .where("employer", "==", user.email)
        .get();
      let events = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        events.push(appData);
      });
      this.events = events;
    },
    async addEvent() {
      if (
        this.name &&
        this.start &&
        this.shiftTo &&
        this.startTime &&
        this.endTime
      ) {
        var user = firebase_app.auth().currentUser;
        const arrayName = this.shiftTo.split(" ");
        let toFirstName = arrayName[0];
        let toLastName = arrayName[1];
        var doc = db.collection("users").where("email", "==", user.email);
        var code = (await doc.get()).docs[0]._delegate._document.data.value
          .mapValue.fields.code.stringValue;
        var doc2 = db
          .collection("users")
          .where("firstname", "==", toFirstName)
          .where("lastname", "==", toLastName)
          .where("code", "==", code);
        var toEmail = (await doc2.get()).docs[0]._delegate._document.data.value
          .mapValue.fields.email.stringValue;
        await db.collection("events").add({
          name: this.name,
          details: this.details,
          start: this.start + " " + this.startTime,
          end: this.start + " " + this.endTime,
          color: this.color,
          employer: user.email,
          employee: toEmail,
        });
        this.getEvents();
        this.name = "";
        this.details = "";
        this.start = "";
        this.end = "";
        this.color = "#1976D2";
        this.shiftTo = "";
        this.startTime = "";
        this.endTime = "";
      } else {
        alert("Job, start, end, and employee are required");
      }
    },
    async deleteEvent(ev) {
      await db.collection("events").doc(ev).delete();
      this.selectedOpen = false;
      this.getEvents();
    },
    viewDay({ date }) {
      this.focus = date;
      this.type = "day";
    },
    getEventColor(event) {
      return event.color;
    },
    setToday() {
      this.focus = this.today;
    },
    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },
    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        this.selectedElement = nativeEvent.target;
        requestAnimationFrame(() =>
          requestAnimationFrame(() => (this.selectedOpen = true))
        );
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        requestAnimationFrame(() => requestAnimationFrame(() => open()));
      } else {
        open();
      }

      nativeEvent.stopPropagation();
    },
    updateRange({ start, end }) {
      const events = [];

      const min = new Date(`${start.date}T00:00:00`);
      const max = new Date(`${end.date}T23:59:59`);
      const days = (max.getTime() - min.getTime()) / 86400000;
      const eventCount = this.rnd(days, days + 20);

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0;
        const firstTimestamp = this.rnd(min.getTime(), max.getTime());
        const first = new Date(firstTimestamp - (firstTimestamp % 900000));
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000;
        const second = new Date(first.getTime() + secondTimestamp);

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        });
      }

      this.events = events;
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
  },
};
</script>
