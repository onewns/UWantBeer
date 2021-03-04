<template>
  <div class="beer-detail-wrap">
    <div class="beer-name-box">
      <div class="beer-name">{{ item.name }}</div>
        <div></div>
    </div>

    <div
      class="beer-content-box">
      <!-- beer img -->
      <div class="beer-img" :style="{'background-image': `url(${imgUrl})`}">
      </div>
      <!-- beer info -->
      <div class="beer-info">
        <div class="info-title flex-between">
          <div>맥주 정보</div>
          <!-- <div v-if="isAuthed" class="video-call-btn">채팅 입장하기</div> -->
        </div>
        <p>제조업체</p>
        <p>{{ item.brew_name }}</p>
        <p>스타일</p>
        <p>{{ item.style }}</p>
        <p>국가 {{ item.country }}</p>
        <p>도수 {{ item.abv }}%</p>
      </div>
    </div>

    <!-- review -->
    <div class="review-wrap">
      <div class="flex-between" style="margin-bottom: 15px;">

        <!-- title: review list -->
        <div v-if="!isReviewCreate" class="info-title">
          <div>
            평점 {{ avgRate || 0 }}
            <span style="margin-left: 10px;">
              {{ beerReviewArray.length }}개의 리뷰가 있습니다.
            </span>
          </div>        
          
          <!-- <div v-else class="info-title">
            <span style="margin-left: 10px;">
              리뷰가 없어 평점을 제공할 수 없습니다.
            </span>
          </div> -->
        </div>

        <!-- title: review create -->
        <div v-if="isReviewCreate" class="info-title">리뷰 작성</div>

        <!-- toggle button -->
        <div 
          v-if="isAuthed"
          @click="toggleReview"
          class="base-btn">
          <span v-if="isReviewCreate">
            <i class="fas fa-list"></i> 리뷰 목록
          </span>
          <span v-else>
            <i class="fas fa-pen"></i> 리뷰 작성
          </span>
        </div>
      </div>

      <!-- review create -->
      <beer-review-create
        @toggle-review="toggleReview"
        v-if="isReviewCreate"
        :itemId="item.id">
      </beer-review-create>

      <!-- review list -->
      <div v-if="!isReviewCreate" class="review-list-wrap">
        <!-- if review -->
        <div v-if="beerReviewArray.length">
          <div v-for="review in beerReviewArray" :key="review.id" style="overflow: hidden">
            <beer-review-item :review="review"></beer-review-item>
          </div>
        </div>
        <!-- else -->
        <div v-else class="no-review-wrap">
          작성된 리뷰가 없습니다. <br>
          첫 리뷰 작성자가 되어주세요!
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import BeerReviewCreate from '@/components/beer/BeerReviewCreate'
import BeerReviewItem from '@/components/beer/BeerReviewItem'

export default {
  name: 'BeerListItemDetail',

  components: {
    'beer-review-create': BeerReviewCreate,
    'beer-review-item': BeerReviewItem,
  },

  data() {
    return {
      reviewContent: null,
      isReviewCreate: false,
      avgRate: 0
    }
  },

  computed: {
    item() {
      this.calavgRate()
      return this.$store.state.beer.beerItem
    },
    beerReviewArray() {
      return this.$store.state.beer.beerReviewArray
    },
    isAuthed() {
      return this.$store.getters['common/isAuthed']
    },
    imgUrl() {
      return this.item.image_url || this.getRandomBeerImg()
    }

  },

  methods: {
    calavgRate() {
      let sum = 0
      this.$store.state.beer.beerReviewArray.forEach((e) => { sum += e.rate})
      this.avgRate = sum / this.$store.state.beer.beerReviewArray.length
    },
    toggleReview() {
      this.isReviewCreate = !this.isReviewCreate
    },
    getRandomBeerImg() {
      let randomNumber = Math.floor(Math.random() * 5 + 1)
      return require(`../../assets/img/beer${randomNumber}.svg`)
    },
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.beer {
  &-name {
    margin-bottom: 10px;
    font-size: 1.8rem;
    font-weight: bolder;

    &-box {
      margin: 10px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;

      border-bottom: 1px solid black;
      border-image-source: $gradient-green;
      border-image-slice: 60 30;
    }
  }

  &-info {
    width: 23vw;
    padding: 5px;
    text-align: left;
    background-color: white;
    border-radius: 5px;

    .info-attr {
      font-weight: bold;
    }
  }

  &-img {
    @extend .flex-center;
    width: 23vw;
    margin-right: 30px;
    height: 280px;
    background-color: #fefefe;
    background-position: 50% 50%;
    background-size: cover;
    border: 1px dashed lightgrey;
    overflow: hidden;
  }
}

.info-title {
  margin: 10px 0;
  text-align: left;
  font-size: 1.3rem;
  font-weight: bold;

  span {
    color: grey;
    font-size: 0.8rem;
    font-weight: light;
  }
}

.beer-content-box {
  display: flex;
  background: white;
}

.review {
  &-wrap {
    margin-top: 30px;
  }

  &-title {
    padding: 10px;
  }

  &-input-wrap {
    display: flex;
    // border-top: 1px solid lightgray;
    // border-bottom: 1px solid lightgray;
  }

  &-input {
    width: 75vw;
    height: 60px;
    transition: 200ms;
    border: none;
    padding: 10px 15px;
    
    &:focus {
      outline: none;
    }
  }

  &-submit-btn {
    @extend .flex-center;
    
    width: 65px;
    height: 30px;
    border-radius: 15px;
    background-color: #333333;
    color: white;
    font-size: 0.8rem;

    &-active {
      background-color: $highlight-color;
    }

    &-wrap {
      @extend .flex-center;
      width: 100px;
    }
  }
}

.video-call-btn {
  @extend .base-btn;
  font-weight: normal;
}


.no-review-wrap {
  padding: 50px;
}

@media screen and (max-width: 768px) {
  .modal-wrap {
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
  }

  .beer-content-box {
    display: inherit;
    div {
      width: auto;
    }
  }

  .beer-img {
    margin: 0;
    height: 300px;
  }
}

</style>