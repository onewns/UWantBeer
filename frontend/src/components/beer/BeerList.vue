<template>
  <div>
    <div v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="limit" infinite-scroll-throttle-delay="1000"	class="beer-list-box">
      <div 
        v-for="(item, index) in searchResultArray" :key="index">
        <beer-list-item :item="item" :beerId="item.id"></beer-list-item>
      </div>
    </div>
  </div>
</template>

<script>
// components
import BeerListItem from './BeerListItem'
import api from '@/api/api'

// let count = 0

export default {
  name: 'BeerList',

  data() {
    return {
      limit: 12,
      busy: false
    }
  },

  components: {
    'beer-list-item': BeerListItem,
  },

  computed: {
    searchResultArray() {
      return this.$store.state.search.searchResultArray
    }
  },

  methods: {
    searchMore() {
       api.search({ keyword: this.$store.state.search.keyword, style: this.$store.state.search.style, country: this.$store.state.search.country, abvmax: this.$store.state.search.abv[1], abvmin: this.$store.state.search.abv[0], limit: this.limit
        }).then((res) => {
          if (res.status === 200) {
            this.$store.dispatch('search/fetchMoreResult', res)
            this.$store.dispatch('search/fetchSearchOrNot', null)
          } else if (res.status == 202) {
            this.$store.dispatch('search/fetchMoreResult', res)
            this.$store.dispatch('search/fetchSearchOrNot', true) 
          }
        }).catch(() => alert('error'))
    },
    loadMore: async function() {
      if (this.$store.state.search.searchResultArray.length&&!this.$store.state.search.noMoreSearch) {
        this.busy = true;
        await setTimeout( () => {
        this.limit += 12
        this.searchMore()
        this.busy = false;
        }, 1000);
      }
    },
    
    created() {
      this.loadMore();
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.beer-list-box {
  @extend .flex-center;
  margin: 0 10vw;
  display: grid !important;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
}

@media screen and (max-width: 960px){
  .beer-list-box {
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 10px;
  }
}

@media screen and (max-width: 768px){
  .beer-list-box {
    margin: 0 10px;
    grid-template-columns: 1fr;
    grid-gap: 10px;
  }
}
</style>