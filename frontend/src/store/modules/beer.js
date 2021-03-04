export default {
  namespaced: true,

  state: {
    beerItem: null,
    beerImg: 0,
    beerReviewArray: [],
  },

  mutations: {
    setBeerItem(state, item) {
      state.beerItem = item
    },
  },

  actions: {},

  
}