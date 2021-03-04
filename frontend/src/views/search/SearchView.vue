<template>
  <div style="padding-bottom: 100px;">
    <div class="search-header">
        <search-bar></search-bar>
      <div class="search-filter-box flex-center">
      </div>
    </div>

    <beer-list></beer-list>
  </div>
</template>

<script>
// components
import SearchBar from '@/components/common/SearchBar'
import BeerList from '@/components/beer/BeerList'

export default {
  name: "SearchView",

  components: {
    'search-bar': SearchBar,
    'beer-list': BeerList,
  },

  computed: {
    keyword() {
      return this.$store.state.search.keyword
    },
    searchResultArray() {
      return this.$store.state.search.searchResultArray
    },
    isSearchResult() {
      return !!this.$route.params.keyword
    },
  },

  destroyed() {
    this.$store.commit('search/resetSearchState')
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.search-header {
  @extend .flex-center;
  height: 200px;
  margin: 40px auto;
  background-image: $gradient-green;
  flex-direction: column;
  border-bottom: 1px solid lightgrey;
}

.search-filter-box {
  height: 80px;
}

@media screen and (max-width: 768px) {
  .search-header {
    height: 160px;
    justify-content: start;
  }

  .search-filter-box {
    display: none;
  }
}

</style>