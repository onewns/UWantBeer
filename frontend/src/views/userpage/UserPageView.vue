<template>
  <div>
    <!-- header -->
    <div class="user-header">
      <!-- user info section -->
      <div class="user-info-wrap">
        <div class="user-info-box">
          <!-- user photo -->
          <div class="user-photo">
            <img src="../../assets/img/base-user-img.svg" alt="">
            <div @click="onClickWIP" class="user-photo-btn">
              <i class="fas fa-camera"></i>
            </div>
          </div>

          <!-- user info -->
          <div class="user-info-content">
            <h2>{{ username }}</h2>
            <div>안녕하세요, 맥주를 좋아하는 {{ username }}입니다.</div>
          </div>

          <!-- setting button -->
            <i
              v-if="isMyPage"
              @click="onClickWIP"
              class="fas fa-cog user-info-btn"></i>
        </div>
      </div>

      <!-- tabs -->
      <div class="user-content-tab-box">
        <div
          v-for="index in tabName.length" :key="index"
          @click="onSelectTab(index)"
          v-text="tabName[index-1]"
          :class="[selectedTab === index ? 
          'user-content-tab-selected' : '',
          'user-content-tab']">
        </div>
      </div>
    </div>

    <!-- content -->
    <div class="user-content-wrap">

      <!-- reviews -->
      <div v-if="selectedTab === 1" class="userpage-content-wrap">
        <user-review-list
        v-if="reviewArray.length"
        :reviewArray='reviewArray'></user-review-list>
        <div v-else>작성한 리뷰가 없습니다.</div>
      </div>
      <!-- wish list -->
      <div v-if="selectedTab === 2" class="userpage-content-r">
        <beer-list></beer-list>
        <div>찜 목록이 비어있습니다.</div>
      </div>
      <!-- calendar -->
      <user-calendar
        v-if="selectedTab === 3" :reviewArray="reviewArray">
      </user-calendar>
    </div>

  </div>
</template>

<script>
// components
import BeerList from '@/components/beer/BeerList'
import UserCalendar from '@/components/userpage/UserCalendar'
import UserReviewList from '@/components/userpage/UserReviewList'

// modules
import api from '@/api/api'

export default {
  name: 'UserPageView',

  components: {
    UserReviewList,
    BeerList,
    UserCalendar
  },

  data() {
    return {
      selectedTab: 1,
      tabName: ['리뷰', '찜 목록', '다이어리'],
      username: '',
      reviewArray: [],
    }
  },

  computed: {
    isMyPage() {
      return this.$cookies.get('username') === this.username
    }
  },

  methods: {
    onSelectTab(index) {
      this.selectedTab = index
    },
    onClickWIP() {
      alert('곧 업데이트될 예정입니다.')
    },
  },

  created() {
    this.username = this.$route.params.username
    
    api.getReviewByAuthor({user_id: this.$cookies.get('user_id')})
      .then((res) => {
        this.reviewArray = res.data
        this.$store.dispatch('review/fetchReviewArray', this.reviewArray)
      })
    // data에 userData 설정

    // getUserReviewArray
    // store에 저장
    // reviewList, calendar에서 사용
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.user-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f2f2f2;
  // background-image: url('../../assets/img/header.jpg');
  background-image: $gradient-green;
  // background-size: 100%;
}

.user-info {
  &-wrap {
    margin: 70px 0 30px;  
  }

  &-box {
    position: relative;
    display: flex;
    align-items: center;
    background-color: white;
    width: 60vw;
    height: 180px;
    border: 1px solid lightgrey;
  }

  &-content {
    text-align: left;
    margin-right: 20px;
  }

  &-btn {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 1.3rem;
    transition: 400ms;
    &:hover {
      color: $highlight-color;
      transform: rotate(180deg);
    }
  }
}

.user-photo {
  @extend .flex-center;
  position: relative;
  margin: 0 50px 0 100px;
  min-width: 100px;
  min-height: 100px;
  border-radius: 100%;
  border: 3px solid $highlight-color;
  background-color: #f2f2f2;

  img {
    width: 80px;
  }
}

.user-photo-btn {
  @extend .flex-center;
  position: absolute;
  top: 73px;
  left: 73px;
  width: 25px;
  height: 25px;
  border-radius: 100%;
  border: 2px solid $font-main;
  background: grey;
  color: white;
  font-size: 12px;

  &:hover {
    cursor: pointer;
    background: $highlight-color;
  }
}

.user-content-wrap {
  @extend .flex-center;
  margin-top: 50px;
  padding: 50px 10vw 100px;
  border-top: 1px solid lightgrey;
  background-color: #f2f2f2;
}

.user-content-tab {
  @extend .flex-center;
  // border: 1px solid lightgrey;
  color: white;

  width: 20vw;
  // min-width: 180px;
  height: 50px;
  font-size: 14px;

  &-box {
    @extend .flex-center;
    background-color: rgba(51, 51, 51, 0.8);
    width: 100vw;
  }

  &-selected {
    background-color: white !important;
    border-top: 3px solid $highlight-color;
    color: $font-main;
  }

  &:hover {
    cursor: pointer;
    background-color: rgba(51, 51, 51, 0.9);
  }
}

.userpage-content-wrap {
  @include blend-in-mixin;
}

@media screen and (max-width: 768px) {
  .user-header {
    background: white;
  }

  .user-info {
    &-wrap {
      margin: 40px 0 0;
      background: white;
    }

    &-box {
      width: 100vw;
      border: none;
    }
  }
  
  .user-photo {
    margin: 20px;
  }

  .user-content-wrap {
    margin: 50px 0 100px;
  }

  .user-content-tab {
    margin: 0;
    flex-grow: 1;
    min-width: auto;
    height: 35px;
    font-size: 12px;

    &-box {
      width: 100vw;
    }
  }
}
</style>
