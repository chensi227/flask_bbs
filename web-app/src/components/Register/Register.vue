<template>
  <div>
    <Card style="width:350px;margin: 0 auto" :bordered="false">
      <p slot="title">
        <Icon type="person-add"></Icon>
        注册
      </p>
      <register-form></register-form>
    </Card>
  </div>
</template>
<script>
  import RegisterForm from './RegisterForm.vue'
  export default {
    components:{
      RegisterForm
    }
  }
</script>
