import Vue from 'vue'
import Router from 'vue-router'
import Store from './../store/index'
import JwtToken from './../helpers/jwt'
import axios from 'axios'

import HelloWorld from '@/components/HelloWorld'
import Register from '../components/Register/Register'
import Login from '../components/Login/Login'
import Home from '../components/Home/Home'
import jwt from "../helpers/jwt";

Vue.use(Router)

let routes = [
  {
    path: '/home',
    name: 'home',
    component: Home,
    meta:{require:true},
  },
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld,
    meta:{}
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta:{}
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta:{}
  },
]

const route = new Router({
  mode:'history',
  routes
})



// route.beforeEach((to, from, next) => {
//   if (to.meta.require) {
//     if (Store.state.token || JwtToken.getToken()) {
//       return next()
//     } else {
//       return next({'name': 'login'})
//     }
//   }
//   next()
// })


export default route
