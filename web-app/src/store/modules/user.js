import * as types from './../mutation-type'
export default {
  state : {
    username:null,
    password:null,
  },
  mutations:{
    [types.SET_USER_TOKEN](state,payload){
      state.username = payload.token
      state.password = ''
    }
  }
  ,
}
