import { createRouter, createWebHashHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import login from '../views/login-page.vue'
import request from '../views/request-page.vue'
import all_schedule from '../views/all-schedule.vue'
import change_shift from '../views/change-shift.vue'
import home_page from '../views/home-page.vue'
import on_leave from '../views/on-leave.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: login
  },
  {
    path: '/request',
    name: 'request',
    component: request
  },
  {
    path: '/all-schedule',
    name: 'all-schedule',
    component: all_schedule
  },
  {
    path: '/change-shift',
    name: 'change-shift',
    component: change_shift
  },
  {
    path: '/home-page',
    name: 'home-page',
    component: home_page
  },
  {
    path: '/on-leave',
    name: 'on-leave',
    component: on_leave
  }
  //{
  //  path: '/',
  //  name: 'home',
  //  component: HomeView
  //},
  //{
  //  path: '/about',
  //  name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  //  component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  //}
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
