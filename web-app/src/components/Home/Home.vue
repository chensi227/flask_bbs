<template>
  <div class="layout">
    <Menu mode="horizontal" theme="dark" active-key="1">
      <Menu-item key="100" name="logo">
        {{ title }}
      </Menu-item>
      <div class="layout-nav">
        <Menu-item key="1" name="导航一">
          <Icon type="ios-navigate"></Icon>
          导航一
        </Menu-item>
        <Menu-item key="2" name="导航二">
          <Icon type="ios-keypad"></Icon>
          导航二
        </Menu-item>
        <Menu-item key="3" name="导航三">
          <Icon type="ios-analytics"></Icon>
          导航三
        </Menu-item>
        <Menu-item key="4" name="导航四">
          <Icon type="ios-paper"></Icon>
          导航四
        </Menu-item>
      </div>
    </Menu>
    <div class="layout-content">
      <Row>
        <i-col span="4">
          <Menu active-key="1-2" width="auto" :open-keys="['1']" theme="dark">
            <Submenu key="1" name="submenu">
              <template slot="title">
                <Icon type="ios-navigate"></Icon>
                导航一
              </template>
              <Menu-item key="1-1" name="menu">选项 1</Menu-item>
              <Menu-item key="1-2" name="menu">选项 2</Menu-item>
              <Menu-item key="1-3" name="menu">选项 3</Menu-item>
            </Submenu>
            <Submenu key="2" name="submenu">
              <template slot="title">
                <Icon type="ios-keypad"></Icon>
                导航二
              </template>
              <Menu-item key="2-1" name="menu">选项 1</Menu-item>
              <Menu-item key="2-2" name="menu">选项 2</Menu-item>
            </Submenu>
            <Submenu key="3" name="submenu"  >
              <template slot="title">
                <Icon type="ios-analytics"></Icon>
                导航三
              </template>
              <Menu-item key="3-1" name="menu">选项 1</Menu-item>
              <Menu-item key="3-2" name="menu">选项 2</Menu-item>
            </Submenu>
          </Menu>
        </i-col>
        <i-col span="20">
          <div class="layout-content-main">内容区域</div>
        </i-col>
      </Row>
    </div>
    <div class="layout-copy">
      2011-2016 &copy; TalkingData
    </div>
  </div>
</template>
<script>
  import Jwttoken from './../../helpers/jwt'
  export default {
    name:'home',
    data(){
      return {
        title:'木小撇'
      }
    },
    mounted(){
      console.log(Jwttoken.getToken())
    },
    created(){
      this.$axios.get('/api/resource/').then(response => {
        let data = response.data
        console.log(data)
      }).catch(error => {
        this.$Message.error(error.status)
      })
    }

  }
</script>

<style scoped>
  .layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
  }
  .layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
  }
  .layout-nav{
    width: 500px;
    margin: 0 auto;
  }
  .layout-assistant{
    width: 300px;
    margin: 0 auto;
    height: inherit;
  }
  .layout-breadcrumb{
    padding: 10px 15px 0;
  }
  .layout-content{
    min-height: 200px;
    margin: 15px;
    overflow: hidden;
    background: #fff;
    border-radius: 4px;
  }
  .layout-content-main{
    padding: 10px;
  }
  .layout-copy{
    text-align: center;
    padding: 10px 0 20px;
    color: #9ea7b4;
  }
</style>
