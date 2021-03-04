export default {
  namespaced: true,
  
  state: {
    keyword: null,
    style: null,
    country: null,
    abv: [0, 30],
    searchResultArray: [],
    noMoreSearch: null,
  },

  getters: {
    getSearchResultCount(state) {
      return state.searchResultArray.length
    }
  },

  mutations: {
    setOptions(state, {keyword, style, country, abvmax, abvmin}) {
      state.keyword = keyword
      state.style = style
      state.country = country
      state.abv[1] = abvmax
      state.abv[0] = abvmin
    },
    setSearchResultArray(state, resultArray) {
      state.searchResultArray = resultArray
    },
    setMoreResultArray(state, resultArray) {
      // state.searchResultArray = state.searchResultArray.concat(resultArray)
      state.searchResultArray = [...state.searchResultArray, ...resultArray]
    },
    setSearchOrNot(state, TrueFalse) {
      state.noMoreSearch = TrueFalse
    },
    resetSearchState(state) {
      state.keyword = null,
      state.searchResultArray = []
      state.nomoresearch = null
    },
  },

  actions: {
    fetchSearchResult({commit}, response) {
      commit('setOptions', response.config.params)
      commit('setSearchResultArray', response.data)
    },
    fetchMoreResult({commit}, response) {
      commit('setMoreResultArray', response.data)
    },
    fetchSearchOrNot({commit}, Boolean) {
      commit('setSearchOrNot', Boolean)
    }
  }
}