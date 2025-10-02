
<template>
  <el-container class="main-container">
    <!-- style="height: 120px" -->
    <el-header class="animated-header" style="height: 12%">
      <h1 class="title">智能管理系统</h1>
      <div class="tech-line"></div>
      <!-- 新增用户信息栏 -->
      <div class="user-info">
        <el-avatar :size="40" src="https://picsum.photos/200/300?random=1" />
        <span class="username">管理员</span>
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
    </el-header>

    <el-main class="dashboard-main">
      <!-- 新增系统状态卡片 -->
      <div class="status-cards">
        <el-card class="status-card" shadow="hover" @click="refreshPercentage">
          <div class="status-content">
            <el-icon :size="40" color="#00dbde"><cpu /></el-icon>
            <div class="status-text">
              <h3 style="color: white;" >系统开发程度</h3>
              <el-progress 
                :percentage="randomPercentage" 
                :color="customColors"
                class="progress-bar"
              />
              <!-- <el-button  class="refresh-btn">
                随机刷新
              </el-button> -->
            </div>
          </div>
        </el-card>
        
        <el-card class="status-card" shadow="hover">
          <div class="status-content">
            <el-icon :size="40" color="#fc00ff"><data-line /></el-icon>
            <div class="status-text">
              <h3 style="color: white;">今日笔记</h3>
              <p>3项事件</p>
            </div>
          </div>
        </el-card>
        
        <el-card class="status-card" shadow="hover">
          <div class="status-content">
            <el-icon :size="40" color="#ffd04b"><bell /></el-icon>
            <div class="status-text">
              <h3 style="color: white;">待办事项</h3>
              <p>5 项待处理</p>
            </div>
          </div>
        </el-card>
      </div>

      <!-- 原有系统卡片 -->
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

      <!-- 日志更新 -->
      <el-card class="recent-activity" shadow="hover">
        <template #header>
          <div class="activity-header">
            <h3 style="color: white;">更新记录</h3>
            <el-button type="text">查看全部</el-button>
          </div>
        </template>
        <el-timeline>
          <el-timeline-item
            v-for="(activity, index) in activities"
            :key="index"
            :timestamp="activity.time">
            {{ activity.content }}
          </el-timeline-item>
        </el-timeline>
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      randomPercentage: 0,
      customColors: [
        { "color": "#87CEEB", "percentage": 15 },
        { "color": "#5D8AA8", "percentage": 30 },
        { "color": "#4682B4", "percentage": 45 },
        { "color": "#4169E1", "percentage": 60 },
        { "color": "#9370DB", "percentage": 75 },
        { "color": "#DA70D6", "percentage": 90 },
        { "color": "#FF6347", "percentage": 100 }
      ]
    }
  },
  mounted() {
    this.generateRandomPercentage();
  },
  methods: {
    generateRandomPercentage() {
      const percentages = [5, 10, 15, 25, 45, 65, 80, 100];
      const randomIndex = Math.floor(Math.random() * percentages.length);
      this.randomPercentage = percentages[randomIndex];
    },
    refreshPercentage() {
      this.generateRandomPercentage();
    }
  }
}
</script>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  Money,
  Goods,
  Sunny,
  Connection,
  ArrowDown,
  Cpu,
  DataLine,
  Bell
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
  },
  {
    name: '我的工具箱',
    desc: '工具箱应用及三方工具网站',
    path: '/ai',
    icon: Connection
  }
])

const activities = ref([
  {
    content: '用户张三更新了财务数据',
    time: '2025-10-02 14:30'
  },
  {
    content: '系统自动备份完成',
    time: '2025-10-02 12:00'
  },
  {
    content: '新版本1.2.0发布',
    time: '2025-10-01 09:15'
  }
])


const navigateTo = (path) => {
  router.push(path)
}


</script>

<style lang="scss" scoped>
// 完成度
.progress-bar {
  margin: 20px 0;
  width: 80%;
}
.refresh-btn {
  margin-top: 10px;
}
//

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
  position: relative;
  margin-top: -28px; /* 根据需求调整负值 */

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
    height: 3px;
    background: linear-gradient(to right, transparent, #00dbde, transparent);
    box-shadow: 0 0 10px #00dbde;
  }

  .user-info {
    position: absolute;
    right: 30px;
    top: 60%;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;

    .username {
      font-size: 1rem;
    }
  }
}

.dashboard-main {
  display: flex;
  flex-direction: column;
}

.status-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;

  .status-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
    }

    .status-content {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 1.5rem;

      .status-text {
        flex: 1;

        h3 {
          margin: 0 0 0.5rem 0;
          font-size: 1.1rem;
        }

        p {
          margin: 0;
          color: rgba(255, 255, 255, 0.7);
          font-size: 0.9rem;
        }

        :deep(.el-progress) {
          margin-top: 0.5rem;
        }
      }
    }
  }
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


.recent-activity {
  margin-top: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  transform: translateY(0);
  opacity: 0;
  animation: cardEntrance 0.8s forwards;

  &:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
    border-color: rgba(255, 255, 255, 0.3);
  }

  .activity-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
    
    &:hover {
      transform: translateX(5px);
    }
  }

  :deep(.el-timeline) {
    padding-left: 10px;
    transition: transform 0.3s ease;

    .el-timeline-item {
      opacity: 0;
      animation: itemFadeIn 0.6s forwards;
      animation-delay: calc(0.1s * var(--index));
      
      &:hover {
        .el-timeline-item__timestamp {
          color: rgba(255, 255, 255, 0.9);
        }
      }
    }

    .el-timeline-item__timestamp {
      color: rgba(255, 255, 255, 0.7);
      transition: color 0.3s ease, transform 0.3s ease;
    }
  }
}

@keyframes cardEntrance {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes itemFadeIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
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
