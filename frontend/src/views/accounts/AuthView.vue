<template>
  <div id="auth-wrap" class="flex-center"> 
    <div class="form-wrap">

      <!-- Login Form -->
      <div v-if="isLogin" :class="[ isLogin ? 'form-box-show' : 'form-box-hide', 'form-box']">
        <h2>로그인</h2>
        <login-form v-if="isLogin"></login-form>
      </div>

      <!-- Signup Form -->
      <div v-else :class="[ !isLogin ? 'form-box-show' : 'form-box-hide', 'form-box']">
        <h2>회원가입</h2>
        <signup-form></signup-form>
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from '@/components/accounts/LoginForm'
import SignupForm from '@/components/accounts/SignupForm'

export default {
  name: 'AuthView',

  components: {
    'login-form': LoginForm,
    'signup-form': SignupForm,
  },

  computed: {
    isLogin() {
      return this.$route.params.type==='login'
    }
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/accounts';
</style>