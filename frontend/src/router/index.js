import { createRouter, createWebHashHistory } from 'vue-router'
import AreaList from "@/views/AreaList.vue";

const routes = [
  {
    path: '/',
    name: 'area-list',
    component: AreaList
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
