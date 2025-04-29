import { createRouter, createWebHistory } from 'vue-router'
import AreaListView from "@/views/AreaListView.vue";
import GroupView from "@/views/GroupView.vue";

const routes = [
  {
    path: '/area-list',
    name: 'area-list',
    component: AreaListView
  },
      {
    path: '/group-list',
    name: 'group-list',
    component: GroupView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
