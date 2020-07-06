import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/menu',
    name: 'Menu',
    component: () => import('../views/Menu.vue')
  },
  {
    path: '/orders/waiters',
    name: 'ordenes',
    component: () => import('../views/orders/Waiters.vue')
    //children: [{ path: 'waiters', component: () => import('../views/orders/Waiters.vue') }]
  },
  {
    path: '/orders/delivery',
    name: 'repartidor',
    component: () => import('../views/orders/Delivery.vue')
  },
  {
    path: '/orders/chef',
    name: 'cocinero',
    component: () => import('../views/orders/Chef.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
