<template>
  <div>
    <the-header></the-header>
    <home-recommend v-if="isAuthed"></home-recommend>
    <home-intro v-else></home-intro>
  </div>
</template>

<script>
import TheHeader from '@/components/home/TheHeader'
import HomeIntro from '@/components/home/HomeIntro'
import HomeRecommend from '@/components/home/HomeRecommend'

export default {
  name: 'Home',

  components: {
    TheHeader,
    HomeIntro,
    HomeRecommend,
  },
  
  computed: {
    isAuthed() {
      return this.$store.getters['common/isAuthed']
    },
    username() {
      return this.$cookies.get('username') || null
    },
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.home-line {
  width: 50vw;
  min-width: 250px;
  height: 0;
  margin: 50px auto;
  border-bottom: 1px solid lightgrey;
}

.home-title {
  margin: 50px auto;
  font-weight: bolder;
  font-size: 1.5rem;
  line-height: 150%;

  &-sub {
    margin-top: 30px;
    font-weight: normal;
    font-size: 1rem;
    color: grey;
    line-height: 130%;
  }
}

.home-section {
  margin: 50px 10vw;
}

</style>
