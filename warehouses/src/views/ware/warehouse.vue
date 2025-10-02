
<template>
  <div class="app-container">
    <!-- 顶部导航栏 -->
    <header class="header">
      <div class="logo">仓库管理</div>
      <nav class="top-nav">
        <router-link to="/">综合</router-link>
        <router-link to="/dashboard">管理</router-link>
        <router-link to="/settings">设置</router-link>
        <div class="user-profile">
          <span>少爷</span>
          <i class="fas fa-user-circle"></i>
        </div>
      </nav>
    </header>

    <!-- 侧边导航栏和主内容区 -->
    <div class="main-content">
      <!-- 侧边栏 -->
      <aside class="sidebar">
        <nav class="side-nav">
          <router-link to="/dashboard">
            <i class="fas fa-tachometer-alt"></i>
            Dashboard
          </router-link>
          <router-link to="/users">
            <i class="fas fa-users"></i>
            Users
          </router-link>
          <router-link to="/products">
            <i class="fas fa-box-open"></i>
            Products
          </router-link>
          <router-link to="/orders">
            <i class="fas fa-shopping-cart"></i>
            Orders
          </router-link>
          <router-link to="/reports">
            <i class="fas fa-chart-bar"></i>
            Reports
          </router-link>
        </nav>
      </aside>

      <!-- 主内容区 -->
      <main class="content">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
/* 基础样式 */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* 顶部导航栏样式 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  height: 60px;
  background: linear-gradient(135deg, #6e8efb, #a777e3);
  color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.top-nav {
  display: flex;
  gap: 20px;
  align-items: center;
}

.top-nav a {
  color: white;
  text-decoration: none;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.top-nav a:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

/* 主内容区布局 */
.main-content {
  display: flex;
  flex: 1;
}

/* 侧边栏样式 */
.sidebar {
  width: 220px;
  background-color: #2c3e50;
  color: white;
  padding: 20px 0;
}

.side-nav {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.side-nav a {
  color: white;
  text-decoration: none;
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: background-color 0.3s;
}

.side-nav a:hover {
  background-color: #34495e;
}

.side-nav a.router-link-exact-active {
  background-color: #3498db;
}

/* 主内容区样式 */
.content {
  flex: 1;
  padding: 20px;
  background-color: #f5f7fa;
}
</style>
