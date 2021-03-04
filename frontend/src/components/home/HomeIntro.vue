<template>
  <div class="home-intro-section">
  
    <div class="home-line"></div> 

    <div class="home-title">
      U WANT BEER.는 <br> 맥주를 즐기는 사람들을 위한 <br> 커뮤니티입니다.
    </div>

    <div class="home-line"></div> 

    <!-- cards -->
    <div class="home-intro-card-wrap">

      <div v-for="index in 4" :key="index" class="home-intro-card">
        <div
          :style="{'background-image': `url(${cardImageUrl(index)})`}"
          class="home-intro-card-img">
        </div>
        <div v-html="cardText[index]" class="home-intro-card-msg">
        </div>
      </div>

    </div>

    <!-- signup -->
    <div class="signup-wrap">
      <div class="signup-msg">회원가입하고 모든 기능을 사용해보세요!</div>
      <div
        @click="onClickSignup"
        class="signup-btn">
        회원가입
      </div>

      <div class="circle-sm"></div>
      <div class="circle-lg"></div>
      <div class="circle-sm"></div>
      <div class="circle-lg"></div>
      <div class="circle-sm"></div>

      <!-- signup form -->
      <div class="signup-form-wrap">
        <signup-form></signup-form>
      </div>

      <div @click="onClickUp" class="up-btn">
        <i class="fas fa-chevron-up"></i>
      </div>

    </div>
  </div>
</template>

<script>
import SignupForm from '@/components/accounts/SignupForm'
import { smoothScrollTo } from '@/util/common/scroll'

export default {
  name: 'HomeIntro',

  components: {
    SignupForm
  },

  data() {
    return {
      showSignupForm: false,
      cardImage: '../../assets/img/card',
      cardImageLicense: [
        '',
        '<a href="http://www.freepik.com">Designed by pikisuperstar / Freepik</a>',
        '<a href="https://www.freepik.com/vectors/calendar">Calendar vector created by freepik - www.freepik.com</a>',
        '<a href="https://www.freepik.com/vectors/infographic">Infographic vector created by katemangostar - www.freepik.com</a>',
        '<a href="https://www.freepik.com/vectors/business">Business vector created by freepik - www.freepik.com</a>'
      ],
      cardText: [
        '',
        '검색하고 <br class="hide-on-mobile"> 리뷰를 <br> 남겨보세요.',
        '캘린더로 <br class="hide-on-mobile"> 기록을 <br> 관리해보세요.',
        '빅데이터 분석으로 <br> 취향의 맥주를 <br> 추천해드립니다.',
        '다른 사용자들과 <br> 실시간으로 <br> 소통해보세요'
      ],
    }
  },
  methods: {
    cardImageUrl(index) {
      return require(`../../assets/img/card${index}.jpg`)
    },
    onClickSignup(e) {
      const targetY = window.pageYOffset + e.target.getBoundingClientRect().top
      smoothScrollTo(targetY + 300)
    },
    onClickUp() {
      smoothScrollTo(0)
    }
  },

  created() {
    this.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('blend-up')
        }
      })
    })
  },

  mounted() {
    const cards = document.querySelectorAll('.home-intro-card')
    const signupForm = document.querySelector('.signup-form-wrap')
    cards.forEach(card => this.observer.observe(card))
    this.observer.observe(signupForm)
  },

  beforeDestroyed() {
    this.observer.disconnect()
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.home-line {
  width: 50vw; height: 0;
  margin: 50px auto;
  border-bottom: 1px solid $highlight-color;
  border-image-source: $gradient-green;
    border-image-slice: 60 30;
}

.home-title {
  margin: 50px auto;
  font-weight: bolder;
  font-size: 1.5rem;
  line-height: 150%;
}

.home-intro-card {
  @extend .flex-center;
  flex-direction: column;
  width: 210px;
  height: 250px;
  justify-self: center;

  background: white;
  border-radius: 5px;
  border: 1px solid lightgrey;
  box-shadow: 5px 5px 5px lightgrey;
  opacity: 0;

  &-wrap {
    width: 80vw;
    margin: 50px auto;
    display: grid !important;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: auto;
    grid-gap: 20px;
  }

  &-img {
    @extend .flex-center;
    margin: 10px auto;
    width: 190px;
    height: 120px;
    border: 1px dashed lightgrey;
    // background-color: $highlight-color;
    background-image: url('../../assets/img/card1.jpg');
    background-size: cover;
    background-position-y: 40%;
    font-size: 3rem;
  }

  &-msg {
    margin-bottom: 15px;
    font-size: 1.2rem;
    font-weight: 500;
    text-align: left;
    line-height: 150%;
  }
}

.signup {
  &-wrap {
    height: 100vh;
    padding-top: 20px;
    padding-bottom: 150px;
    background-color: #424244;
    // background-image: linear-gradient(to bottom, #333333, #66676b)
  }
  
  &-btn {
    @extend .base-btn;
    margin: 20px auto;
    padding:0;
    width: 300px;
    height: 40px;
    background: $highlight-color;
    color: white;
    // font-size: 1.2rem;
  }
  
  &-msg {
    color: white;
    margin-top: 30px;
  }

  &-form-wrap {
    @extend .flex-center;
    max-width: 500px;
    min-height: 400px;
    margin: 20px auto auto;
    background-color: white;
    opacity: 0;
  }
}

.up-btn {
  @extend .flex-center;
  width: 35px;
  height: 35px;
  border-radius: 100%;
  border: 2px solid white;
  background: #33333396;
  color: white;
  transition: 100ms;
  margin: 50px auto 0 ;

  &:hover {
    cursor: pointer;
    background-color: $highlight-color;
  }
}

.circle {
  border-radius: 100%;
  margin: 20px auto;

  &-lg {
    @extend .circle;
    width: 10px;
    height: 10px;
    background: #999999;
    opacity: 0.7;
  }

  &-sm {
    @extend .circle;
    width: 7px;
    height: 7px;
    background: white;
  }
}

@media screen and (max-width: 1100px) {
  .home-intro-card-wrap {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 768px) {
  .home-intro {
    &-section {
      margin: 0;
    }

    &-card {
      min-width: 0;
      width: 80vw;

      &-msg {
        margin: 0;
      }
    }

    &-card-wrap {
      grid-template-columns: repeat(1, 1fr);
    }
}
}
</style>