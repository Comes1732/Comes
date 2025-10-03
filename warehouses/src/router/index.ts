import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginViews.vue'
import RegisterPage from '@/views/RegisterPage.vue'

const routes = [
  {       
    path: '/',
    name: 'Home',
    component: HomeView,   // 首页
    meta: { requiresAuth: true }   // 需要登录--默认权限
  },{ 
    path: '/Login',
    name: 'Login',
    component: LoginView,  // 登录
    meta: { guestOnly: true }  // 仅未登录可访问
  },{  
    path: '/Regis',
    name: 'Regis',        // 注册
    component: RegisterPage,
    meta: { guestOnly: true }  
  },{
    path: '/index/:toolName',
    name: 'DynamicTool', // 动态路由名称
    component: () => import('@/views/index/index.vue'),
    meta: { requiresAuth: true } // 默认认证要求
  }
]


const router = createRouter({
  history: createWebHistory(),
  routes
})

// 全局前置守卫
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('authToken')
  
  // 需要登录但未认证
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({
      path: '/login',
      query: { redirect: to.fullPath } // 携带原路径
    })
  } 
  // 已登录但访问guestOnly页面
  else if (to.meta.guestOnly && isAuthenticated) {
    next(from.path || '/dashboard') // 返回原页面或默认页
  }
  // 正常放行
  else {
    next()
  }
})

export default router
