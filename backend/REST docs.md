# REST API Document

[서비스명]을 위한 REST API 문서입니다. 



## User Authentication

유저 인증 관련 API입니다. 로그인, 로그아웃, 회원정보 출력 기능을 제공합니다.



### Login

로그인을 위한 API입니다. 로그인 성공시 성공 메세지와 사용자 토큰을 리턴합니다.

- URL

  `user/login`

- Methods

  `POST`

- Params

  **Required**:

  `email: String`

  `password: String`

- Success Response

  - Status: 200 OK

  - Response

    ```json
    {
    	message:"success",
      auth-token: "sample-access-token"
    }
    ```

- Error Response

  - Status: 401

  - Response

    ```JSON
    {
    	error:"Invalid Email or Password"
    }
    ```



### Logout

로그아웃을 위한 API입니다. 로그아웃 성공시 성공 메세지를 리턴합니다.

- URL

   `user/logout`

- Method 

  `POST`

- Params: None

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
    	message: "Logout succeed"
    }
    ```

- Error Response

  - Status: 401 Unauthorized

  - Response

    ```JSON
    {
    	error: "Not a valid user"
    }
    ```



### Sign Up

회원가입을 위한 REST API입니다. 회원가입 성공시 성공 메세지와 사용자의 이메일, 이름을 리턴합니다.

- URL

  `user/signup`

- Method
  `POST`

- Params

  **Requried**

  `username: String`

  `email: String`

  `password1: String`

  `password2: String` 

  `type: int`

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
    	message: "Signup Succeed",
    	username: "sample username",
      useremail: "sample useremail"
    }
    ```

- Error Response

  - Status: 400 Bad Request

  - Response

    ```JSON
    {
    	message: "비밀번호를 다시 확인해주세요"
    }
    ```



## Review

맥주 리뷰와 관련된 API들을 소개합니다. 



### Post Review

맥주에 대한 리뷰를 작성합니다. 성공적으로 리뷰가 작성되었을 경우 성공 메세지를 리턴합니다.

- URL

  `review/post`

- Method

  `POST`

- Data Params

  **Required**

  `user_id: int`

  `beer_id: int`

  `content: String`

  **Optional**

  `photo: Blob`

- Success Response

  - Status: 200 OK

  - Sample Response

    ```JSON
    {
    	message: 'review posted successfully'
    }
    ```

- Error Response

  - Status: 400 Bad Request or 401 Unauthorized

  - Sample Response

    ```Json
    {
    	error: '내용은 반드시 입력해야합니다.'
    }
    ```

    or

    ```Json
    {
    	error: '로그인되지 않은 유저입니다.'
    }
    ```



### Get a single Review

단일 리뷰 정보를 위한 API입니다. 요청 성공시 요청한 리뷰에 대한 정보를 리턴합니다.

- URL

  `review/:review_id`

- Method

  `GET`

- Params

  **Required**

  `review_id: String `

- Success Response

  - Status: 200 OK

  - Sample Response

    ```JSON
    {
    	id: 1,
      user_id: 'sample user',
      beer_id: 1,
      content: 'lorem ipsum'
    }
    ```

- Error Response

  - Status: 400 Bad Request

  - Sample Response

    ```JSON
    {
    	error: '해당 리뷰가 존재하지 않습니다.'
    }
    ```



### Get All Reviews 

작성된 모든 리뷰를 가져오기 위한 API입니다. 요청 성공시 작성된 모든 리뷰를 리턴합니다.

- URL

  `review/all`

- Method

  `GET`

- Params

  None

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
      {
        id: 1,
        user_id: 'sample user',
        beer_id: 1,
        content: 'lorem ipsum'
    	},
    	{
        id: 2,
      	user_id: 'sample user2',
      	beer_id: 3,
      	content: 'lorem ipsum2'
      }
    }
    ```

- Error Response

  - Status: 400 Bad Request

  - Response

    ```
    
    ```



### Get Review by User

특정 유저가 작성한 리뷰목록을 위한 API입니다. 요청 성공시 요청에 포함된 특정 유저가 작성한 모든 리뷰를 리턴합니다.

- URL 

  `review/user/:user_id`

- Method

  `GET`

- Params

  `user_id: String`

- Success Response

  Status: 200 OK

  Response

  ```JSON
  {
    {
      id: 1,
      user_id: "sample user",
      beer_id: 1,
      content: "lorem ipsum"
  	},
  	{
      id: 2,
    	user_id: "sample user",
    	beer_id: 3,
    	content: "lorem ipsum2"
    }
  }
  ```

- Error Response

  - Status: 400 Bad Request

  - Response

    ```JSON
    {
    	error: "user doesn't exist"
    }
    ```



### Get review by Wine

ㅁ

- URL

  `review/wine/:wine_id`

- Method

  `GET`

- Params:

  **Required**

  `wine_id: int`

- Success Response

  - Status: 200 OK

  - Response

    ```Json
    {
      {
        id: 1,
        user_id: "sample user",
        wine_id: 1,
        content: "lorem ipsum"
    	},
    	{
        id: 5,
      	user_id: "sample user2",
      	wine_id: 1,
      	content: "lorem ipsum2"
      }
    }
    ```

    

- Error Response

  - Status: 400 Bad Request

  - Response

    ```JSON
    {
    	error: "wine doesn't exist"
    }
    ```



### Delete Review

리뷰 삭제를 위한 API입니다. 요청 성공시 요청된 리뷰를 삭제하고 성공 메세지를 리턴합니다.

- URL

  `review/delete/:review_id`

- Method

  `DELETE`

- Params:

  **Required**

  `review_id: int`

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
    	message: "리뷰가 성공적으로 삭제되었습니다."
    }
    ```

