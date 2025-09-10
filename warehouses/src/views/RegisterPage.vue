
<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2>{{ isLogin ? '用户登录' : '用户注册' }}</h2>
      <el-form 
        ref="authForm" 
        :model="formData" 
        :rules="rules" 
        @submit.prevent="handleSubmit"
      >
        <el-form-item prop="username" v-if="!isLogin">
          <el-input v-model="formData.username" placeholder="4-20位字母数字组合" />
        </el-form-item>
        
        <el-form-item prop="account">
          <el-input 
            v-model="formData.account" 
            :placeholder="isLogin ? '用户名/手机号/邮箱' : '手机号'" 
          />
        </el-form-item>
        
        <el-form-item prop="password" v-if="!showSMSCode">
          <el-input 
            v-model="formData.password" 
            type="password" 
            show-password 
            placeholder="密码（至少8位含大小写和数字）" 
          />
        </el-form-item>
        
        <el-form-item prop="email" v-if="!isLogin">
          <el-input v-model="formData.email" placeholder="请输入邮箱" />
        </el-form-item>
        
        <el-form-item prop="smsCode" v-if="showSMSCode">
          <div class="sms-group">
            <el-input v-model="formData.smsCode" placeholder="6位验证码" />
            <el-button 
              type="primary" 
              :disabled="countdown > 0"
              @click="sendSMSCode"
            >
              {{ countdown > 0 ? `${countdown}s后重试` : '获取验证码' }}
            </el-button>
          </div>
        </el-form-item>
        
        <el-form-item>
          <el-button type="primary" native-type="submit">
            {{ isLogin ? '登录' : '注册' }}
          </el-button>
          <el-button type="text" @click="toggleAuthMode">
            {{ isLogin ? '切换到注册' : '切换到登录' }}
          </el-button>
          <el-button 
            type="text" 
            @click="toggleAuthMethod"
            v-if="isLogin"
          >
            {{ showSMSCode ? '密码登录' : '短信验证码登录' }}
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'

const isLogin = ref(true)
const showSMSCode = ref(false)
const countdown = ref(0)
const authForm = ref(null)

const formData = reactive({
  username: '',
  account: '',
  password: '',
  email: '',
  mobile: '',
  smsCode: ''
})

const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 4, max: 20, message: '长度4-20个字符', trigger: 'blur' }
  ],
  account: [
    { required: true, message: '请输入账号', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/, 
      message: '需含大小写字母和数字', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    { type: 'email', message: '邮箱格式不正确', trigger: 'blur' }
  ],
  mobile: [
    { pattern: /^\+86\d{11}$/, message: '格式如+8613800138000', trigger: 'blur' }
  ],
  smsCode: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
    { len: 6, message: '验证码为6位数字', trigger: 'blur' }
  ]
}

const toggleAuthMode = () => {
  isLogin.value = !isLogin.value
  showSMSCode.value = false
  resetForm()
}

const toggleAuthMethod = () => {
  showSMSCode.value = !showSMSCode.value
}

const sendSMSCode = () => {
  if (!/^\+86\d{11}$/.test(formData.account) && !isLogin.value) {
    ElMessage.error('请输入正确的手机号')
    return
  }
  
  countdown.value = 60
  const timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) clearInterval(timer)
  }, 1000)
  
  ElMessage.success(`验证码已发送至 ${formData.account}`)
}

const resetForm = () => {
  authForm.value?.resetFields()
}

const handleSubmit = () => {
  authForm.value.validate(valid => {
    if (valid) {
      ElMessage.success(isLogin.value ? '登录成功' : '注册成功')
      // 这里添加实际的API调用逻辑
    }
  })
}
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.auth-card {
  width: 450px;
  padding: 40px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #409eff;
}

.sms-group {
  display: flex;
  gap: 10px;
}

.sms-group button {
  width: 140px;
}

.el-form-item:last-child {
  margin-bottom: 0;
  display: flex;
  justify-content: space-between;
}
</style>
