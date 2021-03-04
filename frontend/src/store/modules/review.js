export default {
    namespaced: true,
  
    state: {
      reviewCount: 0,
      reviewArray: []
    },
  
    mutations: {
      setReviewArray(state, array) {
        state.reviewArray = array
      },
    },
  
    actions: {
        fetchReviewArray({commit}, data) {
            commit('setReviewArray', data)
        }
    },
  
    
  }