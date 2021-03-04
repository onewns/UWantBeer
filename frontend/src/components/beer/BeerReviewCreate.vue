<template>
  <div>
    <!-- 별점 -->
    <div class="star-rating-wrap">
      <i
        v-for="index in 5"
        :key="index"

        @click="onClickStar(index)"
        @mouseover="onMouseoverStar(index)"
        @mouseout="onMouseoutStar"
        :class="[ tempRate >=index ? 'star-active' : '', 'fas fa-star']">
      </i>
    </div>
    
    <!-- 사진 -->
    <!-- <div class="review-pic-input-wrap">
      <div class="review-pic-input review-pic-sm">
        <i class="fas fa-plus"></i>
      </div>
    </div> -->

    <!-- 본문 -->
    <div class="review-input-wrap">
      <textarea v-model="content" class="review-input" cols="30" rows="10"></textarea>
    </div>

    <!-- submit button -->
    <div class="flex-between">
      <div></div>
      <div class="review-submit-btn" @click="onClickReviewCreate">리뷰 등록하기</div>
    </div>


  </div>
</template>

<script>
import api from '@/api/api'
export default {
  name: 'BeerReviewCreate',

  props: {
    itemId: Number,
  }, 

  data() {
    return {
      content: null,
      rate: 1,
      tempRate: 1,
    }
  },

  methods: {
    onMouseoverStar(index) {
      this.tempRate = index
    },
    onMouseoutStar() {
      this.tempRate = this.rate
    },
    onClickStar(index) {
      this.rate = index
    },
    onClickReviewCreate() {
      api.ReviewCreate({rate: this.rate, content: this.content, auth: this.$cookies.get('auth'), beer:this.itemId})
        .then((res)=>{
          this.$store.state.beer.beerReviewArray.push(res.data)
          this.$emit('toggle-review')
        })
        .catch(() => {
          alert('err')
        })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.star-rating-wrap {
  text-align: left;
  color: #f3f3f3;
}

.star-active {
  color: $highlight-color !important;
}

.review-input {
  padding: 10px;
  width: 40vw;
  border: none;
  resize: none;
  font-family: "NanumSquareR";
  line-height: 160%;

  &:focus {
    outline: none;
  }

  &-wrap {
    border: 1px solid lightgrey;
  }
}

.review-pic {
  &-input-wrap {
    padding: 20px 0;
  }
  &-sm {
    width: 30px;
    height: 30px;
    border-radius: 3px;
  }

  &-input {
    @extend .flex-center;
    border: 1px dashed grey;
    background-color: #f3f3f3;
    color: #555555;
    font-size: 0.8rem;
  }
}

.review-submit-btn {
  @extend .base-btn;
  margin: 10px 0;

  &-active {
    background-color: $highlight-color;
  }
}


@media screen and (max-width: 768px) {
  .review-input {
    width: 290px;
  }
}
</style>