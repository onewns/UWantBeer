# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
yarn serve
// or
npm run serve
```

### Compiles and minifies for production
```
yarn build
// or
npm run build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).



## 프론트 엔드 서버 세팅

> ##### [Ubuntu] nginX 설치 및 설정
>
> 출처: https://m.blog.naver.com/PostView.nhn?blogId=magnking&logNo=221285120060&proxyReferer=https:%2F%2Fwww.google.com%2F
>
> ##### [Vue.js] ubuntu에 nginx 설치하고 vue.js 설치하기
>
> 출처: https://hplayground.tistory.com/105 [Play Ground]

- pem 키를 이용하여 AWS EC2 ubuntu 환경 접속

```bash
ssh -i J3A405T.pem ubuntu@j3a405.p.ssafy.io
#ubuntu@:~/$

```

- npm, nodejs 설치 및 버전 업그레이드

```bash
#n 모듈 설치
sudo npm install -g n
#n 모듈을 사용하여 Nodejs 설치
sudo n latest

#npm 설치
sudo npm install -g npm

```

- ubuntu 환경 내 프로젝트 파일 클론

```bash
#repo 폴더 생성, git clone 후 frontend 폴더로 이동하여 모듈 설치
#ubuntu@:~/repo/s03p23a405/frontend$ 
npm install
#빌드하여 dist 폴더 생성
npm run build

```

- nginx 로 배포

```bash
#nginx 설치
sudo apt-get install nginx
#ubuntu firewall 활성화
sudo ufw enable
#http, ssh 접근 허용
sudo ufw allow 'Nginx HTTP' ssh
#configure 파일 설정
sudo vi /etc/nginx/sites-available/items-rest.conf
	root /home/ubuntu/repo/s03p22a405/frontend/dist #dist 폴더 연결
	location/ {
		try_files $uri $uri/ /index.html #서버 요청 시 실행 파일 index.html로 변경	
	}
#nginx 재시작
sudo service nginx restart   

```



## Conventions

