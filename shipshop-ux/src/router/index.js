import { createRouter, createWebHashHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import CategoryView from '../views/CategoryView.vue'
import SearchView from '../views/SearchView.vue'
import CartView from '../views/CartView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import MyAccountView from '../views/MyAccountView.vue'
import CheckoutView from '../views/CheckoutView.vue'
import SuccessView from '../views/SuccessView.vue'

import store from '@/store'

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
    path: '/sign-up',
    name: 'sign-up',
    component: SignUpView,
    //props: route => ({ query: route.query.q })
  },
  {
    path: '/log-in',
    name: 'log-in',
    component: LogInView,
    //props: route => ({ query: route.query.q })
  },
  {
    path: '/my-account',
    name: 'my-account',
    component: MyAccountView,
    meta:{
      requireLogin:true
    }
    //props: route => ({ query: route.query.q })
  },
  {
    path: '/cart/checkout',
    name: 'checkout',
    component: CheckoutView,
    meta:{
      requireLogin:true
    }
    //props: route => ({ query: route.query.q })
  },
  {
    path: '/cart/success',
    name: 'success',
    component: SuccessView,
    meta:{
      requireLogin:true
    }
    //props: route => ({ query: route.query.q })
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView,
    //props: route => ({ query: route.query.q })
  },,
  {
    path: '/cart',
    name: 'cart',
    component: CartView,
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

router.beforeEach((to,from,next)=>{

  if(to.matched.some(record=>record.meta.requireLogin) && !store.state.isAuthenticated){
    next({name:'log-in',query:{to:path}})
  }else{
    next()
  }
})

export default router