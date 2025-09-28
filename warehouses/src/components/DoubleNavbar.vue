
<template>
  <div class="double-navbar">
    <!-- 第一排主菜单 -->
    <el-menu 
      mode="horizontal" 
      :default-active="activeMainMenu" 
      @select="handleMainMenuSelect"
      class="main-menu"
    >
      <el-menu-item 
        v-for="item in mainMenus" 
        :key="item.path" 
        :index="item.path"
      >
        <template #title>
          <el-icon v-if="item.icon"><component :is="item.icon" /></el-icon>
          <span>{{ item.title }}</span>
        </template>
      </el-menu-item>
    </el-menu>

    <!-- 第二排子菜单标签 -->
    <el-tabs 
      v-model="activeSubMenu" 
      type="card" 
      class="sub-tabs"
      @tab-click="handleTabClick"
    >
      <el-tab-pane 
        v-for="sub in subMenus" 
        :key="sub.path" 
        :label="sub.title" 
        :name="sub.path"
      ></el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  menuData: {
    type: Array,
    required: true,
    default: () => [
      {
        path: '/system',
        title: '系统管理',
        icon: 'Setting',
        children: [
          { path: '/system/user', title: '用户管理' },
          { path: '/system/role', title: '角色管理' }
        ]
      },
      {
        path: '/business',
        title: '业务管理',
        icon: 'DataBoard',
        children: [
          { path: '/business/order', title: '订单管理' },
          { path: '/business/product', title: '产品管理' }
        ]
      }
    ]
  }
})

const router = useRouter()
const activeMainMenu = ref('')
const activeSubMenu = ref('')
const mainMenus = ref([])
const subMenus = ref([])

// 初始化菜单数据
const initMenus = () => {
  mainMenus.value = props.menuData.map(item => ({
    path: item.path,
    title: item.title,
    icon: item.icon
  }))
  
  // 默认激活第一个主菜单的子菜单
  if (props.menuData.length > 0) {
    activeMainMenu.value = props.menuData[0].path
    subMenus.value = props.menuData[0].children || []
    if (subMenus.value.length > 0) {
      activeSubMenu.value = subMenus.value[0].path
    }
  }
}

// 主菜单切换事件
const handleMainMenuSelect = (index) => {
  const selectedMenu = props.menuData.find(item => item.path === index)
  subMenus.value = selectedMenu?.children || []
  if (subMenus.value.length > 0) {
    activeSubMenu.value = subMenus.value[0].path
    router.push(subMenus.value[0].path)
  }
}

// 子标签切换事件
const handleTabClick = (tab) => {
  router.push(tab.props.name)
}

// 监听路由变化同步菜单状态
watch(
  () => router.currentRoute.value.path,
  (newPath) => {
    for (const main of props.menuData) {
      const matchedSub = main.children?.find(sub => sub.path === newPath)
      if (matchedSub) {
        activeMainMenu.value = main.path
        subMenus.value = main.children
        activeSubMenu.value = newPath
        break
      }
    }
  },
  { immediate: true }
)

initMenus()
</script>

<style scoped>
.double-navbar {
  width: 100%;
  background: #fff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.main-menu {
  padding-left: 20px;
}
.sub-tabs {
  padding: 0 20px;
  background: #f5f7fa;
}
:deep(.el-tabs__header) {
  margin: 0;
}
:deep(.el-tabs__item) {
  height: 40px;
  line-height: 40px;
}
</style>
