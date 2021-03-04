<template>
<div>
  <div v-if="this.review" class="review-box">
    
    <div v-if="review.beer_name" class="review-beer-name">
      {{ review.beer_name }}
      <div
        @click="onClickDetail"
        class="review-beer-name-detail">자세히 보기
      </div>
    </div>

    <!-- username & rate -->
    <div class="review-username-box">
      <!-- username  -->
      <div>
        <span v-if="!review.beer_name" class="review-username">
          {{ review.author_name }}
        </span>
        <!-- rate -->
        <span style="font-size: 10px">
          <i
            v-for="index in 5"
            :key="index"
            :class="[ review.rate >= index ? 'star-active' : '', 'fas fa-star']">
          </i>
        </span>
      </div>

      <!-- date -->
      <div class="review-date">
        {{ review.created_date }}
      </div>
    </div>

    <!-- content -->
    <div class="review-content">
      {{ review.content }}
    </div>

  </div>
</div>
</template>

<script>
import api from '@/api/api'
export default {
  name: 'BeerReviewItem',

  props: {
    review: Object,
  },

  computed: {
    isUserPage() {
      return !!this.beerName || false
    }
  },

  methods: {
    onClickDetail() {
      // alert('현재 지원하지 않는 기능입니다.')
      api.getSingleBeer(this.review.beer)
        .then((res) => {
          console.log(res)
          this.$store.commit('beer/setBeerItem', res.data)
        })
      this.$store.state.beer.beerReviewArray = []
      this.fetchReview()
      this.$store.commit('common/toggleShowModal')
    },
    fetchReview() {
      api.getReviewByBeer({ beer: this.review.beer})
        .then((res) => {
          this.$store.state.beer.beerReviewArray = res.data
        })
        .catch(()=> alert('err'))
    },
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.review {
  &-box {
    width: 40vw;
    margin: 5px auto;
    border: 1px solid lightgrey;
    border-radius: 5px;
    background-color: white;
  }

  &-beer-name {
    margin: 10px;
    font-weight: bolder;
    text-align: left;

    &-detail {
      // margin: 10px 0;
      font-weight: normal;
      font-size: 12px;
      color: grey;

      &:hover {
        cursor: pointer;
        color: $highlight-color;
      }
    }
  }

  &-username-box {
    @extend .flex-between;
    margin: 10px;
    border-bottom: 1px solid lightgrey;
  }

  &-username {
    font-weight: bolder;
  }

  &-content {
    min-height: 40px;
    // padding: 10px;
    margin: 10px;
    text-align: left;
  }

  &-date {
    font-size: 10px;
  }
}
//별점 색깔
.star-active {
  color: $highlight-color !important;
}

@media screen and (max-width: 768px) {
  .review-box {
    width: 90vw;
  }
}

</style>