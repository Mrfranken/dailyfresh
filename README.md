# dailyfresh

### 6.24

完成了从注册功能和部分登陆功能：

- 注册页面与其他页面继承与base.html（模板的继承）
- 注册页面模型类的书写，注册时代码的加密
- 在注册时通过ajax请求判断用户是否存在（这一块的js代码不是自己所写）
- 登陆页面输入用户名密码时的提示功能（登陆页面也有一段js逻辑）
  - 当用户名输入不正确时的提示信息（判断方式：在数据库中查询用户名是否存在）
  - 当用户名输入正确密码输入不正确是的提示信息（判断方式：查询数据库）
  - 未做：**用户名密码输入都正确后的页面跳转和用户登录状态的保持**

