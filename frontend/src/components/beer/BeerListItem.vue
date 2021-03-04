<template>
  <div class="beer-list-item-wrap">
    <!-- beer image -->
    <div 
      @click="onClickBeerItem"
      class="beer-img-wrap"
      :style="{'background-image': `url(${imgUrl})`}">
      <div class="beer-flag">
        <country-flag :country='item.country.toLowerCase()' size="normal"/>
      </div>
        
    </div>

    <!-- beer info -->
    <div class="beer-info-box">
      <div class="beer-info-name">
        <span>{{ beerName }}</span>
      </div>
      <div style="font-size: 13px;">
        <div class="beer-info-title">제조업체</div>
        <div v-text="item.brew_name || '정보없음'"></div>
        <div class="beer-info-title">스타일</div>
        <div>{{ item.style }}</div>
        <div class="beer-info-title">도수</div>
        <div>{{ item.abv }}%</div>
      </div>
    </div>
  </div>
</template>

<script>
// modules
import api from '@/api/api'
import CountryFlag from 'vue-country-flag'

// components
export default {
  name: 'BeerListItem',

  component: {
    CountryFlag
  },

  props: {
    item: Object,
    beerId: Number,
  },

  computed: {
    beerName() {
      return this.item.name_kr !== 'none' ? this.item.name_kr : this.item.name
    },
    imgUrl() {
      return this.item.image_url || this.getRandomBeerImg()
    }
  },
  
  methods: {
    getRandomBeerImg() {
      let randomNumber = Math.floor(Math.random() * 5 + 1)
      return `../../assets/img/beer${randomNumber}.svg`
    },
    fetchReview() {
      api.getReviewByBeer({ beer: this.beerId})
        .then((res) => {
          this.$store.state.beer.beerReviewArray = res.data
        })
        .catch(()=> alert('err'))
    },
    onClickBeerItem() {
      this.$store.commit('beer/setBeerItem', this.item)
      this.$store.state.beer.beerReviewArray = []
      this.fetchReview()
      this.$store.commit('common/toggleShowModal')
    },
  },
}
</script>

<style lang="scss" scoped>
@use "sass:math";
@import '@/assets/style/base';

.beer-list-item-wrap {
  @extend .flex-center;
  border: 1px solid lightgrey;

  &:hover {
    cursor: pointer;
    box-shadow: 5px 5px 10px grey;
  }
}

.beer-img {
  position: relative;
  // top: -200px;
  left: 10px;
  z-index: 1;

  &-wrap {
    @extend .flex-center;
    position: relative;
    min-width: 150px;
    height: 220px;
    background-image: $gradient-main;
    background-size: cover;
    background-position: 50% 50%;
    overflow: hidden;
    
    img {
      max-width: 150px;
      max-height: 100%;
      width: auto;
      height: auto;
      z-index: 1;
    }
  }
}

.flag {
  position: absolute;
  top: -10px;
  left: -15px;
  // border: 1px solid #333333;
  box-shadow: -1px 2px 5px grey;
}

.beer-info {
  &-box {
    flex-grow: 2;
    padding: 5px 15px;
    height: 200px;
    text-align: left;

  }
  &-name {
    color: black !important;
    font-size: 1rem;
    font-weight: bolder;
  }

  &-title {
    margin: 10px auto 5px;
    font-weight: bold;
  }
}

.review-input {
  width: 300px;
  height: 150px;
}

@media screen and (max-width: 768px) {
  .beer-list-item-wrap {
      margin: auto;
  }
}

</style>