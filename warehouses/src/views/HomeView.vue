
<template>
  <el-container class="main-container">
    <el-header class="animated-header" style="height: 12%">
      <h1 class="title">智能管理系统</h1>
      <div class="tech-line"></div>
    </el-header>
    <el-main class="dashboard-main">
      <div class="grid-container" >
        <el-card 
          v-for="(system, index) in systems" 
          :key="index"
          class="system-card"
          响应式动态效果
          :style="`--delay: ${index * 0.1}s`"   
          @click="navigateTo(system.path)"
          shadow="hover">
          <div class="card-content">
            <div class="icon-wrapper">
              <component :is="system.icon" class="system-icon"></component>
            </div>
            <h3>{{ system.name }}</h3>
            <p>{{ system.desc }}</p>
            <div class="glow-effect"></div>
          </div>
        </el-card>
      </div>
      <!-- 下方补充内容 -->
      <div class="dashboard-footer" style="margin-top: 90px;">
        <div class="stats-card">
          <h3>系统运行状态</h3>
          <p>在线用户:248 人 | 今日访问:1,256 次</p>
        </div>
        <div class="quick-links">
          <h3>快捷操作</h3>
          <el-button type="text" icon="el-icon-setting">系统设置</el-button>
          <el-button type="text" icon="el-icon-question">帮助中心</el-button>
        </div>
      </div>

    </el-main>
  </el-container>
</template>

<script setup>
import { markRaw  } from 'vue'   // shallowRef 不会递归转换内部对象，适合组件引用
import { useRouter } from 'vue-router'
import {
  Money,
  Goods,
  Sunny,
  Connection
} from '@element-plus/icons-vue'

const router = useRouter()

const systems = markRaw([
  {
    name: '财务管理系统',
    desc: '企业资产数据管理与分析',
    path: '/finance',
    icon: Money
  },
  {
    name: '仓库管理系统',
    desc: '库存管理与物流追踪',
    path: '/warehouse',
    icon: Goods
  },
  {
    name: '智能天气系统',
    desc: '实时气象数据分析',
    path: '/weather',
    icon: Sunny
  },
  {
    name: '大模型应用管理',
    desc: 'AI模型部署与监控',
    path: '/ai',
    icon: Connection
  }
])

const navigateTo = (path) => {
  router.push(path)
}
</script>

<style lang="scss" scoped>
/* 全局容器样式：控制整个页面布局 */
.main-container {
  height: 100vh; /* 页面高度占满屏幕 */
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); /* 背景渐变色（深蓝紫渐变） */
  color: white; /* 全局文字颜色 */
}