레퍼런스 :  [velog.oi/@cada](https://velog.io/@cada/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%BD%94%EB%94%A9-%EB%B0%8F-%EB%84%A4%EC%9D%B4%EB%B0%8D-%EC%BB%A8%EB%B2%A4%EC%85%98-1%ED%8E%B8)

### Naming

- SFC(Single File Component)의 파일명은 파스칼케이스(PascalCase)를 사용한다.

- 단 한번만 사용하는 SFC는 The를 붙임

- HTML element와의 충돌을 피하기 위해 합성어를 사용한다.

- 줄임말을 사용하지 않는다.

  ``` js
  // bad
  button.vue
  baseButton.vue
  baseBtn.vue
  
  // good
  BaseButton.vue
  TheNavbar.vue
  ```



### Vue

- component / instance의 options 작성 순서는 [공식 문서](https://vuejs.org/v2/style-guide/#Component-instance-options-order-recommended)의 기준에 따른다.

  ``` 
  name
  components
  mixins
  props
  data
  computed
  watch
  lifecycle
  methods
  ```

  

- 각 option 사이에 줄공백을 하나 삽입한다.

- 이외에는 줄공백을 삽입하지 않는다.



- props를 정의할 때 반드시 타입을 명시한다.

  ```js
  // bad
  props: ['status']
  
  // good
  props: {
      status: String,
  }
  ```



- component를 등록하고 template에서 사용할 때, kebab-case를 사용한다.

- component를 import할 때 확장자 .vue는 작성하지 않는다.

  ``` vue
  <template>
  	<div>
          <my-component></my-component>
      </div>
  </template>
  
  <script>
  import MyComponent from '@/components/MyComponent'
      
  export default {
      // ...
      components: {
          'my-component': MyComponent,
      }
  }
  </script>
  ```



- SFC의 style 태그에는 가능한 항상 scoped를 사용한다.

- 기본적으로 글로벌 style로 적용되기 때문에, scoped 없이 작성할 경우 각 컴포넌트에 있는 스타일이 모든 컴포넌트에 적용되어야 하므로 중복된 작업과 성능저하를 가져올 수 있다.

  ``` vue
  <style lang="scss" scoped>
  </style>
  ```

  





### 중괄호

- 모든 제어문에 중괄호를 사용한다.

- if문에서 하나의 구문만 포함할 경우 생략할 수 있다.

- 여는 중괄호 전에는 줄바꿈하지 않는다.

- 여는 중괄호 이후, 닫는 중괄호 이전에 줄바꿈한다.

- 닫는 중괄호 이후에 줄바꿈하되, else, catch, 콤마, 닫는 소괄호가 따라오는 경우 줄바꿈하지 않는다.

  ``` js
  for ( let case in someArray ) {
      if (someCondition) {
   	   doSomething()
  	} else {
      	doSomethingElse()
  	}
  }
  
  if ( someCondition ) doSomthing()
  ```



### 들여쓰기

- 2 spaces를 기본으로 사용한다.
- 새로운 블록{} 이 나타날 때, 배열, 객체에서 들여쓴다.
- 콤마를 사용한 메소드 체인의 경우 각 메소드마다 들여쓴다.



### 세미콜론

- 세미콜론은 사용하지 않는다.



### 공백

줄 공백

- SFC(Single File Component)의 options(name, data, methods 등) 사이에 하나씩 입력한다.





# SCSS(SASS) 사용법

참고자료 :  [Vue CLI 공식문서](https://cli.vuejs.org/guide/css.html#referencing-assets), 

### SASS, SCSS란?

- 대표적인 CSS 전처리기(preprocessor)로서, CSS의 중복적인 문법적 불편함을 해소하고
  변수 선언 및 사용, 간단한 연산 등을 가능하게 함
- 브라우저가 이해할 수 있는 CSS 파일로 컴파일되어(전처리) 동작하게 됨
- SASS와 SCSS의 차이:
  - 기본적으로 기능에는 큰 차이가 없고 문법적 차이가 존재
  - SASS는 파이썬처럼 중괄호 없이 들여쓰기로 범위를 구분
  - SCSS는 CSS와 문법적으로 비슷하므로 작성 및 컴파일에서의 장점이 있음
  - 보통은 SCSS를 추천



### SASS 설치

- -D or --save-dev : package.json의 devDependencies에 추가, 로컬 개발 및 테스트에만 필요
- -S or --save : dependencies에 추가, 프로덕션 환경에 필요
- -g : 글로벌에 설치

``` bash
npm install -D sass-loader sass
```



### SCSS 적용

- SCSS 파일 생성 또는 SFC(.vue 파일) style  옵션 추가
- 스타일 중복 적용을 막기 위해 항상 scoped 옵션 추가

``` vue
<style lang="scss" scoped>    
</style>
```



### 기본적인 SCSS 사용법

참고자료: [heropy.blog](https://heropy.blog/2018/01/31/sass/)



### 내장 함수

참고자료: [공식문서](https://sass-lang.com/documentation/modules)



### 현재 프로젝트에서의 SCSS 활용

- `@/assets/style/base.scss` 파일에 기본적인 변수 선언

- 각 SFC 또는 scss 파일에서 import하여 활용

  ``` scss
  // base.scss
  $font-main: #333333;
  $highlight-color: rgb(34, 96, 231);
  $gradient-main: linear-gradient(to right bottom, #272a31, #1f1f22, #292929);
  $nav-height: 40px;
  ```

  

  ``` vue
  // 다른 컴포넌트
  <style lang="scss" scoped>
  @import '@/assets/style/base'
      
      .some-button {
          ...
          &:hover {
              background-color: $highlight-color:
          }
      }
  </style>
  ```

  







### axios 인터셉터, api

- axios 요청 전, 응답 후 then, catch 처리 전 사용자 설정 가능

```js
//파일 위치 frontend/src/axios.js

import axios from 'axios'

//axios 인스턴스 생성
const instance = axios.create({
    baseURL: 'http://localhost:8000/',
})


/* 요청 인터셉터
2개의 콜백 함수를 받음.
*/
    
instance.interceptors.request.use(
    function (config) {
        /* 요청 성공 직전 호출
         axios 설정값을 넣는다 (사용자 정의 설정도 추가 가능) */
        return config;
    }, 
    function (error) {
        // 요청 에러 직전 호출
        return Promise.reject(error);
    }
);

instance.interceptors.response.use(
    function (response) {
    /*
        http status가 200인 경우
        응답 성공 직전 호출 
        그 후 .then() 으로 이어짐
    */
        return response;
    },

    function (error) {
    /*
        http status가 200이 아닌 경우
        응답 에러 직전 호출
        .catch() 으로 이어짐    
    */
        return Promise.reject(error);
    }
);

export default instance;
```

- axios api

```js
//위치 frontend/src/api/api.js

// 작성한 axios 인터셉터를 가져온다
import axios from '../axios.js'

export default {
    login(data) {
        // axios 요청 생성 함수
        return axios({
            // baseURL설정되어 있기 때문에 그 뒤의 URL만 작성
            url: 'rest-auth/login/',
            method: 'post',
            data: {
                email: data.email,
                password: data.password
            }
        })
    },
    signup(data) {
        return axios({
            url: 'rest-auth/registration/',
            method: 'post',
            data: {
                username: data.username,
                email: data.email,
                password1: data.password1,
                password2: data.password2,
            }
        })
    }
}
```

- component에서 axios 요청 예시

```vue
<script>
import api from '@/api/api.js'

export default {

  methods() {
	handleSubmit() {
        if (this.isFormValid) {
            api.login({email: this.email, password: this.password})
                .then((res) => {
                alert('로그인 성공')
                this.$cookies.set('user_loggedin',res.data.key)
                this.$router.push('/').catch(smoothScrollTo(0)).catch()
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
```



