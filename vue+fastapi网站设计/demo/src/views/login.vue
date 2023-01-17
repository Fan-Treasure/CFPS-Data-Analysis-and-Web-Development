<template>
  <div class="back">
    <div class="inner">

      <div class="login" v-if="login">
        <div class="wenzi">
          <p>欢迎登录</p>
        </div>
        <div class="l1">
          <el-input placeholder="请输入账号" v-model="zhanghao" clearable></el-input>
        </div>
        <div class="l2">
          <el-input placeholder="请输入密码" v-model="mima" show-password></el-input>
        </div>
        <div class="l3">
          <el-link :underline="false" icon="el-icon-edit" @click="dialogVisible2 = true">忘记密码</el-link>
        </div>
        <div class="l4">
          <el-button type="primary" @click="denglu" :loading="load">登录</el-button>
        </div>
      </div>

      <div :class="{zhuce:sig == true,xianshi:sig2==true}" v-if="login">
        <div class="z1">
          <el-button type="primary" plain @click="qiehuan">没有账号，点击注册</el-button>
        </div>
      </div>

      <div :class="{login2:sig == true,xianshi2:sig3==true}" v-if="!login">
        <div class="z2">
          <el-button type="primary" plain @click="qiehuan2">已有账号，点击登陆</el-button>
        </div>
      </div>
      <div class="zhuce2" v-if="!login">
        <div v-show="sig4">
          <div class="wenzi2">
            <p>注册账号</p>
          </div>

          <div class="z3">
            <el-input placeholder="请输入账号" v-model="name" clearable></el-input>
          </div>
          <div class="z4">
            <el-input placeholder="请输入密码" v-model="secret" show-password></el-input>
          </div>
          <div class="z5">
            <el-input placeholder="请再次输入密码" v-model="secret2" show-password></el-input>
          </div>
          <div class="z6">
            <el-button type="primary" @click="handleon" :loading="load">注册</el-button>
          </div>
        </div>
      </div>
    </div>
    <el-dialog title="忘记密码" :visible.sync="dialogVisible2" width="30%">
      <el-form ref="form2" :model="form2" label-width="80px">
        <el-form-item label="账号">
          <el-input v-model="form2.name"></el-input>
        </el-form-item>
        <el-form-item label="修改密码">
          <el-input v-model="form2.secret"></el-input>
        </el-form-item>
        <el-form-item label="确认密码">
          <el-input v-model="form2.secret2"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="handleoff2">取 消</el-button>
        <el-button type="primary" @click="handleon2">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        dialogVisible2: false,
        login: true,
        sig4: false,
        zhanghao: '',
        mima: '',
        sig: true,
        sig2: false,
        sig3: false,
        form2: {
          name: '',
          secret: '',
          secret2: ''
        },
        name: '',
        secret: '',
        secret2: '',
        load:false
      }
    },
    methods: {
      qiehuan() {
         this.$message({
          message: '注册后，系统会自动为您备份数据库，过程大概需要5-10分钟',
          type: 'warning'
        });
        this.sig2 = true
        this.sig3 = false
        clearTimeout(this.timer);
        this.timer = setTimeout(() => {
          this.login = !this.login;
          this.sig4 = true
        }, 3000);

      },
      qiehuan2() {
        this.sig3 = true
        this.sig2 = false
        this.sig4 = false
        clearTimeout(this.timer);
        this.timer = setTimeout(() => {
          this.login = !this.login;
        }, 3000);
      },
      denglu() {
        var signal_denglu = 1;
        axios.post('http://82.156.173.187:8040/login', {
          username: this.zhanghao,
          password: this.mima
        }).then(response => {
          if (response.data.status == 'success') {
            signal_denglu = 0;
            this.$session.set('token', response.data.access_token)
            this.$session.set('rtoken', response.data.refresh_token)
            this.$session.set('username', this.zhanghao)
            this.$session.set('signal', 1)
            this.$router.push('/index');
          } else {
            this.$message.error('登陆失败');
          }
        })
      },
      handleoff() {
        this.dialogVisible = false;
        this.secret = '';
        this.name = '';
        this.secret2 = '';
      },
      handleon() {

        if (!this.name) {
          this.$message.error('请输入账户');
          return false
        }
        if (!this.secret) {
          this.$message.error('请输入密码');
          return false
        }
        if (!this.secret2) {
          this.$message.error('请再次输入密码');
          return false
        }
        if (this.secret2 != this.secret) {
          this.$message.error('密码不一致，请重新输入');
          return false
        }
        this.load = true
        this.dialogVisible = false;
        axios.post('http://82.156.173.187:8040/register', {
          username: this.name,
          password: this.secret
        }).then(res => {
          this.load = false
          console.log(res);
          this.$message({
            message: '恭喜你，注册成功',
            type: 'success'
          });
        })

        this.secret = '';
        this.name = '';
        this.secret2 = '';
      },
      handleoff2() {
        this.dialogVisible2 = false;
        this.form2.secret = '';
        this.form2.name = '';
        this.form2.secret2 = '';
      },
      handleon2() {

        if (!this.form2.name) {
          this.$message.error('请输入账户');
          return false
        }
        if (!this.form2.secret) {
          this.$message.error('请输入密码');
          return false
        }
        if (!this.form2.secret2) {
          this.$message.error('请再次输入密码');
          return false
        }
        if (this.form2.secret2 != this.form2.secret) {
          this.$message.error('密码不一致，请重新输入');
          return false
        }
        this.dialogVisible2 = false;
        axios.post('http://82.156.173.187:8040/change_password', {
          username: this.form2.name,
          new_password: this.form2.secret
        }).then(res => {
          console.log(res);
          this.$message({
            message: '恭喜你，修改密码成功',
            type: 'success'
          });
        })
        this.form2.secret0 = '';
        this.form2.secret = '';
        this.form2.name = '';
        this.form2.secret2 = '';
      },

    }

  }
