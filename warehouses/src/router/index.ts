import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginViews.vue'
import RegisterPage from '@/views/RegisterPage.vue'
import WelcomeItem from '@/components/WelcomeItem.vue'

const routes = [
  {       
    path: '/dashboard',
    name: 'Home',
    component: HomeView,   // 首页
    meta: { requiresAuth: true }  
  },{ 
    path: '/Login',
    name: 'Login',
    component: LoginView,  // 登录
    meta: { requiresAuth: false }  
  },{  
    path: '/Regis',
    name: 'Regis',        // 注册
    component: RegisterPage,
    meta: { requiresAuth: false }  
  },{ 
    path: '/Welcome',
    name: 'Welcome',
    component: WelcomeItem,  // 大屏展示
    meta: { requiresAuth: true }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token')
  
  // 检查路由是否需要认证
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/Login')
  } 
  // 检查路由是否需要游客状态（未登录）
  else if (to.meta.requiresGuest && isAuthenticated) {
    next('/')
  }
  // 其他情况正常放行
  else {
    next()
  }
})

// router.beforeEach((to, from, next) => {
//   const requiresAuth = to.matched.some(record => record.meta.requiresAuth) // 验证是否存在权限
//   const isAuthenticated = !!localStorage.getItem('token') //  验证是否存在token
//   console.log(requiresAuth, isAuthenticated)

//   // isAuthenticated == false or requiresAuth == false
//   if (requiresAuth && isAuthenticated) {
//     next('/')  // 其他情况正常放行
//   }
//   else {
//     console.log('/login')
//     next('/Login')  // 需要认证但未登录
//   }
// })


export default router
