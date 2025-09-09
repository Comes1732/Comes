
<template>
  <!-- 登录页面容器，设置背景图片 -->
  <div class="login-page" :style="{ backgroundImage: 'url(/static/images/MSI.png)' }">
    <!-- 主容器使用Flexbox布局，添加鼠标移动特效 -->
    <div 
      class="login-container"
      @mousemove="handleMouseMove"
      :style="{
        transform: `perspective(1000px) rotateX(${tiltY}deg) rotateY(${tiltX}deg)`
      }"
    >
      <!-- 半透明登录卡片 -->
      <div class="login-card">
        <!-- 登录标题 -->
        <h2>用户登录</h2>
        
        <!-- 登录表单 -->
        <form @submit.prevent="handleSubmit">
          <!-- 用户名输入组 -->
          <div class="form-group">
            <label for="username">用户名</label>
            <input 
              type="text" 
              id="username" 
              v-model="form.username" 
              placeholder="请输入用户名"
            >
          </div>
          
          <!-- 密码输入组 -->
          <div class="form-group">
            <label for="password">密码</label>
            <input 
              type="password" 
              id="password" 
              v-model="form.password" 
              placeholder="请输入密码"
            >
          </div>
          
          <!-- 登录按钮 -->
          <button type="submit" class="login-btn">登 录</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
// 引入Vue响应式API
import { ref } from 'vue'

// 定义表单数据响应式对象
const form = ref({
  username: '',
  password: ''
})

// 定义卡片倾斜角度响应式变量
const tiltX = ref(0)
const tiltY = ref(0)

/**
 * 处理鼠标移动事件，实现3D倾斜效果
 * @param {MouseEvent} e - 鼠标事件对象
 */
const handleMouseMove = (e) => {
  // 获取容器位置和尺寸信息
  const { left, top, width, height } = e.currentTarget.getBoundingClientRect()
  // 计算鼠标在容器内的相对位置(-0.5到0.5)
  const x = (e.clientX - left) /* width - 0.5 */
  const y = (e.clientY - top) /* height - 0.5 */
  // 根据鼠标位置设置倾斜角度
  tiltX.value = y * 0.005 // 垂直移动影响X轴旋转
  tiltY.value = x * -0.008 // 水平移动影响Y轴旋转
}

/**
 * 处理表单提交事件
 */
const handleSubmit = () => {
    // 表单验证逻辑
    console.log(form.value.username)
    console.log(form.value.password)
    // 1. 重置错误状态
    if (!form.value.username.trim()) {
        throw new Error('用户名不能为空')
      }
      if (form.value.password.length < 6) {
        throw new Error('密码长度不能少于6位')
      }

    // try {
    //  

      
    //   // 2. 基础表单验证
      
    //   // 3. 发起登录请求
    //   const { data } = await axios.post('/api/admin/login', {
    //     username: form.username,
    //     password: form.password
    //   })

    //   // 4. 处理登录成功
    //   localStorage.setItem('token', data.token)
    //   console.log('登陆成功')
    //   // router.push('/dashboard')
      
    // } catch (error) {
    //   // 5. 错误处理
    //   errorMsg.value = error.response?.data?.message || error.message
    //   console.error('登录失败:', error)
    // } finally {
    //   // 6. 重置加载状态
    //   loading.value = false
    // }
   
  }

</script>

<style scoped>

/* 登录页面容器 */
.login-page {
  /* 尺寸设置 */
  width: 100vw;
  height: 100vh;
  min-width: 100vw;
  min-height: 100vh;
  
  /* 背景设置 */
  background-image: url('your-background-image.jpg'); /* 替换为您的图片路径 */
  background-size: cover; /* 确保图片覆盖整个容器 */
  background-position: center;
  background-repeat: no-repeat; /* 防止图片重复 */
  background-attachment: fixed; /* 可选：固定背景 */
  
  /* 布局设置 */
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  box-sizing: border-box; /* 包含padding和border在内计算尺寸 */
  
  /* 防止内容溢出 */
  overflow: hidden;
}


/* 登录容器样式 */
.login-container {
  display: flex; /* Flex布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  width: 100%; /* 全宽 */
  height: 100%; /* 全高 */
  transition: transform 0.1s ease-out; /* 平滑过渡效果 */
}

/* 登录卡片样式 */
.login-card {
  background: rgba(255, 255, 255, 0.521); /* 半透明背景 */
  backdrop-filter: blur(10px); /* 毛玻璃效果 */
  padding: 2rem 3rem; /* 内边距 */
  border-radius: 15px; /* 圆角 */
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2); /* 阴影 */
  border: 1px solid rgba(255, 255, 255, 0.1); /* 边框 */
  width: 400px; /* 固定宽度 */
  transition: all 0.3s ease; /* 过渡动画 */
}

/* 卡片悬停效果 */
.login-card:hover {
  transform: translateY(-5px); /* 上移效果 */
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25); /* 增强阴影 */
}

/* 标题样式 */
.login-card h2 {
  color: white; /* 白色文字 */
  text-align: center; /* 居中 */
  margin-bottom: 2rem; /* 底部间距 */
  font-size: 1.8rem; /* 字体大小 */
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 文字阴影 */
}

/* 表单组样式 */
.form-group {
  margin-bottom: 1.5rem; /* 底部间距 */
}

/* 标签样式 */
.form-group label {
  display: block; /* 块级元素 */
  color: white; /* 白色文字 */
  margin-bottom: 0.5rem; /* 底部间距 */
  font-size: 0.9rem; /* 字体大小 */
}

/* 输入框样式 */
.form-group input {
  width: 100%; /* 全宽 */
  padding: 0.8rem 1rem; /* 内边距 */
  border: none; /* 无边框 */
  border-radius: 8px; /* 圆角 */
  background: rgba(255, 255, 255, 0.2); /* 半透明背景 */
  color: white; /* 白色文字 */
  font-size: 1rem; /* 字体大小 */
  transition: all 0.3s; /* 过渡动画 */
}

/* 输入框聚焦效果 */
.form-group input:focus {
  outline: none; /* 移除默认轮廓 */
  background: rgba(255, 255, 255, 0.3); /* 更亮的背景 */
  box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.2); /* 发光效果 */
}

/* 登录按钮样式 */
.login-btn {
  width: 100%; /* 全宽 */
  padding: 0.8rem; /* 内边距 */
  background: linear-gradient(45deg, #4e54c8, #8f94fb); /* 渐变背景 */
  color: white; /* 白色文字 */
  border: none; /* 无边框 */
  border-radius: 8px; /* 圆角 */
  font-size: 1rem; /* 字体大小 */
  cursor: pointer; /* 手型光标 */
  transition: all 0.3s; /* 过渡动画 */
  margin-top: 1rem; /* 顶部间距 */
}

/* 按钮悬停效果 */
.login-btn:hover {
  transform: translateY(-2px); /* 上移效果 */
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* 阴影效果 */
}
</style>
