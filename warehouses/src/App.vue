<template>
  <div class="app-container">
    <!-- <DoubleNavbar :menu-data="menuList" /> -->
    <div class="main-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import DoubleNavbar from '@/components/DoubleNavbar.vue'

const menuList = [
  {
    path: '/dashboard',
    title: '控制台',
    icon: 'DataLine',
    children: [
      { path: '/dashboard/analysis', title: '分析页' },
      { path: '/dashboard/workbench', title: '工作台' }
    ]
  },
  {
    path: '/system',
    title: '系统管理',
    icon: 'Setting',
    children: [
      { path: '/system/user', title: '用户管理' },
      { path: '/system/role', title: '角色管理' }
    ]
  }
]
</script>
