import { fileURLToPath, URL } from 'node:url'
import dns from 'dns'
import { defineConfig } from 'vite'      //重点部分
import vue from '@vitejs/plugin-vue'
dns.setDefaultResultOrder('verbatim')    //重点部分
 
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000/",  // 后端服务器地址 eg:http://172.0.0.1:8080
        changeOrigin: true,     // 修改请求头中的 `Host` 为目标地址
        rewrite: (path) => path.replace(/^\/api/, ''),  // 重写路径（移除 `/api` 前缀）
      }
    }
  }

})