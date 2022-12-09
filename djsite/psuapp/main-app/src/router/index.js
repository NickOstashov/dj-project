import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },

    {
      path: '/problem-detail/:id',
      name: 'problem-detail',
      component: () => import(/* webpackChunkName: "about" */ '../views/DetailView.vue')
    },

    {
      path: '/app/',
      name: 'create-app',
      component: () => import(/* webpackChunkName: "about" */ '../views/AppForm.vue')
    },

    {
      path: '/applications/',
      name: 'apps',
      component: () => import(/* webpackChunkName: "about" */ '../views/ApplicationView.vue')
    },
   
   
  ]
  
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  
  export default router