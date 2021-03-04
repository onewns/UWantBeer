<template>
  <div>
      <!-- dark area -->
      <div
        @click="onClickWrap"
        id="sidebar-wrap"
        :class="show ? 'sidebar-wrap-show' : ''">
      </div>

      <!-- sidebar -->
      <div :class="[ show ? 'sidebar-show' : '', 'sidebar' ]">
        <div v-show="show">

          <!-- user info -->
          <div
            @click="onClickLink(`/user/${username}`)"
            class="menu-item">
            마이페이지~
          </div>
          
          <!-- menu items -->
          <div
            @click="onClickLink('/')"
            class="menu-item">
            <i class="fas fa-home"></i>
            홈
          </div>
          
          <div
            @click="onClickLink('/search')"
            class="menu-item">
            <i class="fas fa-search"></i>
            검색
          </div>

            <div class="menu-item">
              <i class="fas fa-list"></i>
              게시판
            </div>

            <div class="menu-item">
              <i class="fas fa-question"></i>
              About Us
            </div>

        </div>
      </div>
  </div>
</template>

<script>
import 'vuex'
import { smoothScrollTo } from '@/util/common/scroll'

export default {
  name: 'TheSidebar',

  computed: {
    show() {
      return this.$store.state.common.showSidebar
    },
    username() {
      return this.$cookies.get('username') ? this.$cookies.get('username') : 'temp'
    }
  },

  methods: {
    onClickWrap() {
      this.$store.commit('common/toggleShowSidebar')
    },
    onClickLink(path) {
      this.$router.push(path).catch(smoothScrollTo(0))
      this.$store.commit('common/toggleShowSidebar')
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  width: 0;
  overflow: hidden;
  transition: 350ms;
  background-image: $gradient-main;
  z-index: 7;
}

.sidebar-show {
  width: 250px;
}

.sidebar-wrap-show {
  @include fixed-background;
  z-index: 6;

  background: rgba(0, 0, 0, 0.8);
  transition: ease-in-out 300ms;
}

.sidebar-logo {
  height: 150px;
  color: white;
  border: 1px solid lightblue;
}

.menu-item {
  display: flex;
  align-items: center;
  padding-left: 50px;
  margin: 5px;
  border-radius: 25px;
  height: 50px;
  color: white;
  transition: 200ms;

  &:hover {
    cursor: pointer;
    // color: $highlight-color;
    background-color: $highlight-menu;
    text-shadow: 1px 1px 2px black;
  }

  .fas {
    margin-right: 15px;
  }
}
</style>