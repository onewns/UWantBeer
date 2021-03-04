import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import cookies from 'vue-cookies'
import VCalendar from 'v-calendar'
import infiniteScroll from 'vue-infinite-scroll'
import CountryFlag from 'vue-country-flag'
import VueParticles from 'vue-particles'
import VueLoading from 'vue-loading-template'

Vue.use(cookies)
Vue.use(VCalendar)
Vue.use(infiniteScroll)
Vue.component('country-flag', CountryFlag)
Vue.use(VueParticles)
Vue.use(VueLoading)

require('@/assets/scss/main.scss')
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
