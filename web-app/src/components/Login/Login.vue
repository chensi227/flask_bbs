<template>
  <div>
    <Card style="width:350px;margin: 0 auto" :bordered="false">
      <p slot="title">
        <Icon type="log-in"></Icon>
        登录
      </p>
      <login-form></login-form>
    </Card>
  </div>
</template>
<script>
  import LoginForm from './LoginForm'
  export default {
    components:{
      LoginForm
    }
  }
</script>
