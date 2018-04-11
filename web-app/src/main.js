// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import axios from 'axios'
import 'iview/dist/styles/iview.css'
import JwtToken from './helpers/jwt'
import store from './store/index'

Vue.use(iView);

Vue.config.productionTip = false

Object.defineProperty(Vue.prototype, '$axios', { value: axios });

axios.defaults.baseURL = 'http://127.0.0.1:5000'

axios.defaults.auth = {
  username: '',
  password: '',
}

axios.interceptors.request.use(function (config) {
  if (JwtToken.getToken()){

  }
}, function (error) {
  return Promise.reject(error);
});


router.beforeEach((to, from, next) => {
  if (to.meta.require) {
    if (store.state.token || JwtToken.getToken()) {
      axios.defaults.auth = {
        username: JwtToken.getToken(),
        password: JwtToken.getToken(),
      }
      return next()
    } else {
      return next({'name': 'login'})
    }
  }
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
