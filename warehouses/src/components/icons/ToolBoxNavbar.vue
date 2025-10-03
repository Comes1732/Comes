
<template>
    <!-- 导航栏容器 -->
    <el-container class="main-container">

        <!-- 关键属性：垂直居中-->
        <el-header class="animated-header" style=" height: 10%; display: flex; align-items: center;">

        <!-- 新增用户信息栏-确保占满header宽度 -->
        <div class="user-info" style=" display: flex; align-items: center;  justify-content: space-between; width: 100%;">
            <h1 style="margin: 0;">智能管理系统</h1>
            <div class="username" style="display: flex; align-items: center; gap: 10px;" >
                <el-avatar :size="40" src="https://picsum.photos/200/300?random=1" />
                <span >管理员</span>
                <el-dropdown>
                <el-icon :size="20"><arrow-down /></el-icon>
                <template #dropdown>
                    <el-dropdown-menu>
                    <el-dropdown-item>个人中心</el-dropdown-item>
                    <el-dropdown-item>系统设置</el-dropdown-item>
                    <el-dropdown-item divided>退出登录</el-dropdown-item>
                    </el-dropdown-menu>
                </template>
                </el-dropdown>
            </div>
        </div>

        </el-header>
    </el-container>

</template>

<script setup lang="ts">
</script>

<style scoped>
/* 新增动画关键帧定义 */
@keyframes pulseGlow {
  0% { box-shadow: 0 0 5px #00dbde; }
  50% { box-shadow: 0 0 20px #fc00ff; }
  100% { box-shadow: 0 0 5px #00dbde; }
}

@keyframes floatUp {
  0% { transform: translateY(10px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

@keyframes scanLine {
  0% { background-position: -100% 0; }
  100% { background-position: 100% 0; }
}

@keyframes textWave {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.animated-header {
  /* 原有样式保持不变 */
  animation: fadeInDown 0.8s ease-out, pulseGlow 3s infinite; /* 新增呼吸光效 */
  
  .title {
    /* 原有渐变文字样式保持不变 */
    animation: textWave 8s ease infinite; /* 新增文字流光动画 */
    background-size: 200% auto; /* 配合textWave动画 */
  }

  .tech-line {
    /* 原有样式保持不变 */
    position: relative;
    overflow: hidden;
    
    &::after {
      /* 新增扫描线效果 */
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(
        to right,
        transparent,
        rgba(0, 219, 222, 0.8),
        transparent
      );
      animation: scanLine 2.5s linear infinite;
    }
  }

  .user-info {
    display: flex;          /* 启用flex布局 */
    align-items: center;    /* 垂直居中对齐 */
    /* 原有样式保持不变 */
    animation: floatUp 0.6s ease-out both; /* 新增浮动入场效果 */
    animation-delay: 0.5s; /* 延迟触发 */
    
    
  }
}
/* 星空背景容器 */
.main-container {
  position: relative;    /* 建立定位上下文 */
  overflow: hidden;      /* 隐藏溢出内容 */
  
  /* 伪元素创建星空层 */
  &::before {
    content: '';         /* 伪元素必须属性 */
    position: absolute;  /* 绝对定位 */
    width: 300%;         /* 扩大画布范围 */
    height: 300%;
    
    /* 三色星体配置（无序分布） */
    background: 
      /* 青色星群：不同大小和位置的星体 */
      radial-gradient(1.2px 1.2px at 18% 32%, #00dbde, transparent),
      radial-gradient(0.8px 0.8px at 72% 45%, #00dbde, transparent),
      radial-gradient(1px 1px at 35% 68%, #00dbde, transparent),
      
      /* 紫色星群：不同大小和位置的星体 */
      radial-gradient(1.5px 1.5px at 82% 18%, #fc00ff, transparent),
      radial-gradient(1.8px 1.8px at 48% 38%, #fc00ff, transparent),
      radial-gradient(1.2px 1.2px at 15% 78%, #fc00ff, transparent),
      
      /* 琥珀色星群（替代纯白）：不同大小和位置的星体 */
      radial-gradient(1px 3px at 65% 25%, #FFD166, transparent),
      radial-gradient(1.1px 1.5px at 28% 55%, #FFD166, transparent),
      radial-gradient(1.3px 1.7px at 88% 62%, #FFD166, transparent);
    
    /* 星体分布控制 */
    background-size: 150px 150px; /* 增大重复单元 */
    
    /* 复合动画效果 */
    animation: 
      starPulse 5s ease-in-out infinite,  /* 呼吸效果 */
      starDrift 40s linear infinite;        /* 无序漂移 */
    opacity: 0.3; /* 初始透明度 */
  }
}

/* 星光呼吸动画 */
@keyframes starPulse {
  0%, 100% {
    /* 元素的透明度 */
    opacity: 0.5;
    filter: blur(3px); 
    /* 缩放系数 */
    transform: scale(1.0); 
  }
  50% {
    opacity: 1.2;
    filter: blur(5px); 
    transform: scale(1.55);
  }
}

/* 无序漂移动画 */
@keyframes starDrift {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: -450px -450px; /* 斜向移动 */
  }
}



@keyframes starPulse {
  0% {
    transform: scale(0.5);
    opacity: 0;
  }
  50% {
    opacity: 0.8; /* 星光最亮时刻 */
  }
  100% {
    transform: scale(2); /* 扩散放大 */
    opacity: 0;
  }
}


@keyframes starField {
  from { transform: translateY(0) translateX(0); }
  to { transform: translateY(-100px) translateX(-100px); }
}

.main-container {
  height: 100vh;
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
  color: white;
}

</style>
