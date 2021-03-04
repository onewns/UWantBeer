import * as cookies from 'vue-cookies'

export default {
  namespaced: true,
  
  state: {
    cookie: cookies.get('auth') ? true : false,
    showSidebar: false,
    showModalMain: false,
  },

  getters: {
    isAuthed(state) {
      return state.cookie | cookies.get('auth')
    }
  },
  
  mutations: {
    toggleCookie(state) {
      state.cookie = !state.cookie
    },
    toggleShowSidebar(state) {
      state.showSidebar = !state.showSidebar
    },
    toggleShowModal(state) {
      state.showModalMain = !state.showModalMain
    },
  },

  actions: {
  }
}