</script>

<style>
  .back {
    background: url(https://s3.bmp.ovh/imgs/2022/02/dabcf24092ceae6f.jpg);
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    overflow: hidden;
    overflow-y: hidden;
    overflow: hidden;
    overflow-y: hidden;
    height: 100vh;
  }

  .inner {
    width: 60%;
    margin-left: 20%;
    height: 60vh;
    margin-top: 20vh;
    background-color: white;
    border-radius: 15px;
    opacity: 0.9;
    display: flex;
  }

  .login {
    width: 50%;
    height: 60vh;
    border-radius: 15px;
    text-align: center;
    font-size: 20px;
  }

  .login2 {
    width: 50%;
    height: 60vh;
    border-radius: 15px;
    background-color: rgb(130, 160, 130);
    text-align: center;
    font-size: 20px;
  }

  .wenzi {
    margin-top: 15vh;
  }

  .wenzi2 {
    margin-top: 10vh;
  }

  .l1 {
    width: 70%;
    margin-left: 15%;
    margin-top: 1vh;
    margin-bottom: 2vh;
  }

  .l2 {
    width: 70%;
    margin-left: 15%;
    margin-top: 1vh;
    margin-bottom: 1vh;
  }

  .l3 {
    margin-left: 50%;
  }

  .zhuce {
    width: 50%;
    height: 60vh;
    text-align: center;
    border-radius: 15px;
    font-size: 20px;
    background-color: rgb(130, 160, 130);
  }

  .zhuce2 {
    width: 50%;
    height: 60vh;
    text-align: center;
    border-radius: 15px;
    font-size: 20px;
  }

  .z1 {
    margin-top: 25vh;
  }

  .z2 {
    margin-top: 25vh;
  }

  .z3 {
    width: 70%;
    margin-left: 15%;
    margin-top: 1vh;
    margin-bottom: 2vh;
  }

  .z4 {
    width: 70%;
    margin-left: 15%;
    margin-top: 1vh;
    margin-bottom: 2vh;
  }

  .z5 {
    width: 70%;
    margin-left: 15%;
    margin-top: 1vh;
    margin-bottom: 2vh;
  }

  .xianshi {
    animation: change;
    animation-duration: 3s
  }

  .xianshi2 {
    animation: change2;
    animation-duration: 3s
  }

  @keyframes change {
    0% {
      transform: translateX(0);
    }

    100% {
      transform: translateX(-29.4vw);
    }
  }

  @keyframes change2 {
    0% {
      transform: translateX(0);
    }

    100% {
      transform: translateX(29.4vw);
    }
  }
</style>