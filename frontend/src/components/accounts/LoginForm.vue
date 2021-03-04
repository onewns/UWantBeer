<template>
    <div>
        <!-- email -->
        <div>
            <input
                v-model="email"
                type="email"
                class="account-input"
                placeholder="이메일"
                autocapitalize="off"
                autofocus
                autocomplete="on">
            
            <!-- email error message -->
            <div
                v-if="email && !isEmailValid"
                class="account-input-err">
                예) example@ssafy.com
            </div>
        </div>

        <!-- password -->
        <div>
            <input
                @keypress.enter="handleSubmit()"
                v-model="password"
                type="password"
                class="account-input"
                placeholder="비밀번호">

            <!-- login error message -->
            <div
                v-if="submitChecker && !isFormValid"
                class="account-input-err" >
                이메일과 비밀번호를 입력해주세요.
            </div>

            <!-- remember-me button -->
            <div class="checkbox-box">
                <div></div>
                <div class="flex-center">
                    <input
                        v-model="rememberMe"
                        type="checkbox" id="remember-btn">
                    <label for="remember-btn" style="font-size: 0.8rem;">아이디 기억하기</label>
                </div>
            </div>
        </div>   

        <!--  submit button  -->
        <div
            @click="handleSubmit()"
            :class="[ isFormValid ? 'active-btn' : '' , 'submit-btn']">
            로그인
        </div>
        <div class="signup-msg">
            아직 회원이 아니신가요?
        </div>
        <div
            @click="onClickLink('/auth/signup')"
            class="signup-btn">
            회원가입
        </div>
    </div>
</template>

<script>
// modules
import api from '@/api/api'
import accountsRegex from '@/util/regex/accountsRegex'
import 'vuex'

export default {
    name: 'LoginView',

    data() {
        return {
            email: localStorage.email ? localStorage.email : null,
            password: null,
            submitChecker: null,
            rememberMe: localStorage.email ? true : false,
        }
    },

    computed: {
        isEmailValid() {
            return accountsRegex.email.test(this.email)
        },
        isFormValid() {
            return (this.isEmailValid && !!this.password)
        }
    },

    methods: {
        onClickLink(path) {
      this.$router.push(path)
        .catch(() => {})
    },
        handleSubmit() {
            if (this.isFormValid) {
                api.login({email: this.email, password: this.password})
                    .then((res) => {
                        // 이메일 기억하기
                        console.log(res)
                        if (this.rememberMe) {
                            localStorage.email = this.email
                        }

                        // 쿠키 설정 및 redirect
                        this.$cookies.set('auth', res.data.key)
                        this.$cookies.set('username', res.data.user.username)
                        this.$cookies.set('user_id', res.data.user.id)
                        this.$store.commit('common/toggleCookie')
                        this.$router.push('/')
                    }).catch(() => {
                        alert('로그인 실패')
                    })
            }else{
                this.submitChecker = true
            }
        },
    }
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/accounts';
</style>