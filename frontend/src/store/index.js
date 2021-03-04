import Vue from 'vue'
import Vuex from 'vuex'

import common from './modules/common'
import search from './modules/search'
import beer from './modules/beer'
import review from './modules/review'
  
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    common,
    search,
    beer,
    review
  }
})
