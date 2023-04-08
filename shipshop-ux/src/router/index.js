import { createRouter, createWebHashHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import CategoryView from '../views/CategoryView.vue'
import SearchView from '../views/SearchView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView,
    //props: route => ({ query: route.query.q })
  },
  {
    path:'/:category_slug/:product_slug',
    name:'product',
    component:ProductView
  },
  {
    path:'/:category_slug',
    name:'category',
    component:CategoryView
  },
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router