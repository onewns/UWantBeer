<template>
  <div id="header-img">

      <div class="header-msg">
        U WANT BEER. <br>
        NOW. <br>
        <p class="header-msg-sm">
          지금 원하는 맥주를 검색해보세요!
        </p>
      </div>

      <div class="search-bar-wrap">
        <search-bar></search-bar>
      </div>

    <vue-particles
        color="#ffffff"
        :particleOpacity="0.8"
        :particlesNumber="150"
        shapeType="circle"
        :particleSize="13"
        linesColor="#dedede"
        :linesWidth="1"
        :lineLinked="false"
        :lineOpacity="0"
        :linesDistance="0"
        :moveSpeed="4"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="bubble"
        style="height: 100%; width: 100%;"
      >
      </vue-particles>

      <div @click="onClickDown" class="down-btn">
        <i class="fas fa-chevron-down"></i>
      </div>
  </div>
</template>

<script>
import SearchBar from '@/components/common/SearchBar'
import { smoothScrollTo } from '@/util/common/scroll'

export default {
  components: {
    'search-bar': SearchBar
  },

  methods: {
    onClickDown() {
      smoothScrollTo(window.innerHeight+10)
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

#header-img {
  @extend .flex-center;
  position: relative;
  flex-direction: column;
  height: 100vh;
  background: #333333;
  background-image: $gradient-yellow;
  background-size: cover;
}

.header-msg {
  position: absolute;
  top: 23vh;
  left: 25vw;
  margin-bottom: 20px;
  font-size: 4rem;
  font-weight: bolder;
  text-align: left;
  color: white;
  text-shadow: 3px 3px 5px #333333;

  &-sm {
    font-size: 1.5rem;
    text-shadow: none;
    color: #333333;
  }
}

.search-bar-wrap {
  position: absolute;
  top: 50vh;
}

.down-btn {
  @extend .flex-center;
  position: absolute;
  top: 90vh;
  width: 35px;
  height: 35px;
  border-radius: 100%;
  border: 2px solid white;
  background: #33333396;
  color: white;
  transition: 100ms;

  &:hover {
    cursor: pointer;
    background-color: $highlight-color;
  }
}

@media screen and (max-width: 768px) {
  .header-msg {
    font-size: 2rem;
    left: auto;

    &-sm {
      font-size: 1rem;
    }
  }
}
</style>
