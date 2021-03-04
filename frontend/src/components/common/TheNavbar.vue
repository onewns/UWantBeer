<template>
  <div
    :class="[show ? '' : 'nav-hide', isHome ? 'nav-transparent' : '']"
    id="nav">
  
    <!-- menu button : mobile -->
      <!-- <i
        v-if="show"
        @click="onClickMenu"
        id="menu-btn"
        class="fas fa-bars show-on-mobile"></i> -->

    <!-- logo -->
    <div
      v-if="show"
      @click="onClickLink('/')"
      class="nav-logo">
      U WANT BEER.
    </div>

    <!-- menu : pc -->
    <div class="hide-on-mobile">
      
    </div>

    <!-- auth buttons : not authed -->
    <div
      v-if="show && !isAuthed"
      @click="onClickLink('/auth/login')"
      class="base-btn">로그인
    </div>


    <!-- user button : authed  -->
    <div
      v-if="show && isAuthed"
      @click="toggleDropdown"
      class="nav-user-icon">
      <span class="nav-user-icon-msg">{{ username }}님, 안녕하세요!</span>
      <i class="fas fa-user-circle"></i>
    
      <!-- user botton dropdown menu -->
      <div
        v-if="showUserDropdown"
        @click="toggleDropdown"
        class="user-dropdown-box">
        <div>
          <div
            @click="onClickLink(`/user/${username}`)"
            class="user-dropdown-item">마이페이지</div>
          <div
            @click="onClickLogout"
            class="user-dropdown-item">로그아웃</div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { hasScrolledDown, smoothScrollTo } from '@/util/common/scroll'
import api from '@/api/api'
import 'vuex'

export default {
  name: 'TheNavBar',

  data() {
    return {
      show: true,
      showUserDropdown: false,
      isCheckingScroll: false,
    }
  },

  computed: {
    isAuthed() {
      return !!this.$cookies.get('auth') | this.$store.state.common.cookie
    },
    isHome() {
      return this.$route.path === "/"
    },
    username() {
      return this.$cookies.get('username') || null
    }
  },

  methods: {
    hideOnScroll() {
      if (!this.isCheckingScroll) {
        this.isCheckingScroll = true
        
        hasScrolledDown()
        .then(res => {
          this.show = !res
          this.isCheckingScroll = false
        })
      }      
    },
    onClickMenu() {
      this.$store.commit('common/toggleShowSidebar')
    },
    onClickLink(path) {
      this.$router.push(path)
        .catch(smoothScrollTo(0))
        .catch(() => {})
    },
    toggleDropdown() {
      this.showUserDropdown = !this.showUserDropdown
    },
    onClickLogout() {
      api.logout()
        .then(() => {
          this.$cookies.remove('auth')
          this.$store.commit('common/toggleCookie')
          this.$router.push('/')
          })
        .catch(() => alert('서버에러'))
    },
  },

  mounted() {
    document.addEventListener('scroll', this.hideOnScroll)
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

#nav {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;

  display: flex;
  justify-content: space-between;
  align-items: center;
  height: $nav-height;
  padding: 0 10vw;

  border-bottom: 1px solid lightgrey;
  background-color: white;
  font-size: 0.8rem;

  transition: ease-out 200ms;
  z-index: 2;

  div:hover {
    cursor: pointer;
  }
}

.nav-hide {
  height: 0 !important;
}

.nav-logo {
  @extend .flex-center;
  width: 150px;
  height: $nav-height - 15;
  font-weight: bolder;
}

.nav-transparent {
  background-color: transparent !important;
  border: none !important;
}

#menu-btn {
  font-size: 1.2rem;
  margin: 0 15px;

  &:hover {
      cursor: pointer;
  }
}

.nav-user-icon {
  @extend .flex-center;
  margin-right: 15px;
  font-size: 1.3rem;

  &-msg {
    @extend .hide-on-mobile;
    margin-right: 10px;
    font-size: 12px;
  }
}

.user-dropdown-box {
  position: absolute;
  top: $nav-height;
  background-color: $font-main;
  color: white;
  
  .user-dropdown-item {
    @extend .flex-center;
    width: 150px;
    height: 60px;
    font-size: 12px;

    &:hover {
      background-color: $highlight-menu;
    }
  }
}

.base-btn {
  margin-right: 15px;
}

@media screen and (max-width: 768px) {
  #nav {
    padding: 0;
  }

  .user-dropdown-box {
    right: 0;
  }
}
</style>
