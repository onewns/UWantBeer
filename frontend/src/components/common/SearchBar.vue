<template>
<div style="position: relative">
  <div class="search-bar-wrap flex-center">

    <!-- filter button -->
    <i
      @click="onClickFilter"
      class="fas fa-filter search-filter-btn"></i>
    <input
      @keyup.enter="onSubmit"
      v-model="keyword"
      type="text"
      class="search-input"
      autofocus>
    <div
      @click="onSubmit"
      :class="[ keyword ? 'active-icon' : '', 'search-btn flex-center']">
        <i class="fas fa-search"></i>
    </div>
  </div>

  <div v-show="showFilter" class="filter-wrap">

      <!-- style filter -->
      <select v-model="style" class="search-select">
        <option disabled value="All">스타일</option>
        <option
          v-for="option in styleOptions"
          :key="option.id"
          v-text="option.text"
          :value="option.value">
        </option>
      </select>

      <!-- country filter -->
      <select v-model="country" class="search-select">
        <option disabled value="All">국가</option>
        <option
          v-for="option in countryOptions"
          :key="option.id"
          v-text="option.text"
          :value="option.value">
        </option>
      </select>

      <!-- abv filter -->
      <div class="flex-center">
        <div style="margin-right: 20px; font-size: 14px;">도수(%)</div>
        <vue-slider v-model="abv" v-bind="sliderOptions"></vue-slider>
      </div>
    </div>
</div>
</template>

<script>
// modules
import api from '@/api/api'

// libraries
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

export default {
  name: 'searchBar',

  components: {
    'vue-slider': VueSlider
  },

  data() {
    return {
      keyword: null,
      styleOptions: [
        { text: '전체', value: 'All'},
        { text: 'Lager', value: 'Lager'},
        { text: 'Ale', value: 'Ale'},
        { text: '기타', value: 'Etc'},
      ],
      countryOptions: [
        { text: '전체', value: 'All'},
        { text: '국내', value: 'Kr'},
        { text: '기타', value: 'Etc'},
      ],
      sliderOptions: {
        width: '200px',
        max: 30,
      },
      style: 'All',
      country: 'All',
      abv: [0, 30],
      limit: 12,
      showFilter: false,
    }
  },

  methods: {
    async onSubmit() {
        await api.search({keyword: this.keyword, style: this.style, country: this.country, abvmax: this.abv[1], abvmin: this.abv[0], limit: this.limit
        }).then((res) => {
          if (res.status === 200) {
            console.log(res)
            this.$store.dispatch('search/fetchSearchResult', res)
            this.$store.dispatch('search/fetchSearchOrNot', null)
          } else if (res.status === 202) {
            this.$store.dispatch('search/fetchSearchResult', res)
            this.$store.dispatch('search/fetchSearchOrNot', true)
          }
            else {
            alert("찾으시는 맥주가 없습니다")
            this.$store.dispatch('search/fetchSearchResult', res)
          }
        }).catch(() => alert('error'))
        this.$router.push(`/search/${this.keyword}`).catch(() => {})
    },
    onClickFilter() {
      this.showFilter = !this.showFilter
    },
  },
  
  mounted() {
    const keywordSearched = this.$store.state.search.keyword
    this.keyword = keywordSearched ? keywordSearched : null
  },

  created() {
    this.showFilter = this.$route.matched[0].path === "/search"
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.search-bar-wrap {
  border-radius: 25px;
  border: 1px solid lightgrey;
  background-color: white;
}

.search-filter-btn {
  margin-left: 30px;
  
  &:hover {
    @extend .active-icon;
    cursor: pointer;
  }
}

.search-input {
  width: 600px;
  height: 45px;
  margin-left: 30px;
  padding: 0;
  border: none;
  background-color: white;
  font-size: 20px;
  
  &:focus {
    outline: none;
  }
}

.search-btn {
  width: 75px;
  height: 50px;
  padding: 1px 2px;
  border-radius: 0 25px 25px 0;
  background-color: white;

  &:hover {
    @extend .active-icon;
    cursor: pointer;
    color: white;
  }
}

.active-icon {
  animation: active-icon;
  animation-duration: 250ms;
  animation-iteration-count: 2;
  color: $highlight-color;
}

@keyframes active-icon {
  to {font-size: 115%;}
}

// filters
.filter-wrap {
  @extend .flex-center;
  @include blend-in-mixin;
  position: absolute;
  top: 60px;
  padding: 20px 0;
  width: 757px;
  border-radius: 25px;
  border: 1px solid lightgrey;
  background: white;
}

.search-select {
  margin: 0 20px;
  height: 35px;
  width: 100px;
  border: none;
  
  &:focus {
    outline: none;
  }
}

@media screen and (max-width: 768px) {
  .search-bar-wrap {
    width: 100vw;
    border: none;
    border-radius: 0;
  }

  .search-filter-btn {
    margin-left: 15px;
  }

  .search-input {
    height: 40px;
    flex-grow: 2;
    font-size: 18px;
    font-weight: bold;
  }

  .search-btn {
    height: 40px;
    width: 80px;
    border-radius: 0;
  }

  .search-select {
    margin-bottom: 20px;
  }

  .filter-wrap {
    width: 100vw;
    top: 40px;
    border-radius: 0;
    border: none;
    border-bottom: 1px solid lightgrey;
    display: inherit;
  }
}
</style>