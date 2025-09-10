
import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginViews.vue'
import RegisterPage from '@/views/RegisterPage.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginView,
    meta: { requiresAuth: false }  // （未登录用户可访问）
  },{
    path: '/Regis',
    name: 'Regis',
    component: RegisterPage,
    meta: { requiresAuth: false }  // （未登录用户可访问）
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const isAuthenticated = localStorage.getItem('token')
  
  if (requiresAuth && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
