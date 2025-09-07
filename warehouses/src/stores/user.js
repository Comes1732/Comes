
import { defineStore } from 'pinia'
import { loginAPI } from '@/api/auth'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    userInfo: JSON.parse(localStorage.getItem('userInfo')) || null
  }),
  actions: {
    async login(credentials) {
      const { data } = await loginAPI(credentials)
      this.token = data.token
      this.userInfo = data.user
      localStorage.setItem('token', data.token)
      localStorage.setItem('userInfo', JSON.stringify(data.user))
    },
    logout() {
      this.token = ''
      this.userInfo = null
      localStorage.removeItem('token')
      localStorage.removeItem('userInfo')
    }
  },
  getters: {
    isAuthenticated: (state) => !!state.token
  }
})
