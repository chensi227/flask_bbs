<template>
  <div>
    <Form ref="loginForm" :model="loginForm" :rules="rule" :label-width="60">
      <FormItem label="用户名" prop="name">
        <Input v-model="loginForm.name" placeholder="请输入用户名"></Input>
      </FormItem>
      <FormItem label="密码" prop="passwd">
        <Input type="password" v-model="loginForm.passwd"></Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit('loginForm')">提交</Button>
        <Button type="ghost" @click="handleReset('loginForm')" style="margin-left: 8px">重置</Button>
      </FormItem>
    </Form>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        loginForm: {
          name:'',
          passwd: '',
        },
        rule: {
          name: [
            { required: true, message: '用户名不能为空', trigger: 'blur' }
          ],
          passwd: [
            { required: true, message: '密码不能为空', trigger: 'blur' }
          ],
        }
      }
    },
    methods: {
      handleSubmit (name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            this.$axios.defaults.auth = {
              username: this.loginForm.name,
              password: this.loginForm.passwd
            }

            this.$axios.get('/api/token/').then(response => {
              //this.$Message.success("提交成功")
              let data = response.data
              console.log(data)
              // 保存token
              this.$store.dispatch('login', data)
              this.$router.push('/home')
            }).catch(error => {
              this.$Message.error(error.status)
            })

            this.$Message.success('Success!');
          } else {
            this.$Message.error('表单验证失败');
          }
        })
      },
      handleReset (name) {
        this.$refs[name].resetFields();
      }
    }
  }
</script>
