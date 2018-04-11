import Vue from 'vue'

import Vuex from 'vuex'

import mutations from './mutations'

import actions from './actions'

import Login from './modules/login'

import User from './modules/user'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {

  },
  mutations,
  actions,
  modules: {
    Login,
    User
  }
});

export default store;