- Error Response

  - Status: 400 Bad Request

  - Response

    ```JSON
    {
    	message: "해당하는 리뷰가 존재하지 않습니다."
    }
    ```



### Edit Review

리뷰 수정 요청을 위한 API입니다. 요청 성공시 성공 메세지와 수정된 리뷰의 아이디, 작성자, 와인 아이디, 수정된 리뷰 내용을 리턴합니다.

- URL

  `review/edit/:review_id`

- Method

  `PUT`

- Parameters

  **required**

  `review_id: int`

- Success Response

  Status: 200 OK

  Response

  ```JSON
  {
  	message: "리뷰가 성공적으로 수정되었습니다."
  	review_id: 1,
  	user_id: 2,
  	wine_id: 3,
  	content: "Edited Review Content"
  }
  ```

- Error Response

  - Status: 400 Bad Request or 401 Unauthorized

  - Response

    ```json
    {
    	error: "리뷰 내용은 1글자 이상이어야 합니다."
    }
    ```

    or 

    ```JSON
    {
    	error: "리뷰 수정은 작성자 본인이어야 합니다."
    }
    ```

    or

    ```JSON
    {
    	error: "로그인 되어 있지 않습니다."
    }
    ```

    



## Favourite Beer and User List

사용자가 좋아하는 맥주 목록과 사용자 목록을 생성하기 위한 API들을 소개합니다. 아래의 API들을 사용하여 특정 맥주를 좋아하거나 좋아했던 맥주를 취소할 수 있습니다. 사용자가 좋아하는 전체 맥주 목록도 출력 가능합니다. 사용자가 다른 사용자를 좋아하거나 좋아요를 취소하고 좋아하고 있는 전체 유저 목록도 출력 가능합니다.

### likeWine

특정 맥주에 좋아요를 마킹하기 위한 API입니다. 요청 성공시 성공 메세지와 좋아요를 누른 맥주 정보를 리턴합니다.

- URL

  ```
  like/beer/:beer_id
  ```

- Method

  `POST`

- Params:

  **Required**

  `beer_id: int`

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
    	message: "sample wine을 좋아합니다.",
    	wine_id: 3,
    	wine_name: "sample wine"
    }
    ```

    or

    ```JSON
    {
    	message: "sample wine을 더이상 좋아하지 않습니다"
    }
    ```

    

- Error Response

  - Status: 400 Bad Request or 401 Unauthorized

  - Response

    ```JSON
    {
    	error: "해당 와인이 더 이상 존재하지 않습니다"
    }
    ```

    or

    ```JSON
    {
    	error: "로그인이 필요한 기능입니다."
    }
    ```



### getAllLikeWines

좋아하는 모든 와인의 목록을 위한 API입니다. 요청 성공시 좋아하고 있는 모든 와인의 리스트를 출력합니다.

- URL

  `like/wine/all`

- Method

  `GET`

- Params

  None

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
    	{
    		wine_id:1,
    		wine_name: "first wine"
    	},
    	{
    		wine_id:2,
    		wine_name: "second wine"
    	}
    }
    ```

- Error Response

  - Status: 401 Unauthorized

  - Response

    ```JSON
    {
    	error: "로그인이 필요한 서비스입니다."
    }
    ```

    

### likeUser

특정 유저를 좋아하거나 좋아요를 취소할 수 있는 API입니다. 요청 성공시 성공 메세지와 좋아요를 누른경우 좋아요를 누른 유저의 정보를, 좋아요를 취소했을 경우 취소 성공 메세지를 리턴합니다.

- URL

  `like/user/:user_id`

- Method

  `POST`

- Parameters

  `user_id: int`

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
      message: "user1를 좋아합니다."
      user_id: 1,
      username: "user1"
    }
    ```

- Error Response

  - Status: 400 Bad Request

  - Response

    ```JSON
    {
    	error: "해당 유저가 존재하지 않습니다."
    }
    ```



### getAllLikeUsers

현재 사용자가 좋아하고 있는 모든 사용자를 출력하는 API입니다. 요청 성공시 현재 사용자가 좋아하고 있는 모든 사용자의 `user_id`, `username` 을 리턴합니다.

- URL

  `like/user/all`

- Method

  `GET`

- Params

  None

- Success Response

  - Status: 200 OK

  - Response

    ```JSON
    {
    	{
    		user_id: 1,
    		username: "user1"
    	},
    	{
    		user_id: 2,
    		username: "user2"
    	}
    }
    ```

- Error Response

  - Status: 401 Unauthorized

  - Response

    ```JSON
    {
    	error: "로그인된 사용자만 가능합니다."
    }
    ```



