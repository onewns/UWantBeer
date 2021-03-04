<template>
    <div>
        <!-- username -->
        <div>
            <input
                v-model="username"
                type="text" 
                placeholder="아이디"
                class="account-input">

            <!-- username helper -->
            <div
                v-if="username && !isUsernameValid"
                class="account-input-err">
                영문으로 시작 / 숫자, _ 포함 4-12글자
            </div>
        </div>

        <!-- email -->
        <div>
            <input
                v-model="email"
                type="email"
                placeholder="이메일"
                class="account-input"
                autocapitalize="off"
                autofocus>

            <!-- email helper -->
            <div
                v-if="email && !isEmailValid"
                class="account-input-err">
                예) example@ssafy.com
            </div>
        </div>

        <!-- password -->
        <div>
            <input
                v-model="password1"
                type="password"
                placeholder="비밀번호"
                class="account-input">
            
            <!-- password helper -->
            <div
                v-if="password1 && !isPasswordValid"
                class="account-input-err">
                숫자, 특수문자 포함 8-20글자
            </div>
        </div>
        
        <!-- password comfirmation -->
        <div>
            <input
                v-model="password2"
                type="password"
                class="account-input"
                placeholder="비밀번호 확인">

            <!-- password comfirmation helper -->
            <div
                v-if="password1 && password2 && !isPasswordSame"
                class="account-input-err">
                비밀번호가 일치하지 않습니다.
            </div>
        </div>

        <!-- submit bottom -->
        <div
            @click="handleSubmit()"
            :class="[isFormValid ? 'active-btn' : '', 'submit-btn']">
            가입하기
        </div>
    </div>
</template>

<script>
// modules
import api from '@/api/api'
import accountsRegex from '@/util/regex/accountsRegex'
import 'vuex'

export default {
    name: 'SignupView',

    data() {
        return {
            pageTitle: '회원가입',
            username: null,
            email: null,
            password1: null,
            password2: null,
            submitChecker: null,
        }
    },

    computed: {
        isEmailValid() {
            return accountsRegex.email.test(this.email)
        },
        // 영문 대소문자로 시작 숫자,_ 포함 4-12글자
        isUsernameValid() {
            return /^[(a-zA-Z)]+[a-zA-Z0-9_]{4,12}$/g.test(this.username)
        },
        // 영문자, 숫자, 특수문자 1개 이상, 8-20글자
        isPasswordValid() {
            return accountsRegex.password.test(this.password1);
        },
        isPasswordSame() {
            return this.password1 === this.password2
        },
        isFormValid() {
            return this.username && this.email && this.password1 && this.isPasswordValid && this.isPasswordSame && this.isEmailValid
        }
    },

    methods: {
        handleSubmit() {
            if (this.isFormValid) {
                api.signup({
                       username: this.username,
                       email: this.email,
                       password1: this.password1,
                       password2: this.password2
                    })
                    .then(() => {
                        alert('회원가입에 성공하셨습니다.')
                        this.$router.push('/auth/login').catch(() => {})
                    })
                    .catch(() => {
                        alert('회원가입 실패')
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