/* 头部区域样式：页面顶部标题栏 */
.animated-header {
  display: flex;
  flex-direction: column; /* 垂直排列子元素（标题+科技线） */
  align-items: center; /* 子元素水平居中 */
  justify-content: center; /* 子元素垂直居中 */
  background: rgba(0, 0, 0, 0.2); /* 半透明黑色背景 */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1); /* 底部白色边框（透明度10%） */
  animation: fadeInDown 0.8s ease-out; /* 头部入场动画（从上往下淡入） */

  .title {
    font-size: 2.5rem; /* 标题文字大小 */
    background: linear-gradient(to right, #00dbde, #fc00ff); /* 标题文字渐变色（蓝紫渐变） */
    -webkit-background-clip: text; /* 文字背景裁剪（仅文字显示渐变） */
    background-clip: text;
    color: transparent; /* 文字透明，显示渐变背景 */
    margin-bottom: 10px; /* 标题下方间距 */
  }

  .tech-line {
    width: 80%; /* 科技线宽度（占头部80%） */
    height: 2px; /* 科技线高度 */
    background: linear-gradient(to right, transparent, #00dbde, transparent); /* 科技线渐变色（中间亮蓝，两侧透明） */
    box-shadow: 0 0 10px #00dbde; /* 科技线发光效果（蓝色光晕） */
  }
}

/* 主内容区域样式：卡片和补充内容的容器 */
.dashboard-main {
  padding: 2rem; /* 内边距（上下左右2rem） */
}

/* 卡片网格容器：控制4个系统卡片的布局 */
.grid-container {
  display: grid; /* 启用网格布局 */
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* 自适应列数（最小宽度300px，自动换行） */
  gap: 2rem; /* 卡片之间的间距（水平和垂直） */
  padding: 1rem; /* 网格容器内边距 */
}

/* 系统卡片样式：单个卡片的基础样式 */
.system-card {
  background: rgba(255, 255, 255, 0.05); /* 卡片背景（白色透明度5%） */
  border: 1px solid rgba(255, 255, 255, 0.1); /* 卡片边框（白色透明度10%） */
  border-radius: 15px; /* 卡片圆角 */
  backdrop-filter: blur(10px); /* 背景模糊效果（毛玻璃效果） */
  cursor: pointer; /* 鼠标悬停时显示手型指针 */
  transition: all 0.3s ease; /* 所有属性变化动画（0.3秒缓动） */
  transform: translateY(20px); /* 初始位置（向下偏移20px，用于入场动画） */
  opacity: 0; /* 初始透明度0（用于入场动画） */
  animation: fadeInUp 0.5s ease-out forwards; /* 卡片入场动画（从下往上淡入） */
  animation-delay: var(--delay); /* 动画延迟时间（通过CSS变量动态设置，每个卡片依次入场） */
  position: relative; /* 相对定位（用于子元素绝对定位） */
  overflow: hidden; /* 隐藏溢出内容（如发光效果） */

  /* 卡片悬停效果 */
  &:hover {
    transform: translateY(-5px); /* 悬停时向上移动5px */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* 悬停时阴影（黑色透明度30%） */
    background: rgba(255, 255, 255, 0.1); /* 悬停时背景透明度提升至10% */

    .glow-effect {
      opacity: 1; /* 悬停时显示发光效果 */
    }
  }

  .card-content {
    padding: 2rem; /* 卡片内边距 */
    text-align: center; /* 卡片内容居中对齐 */
    position: relative; /* 相对定位（z-index生效） */
    z-index: 2; /* 内容层级高于发光效果（避免被遮挡） */

    h3 {
      font-size: 1.5rem; /* 系统名称文字大小 */
      margin: 1rem 0; /* 上下间距1rem */
      color: white; /* 系统名称文字颜色 */
    }

    p {
      color: rgba(255, 255, 255, 0.7); /* 系统描述文字颜色（白色透明度70%） */
    }
  }

  .icon-wrapper {
    width: 80px; /* 图标容器宽度 */
    height: 80px; /* 图标容器高度 */
    margin: 0 auto; /* 水平居中 */
    display: flex;
    align-items: center; /* 图标垂直居中 */
    justify-content: center; /* 图标水平居中 */
    background: rgba(255, 255, 255, 0.1); /* 图标背景（白色透明度10%） */
    border-radius: 50%; /* 圆形图标容器 */
    border: 1px solid rgba(255, 255, 255, 0.2); /* 图标容器边框（白色透明度20%） */

    .system-icon {
      font-size: 2.5rem; /* 图标大小 */
      color: white; /* 图标颜色 */
    }
  }

  .glow-effect {
    position: absolute; /* 绝对定位（相对于卡片） */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at center, rgba(0, 219, 222, 0.2) 0%, transparent 70%); /* 中心发光效果（淡蓝色，向外透明） */
    opacity: 0; /* 默认隐藏发光效果 */
    transition: opacity 0.3s ease; /* 发光效果显示/隐藏动画 */
  }
}

/* 新增：补充内容区域样式（卡片下方的统计和快捷操作） */
.dashboard-footer {
  display: flex; /* 水平排列子元素（统计卡片+快捷操作） */
  justify-content: space-around; /* 子元素均匀分布（左右留空） */
  margin-top: 30px; /* 与上方卡片的间距 */
  padding: 20px; /* 内边距 */
  background: rgba(255, 255, 255, 0.05); /* 半透明背景（同卡片背景） */
  border-radius: 8px; /* 圆角边框 */
}

/* 统计卡片样式：左侧系统状态区域 */
.stats-card, .quick-links {
  padding: 15px; /* 内边距 */
  min-width: 200px; /* 最小宽度（避免内容过窄） */
}

/* 动画定义：卡片入场动画（从下往上淡入） */
@keyframes fadeInUp {
  from {
    opacity: 0; /* 起始状态：完全透明 */
    transform: translateY(20px); /* 起始位置：向下偏移20px */
  }
  to {
    opacity: 1; /* 结束状态：完全不透明 */
    transform: translateY(0); /* 结束位置：回到正常位置 */
  }
}

/* 动画定义：头部入场动画（从上往下淡入） */
@keyframes fadeInDown {
  from {
    opacity: 0; /* 起始状态：完全透明 */
    transform: translateY(-20px); /* 起始位置：向上偏移20px */
  }
  to {
    opacity: 1; /* 结束状态：完全不透明 */
    transform: translateY(0); /* 结束位置：回到正常位置 */
  }
}
</style>

