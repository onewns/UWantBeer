export default {
  email: /^[a-z0-9_+.-]+@([a-z0-9-]+\.)+[a-z0-9]{2,4}$/,

  username: /^[(a-zA-Z)]+[a-zA-Z0-9_]{4,12}$/g,

  password: /^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,20}$/g,
}