
<template>
  <el-container class="main-container">
    <el-header class="animated-header">
      <h1 class="title">智能管理系统</h1>
      <div class="tech-line"></div>
    </el-header>
    <el-main class="dashboard-main">
      <div class="grid-container">
        <el-card 
          v-for="(system, index) in systems" 
          :key="index"
          class="system-card"
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
    </el-main>
  </el-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  Money,
  Goods,
  Sunny,
  Connection
} from '@element-plus/icons-vue'

const router = useRouter()

const systems = ref([
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
.main-container {
  height: 100vh;
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
  color: white;
}

.animated-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  animation: fadeInDown 0.8s ease-out;

  .title {
    font-size: 2.5rem;
    background: linear-gradient(to right, #00dbde, #fc00ff);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 10px;
  }

  .tech-line {
    width: 80%;
    height: 2px;
    background: linear-gradient(to right, transparent, #00dbde, transparent);
    box-shadow: 0 0 10px #00dbde;
  }
}

.dashboard-main {
  padding: 2rem;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
}

.system-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: all 0.3s ease;
  transform: translateY(20px);
  opacity: 0;
  animation: fadeInUp 0.5s ease-out forwards;
  animation-delay: var(--delay);
  position: relative;
  overflow: hidden;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
    background: rgba(255, 255, 255, 0.1);

    .glow-effect {
      opacity: 1;
    }
  }

  .card-content {
    padding: 2rem;
    text-align: center;
    position: relative;
    z-index: 2;

    h3 {
      font-size: 1.5rem;
      margin: 1rem 0;
      color: white;
    }

    p {
      color: rgba(255, 255, 255, 0.7);
    }
  }

  .icon-wrapper {
    width: 80px;
    height: 80px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.2);

    .system-icon {
      font-size: 2.5rem;
      color: white;
    }
  }

  .glow-effect {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at center, rgba(0, 219, 222, 0.2) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
