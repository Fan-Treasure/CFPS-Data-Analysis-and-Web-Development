import Vue from 'vue'
import VueRouter from 'vue-router'
import f from '../views/function.vue'
import introduction from '../views/introduction.vue'
import login from '../views/login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/index',
    name: 'function',
    component: f
  },
  {
    path: '/',
    name: 'introduction',
    component: introduction
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },

]

const router = new VueRouter({
  routes
})

export default router
