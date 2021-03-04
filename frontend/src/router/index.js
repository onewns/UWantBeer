import Vue from 'vue'
import VueRouter from 'vue-router'

// components
import Home from '@/views/Home'
import AuthView from '@/views/accounts/AuthView'
import SearchView from '@/views/search/SearchView'
import UserPageView from '@/views/userpage/UserPageView'
//김연수 추가
// import Chat from '@/components/facecall/FaceCall'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/auth/:type',
    component: AuthView,
  },
  {
    path: '/search/',
    name: 'Search',
    component: SearchView,
    children: [
      {
        path: ':keyword',
        name: 'SearchResult',
        component: SearchView
      }
    ]
  },
  {
    path: '/user/:username',
    name: 'UserPage',
    component: UserPageView,
  },
  // {
  //   path: '/facechat',
  //   component: Chat
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
