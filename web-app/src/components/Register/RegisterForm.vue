<template>
  <div>
      <Form ref="registerForm" :model="registerForm" :rules="rule" :label-width="60">
        <FormItem label="用户名" prop="name">
          <Input v-model="registerForm.name" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="邮箱" prop="mail">
          <Input v-model="registerForm.mail" placeholder="请输入邮箱"></Input>
        </FormItem>
        <FormItem label="密码" prop="passwd">
          <Input type="password" v-model="registerForm.passwd"></Input>
        </FormItem>
        <FormItem label="确认密码" prop="passwdCheck">
          <Input type="password" v-model="registerForm.passwdCheck"></Input>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="handleSubmit('registerForm')">提交</Button>
          <Button type="ghost" @click="handleReset('registerForm')" style="margin-left: 8px">重置</Button>
        </FormItem>
      </Form>
  </div>
</template>
<script>
  export default {
    data () {
      const validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.registerForm.passwdCheck !== '') {
            // 对第二个密码框单独验证
            this.$refs.registerForm.validateField('passwdCheck');
          }
          callback();
        }
      };
      const validatePassCheck = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入确认密码'));
        } else if (value !== this.registerForm.passwd) {
          callback(new Error('两次密码不一致'));
        } else {
          callback();
        }
      };
      return {
        registerForm: {
          name:'',
          passwd: '',
          passwdCheck: '',
          mail:'',
        },
        rule: {
          name: [
            { required: true, message: '用户名不能为空', trigger: 'blur' }
          ],
          passwd: [
            { validator: validatePass, trigger: 'blur' }
          ],
          passwdCheck: [
            { validator: validatePassCheck, trigger: 'blur' }
          ],
          mail: [
            { required: true, message: '邮箱不能为空', trigger: 'blur' },
            { type: 'email', message: '请输入正确的邮箱', trigger: 'blur' }
          ],
        }
      }
    },
    methods: {
      handleSubmit (name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            console.log(this.registerForm);
            this.$Message.success('Success!');
          } else {
            this.$Message.error('请验证了再提交');
          }
        })
      },
      handleReset (name) {
        this.$refs[name].resetFields();
      }
    }
  }
</script>
