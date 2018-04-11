import JwtToken from './../../helpers/jwt'
import * as types from './../mutation-type'

export default {
  actions:{
    login({commit,dispatch},tokenData){
      JwtToken.setToken(tokenData.token)
      commit({
        type:types.SET_USER_TOKEN,
        token:tokenData.token
      })
    }
  }
}
