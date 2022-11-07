<template>
  <v-app class="change-shift">
    <h1 class="text-h6 grey--text">Change Shift/Request Leave</h1>
    <br>
    <p style="margin-left: 2.5em;padding: 0 7em 2em 0;">Pick the date you want to switch/request a leave:</p>
    <div>
    
  </div>
  <br>
    <p style="margin-left: 2.5em;padding: 0 7em 2em 0;">Pick the dates you can work in return:</p>
    <div>
  </div>
    <nav>
      <v-app-bar app color="blue lighten-2" dark>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Shift Manager Pro XL</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn depressed color="blue lighten-2">
          <span>Sign Out</span>
          <v-icon right>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-app-bar>

      <v-navigation-drawer app v-model="drawer" class="primary">
        <v-list dense nav dark>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            router
            :to="item.route"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </nav>
  </v-app>
</template>

<script>

export default {
  components: {  },
  data() {
    return {
      items: [
        { title: "Home", icon: "mdi-view-dashboard", route: "/home-page" },
        { title: "All Schedule", icon: "calander-range", route: "/all-schedule" },
        { title: "Change Shift", icon: "mdi-help-box", route: "/change-shift" },
        { title: "On Leave", icon: "mdi-help-box", route: "/on-leave" },
        { title: "Requests", icon: "mdi-help-box", route: "/request" },
      ],

    };
  },
};
</script>
