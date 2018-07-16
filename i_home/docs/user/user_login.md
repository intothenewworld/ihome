#### 登录接口

#### request请求
    POST /ihome/regist/
    
##### params参数:
    mobile str 电话号码
    password str 密码
    password2 str 确认密码 
    
    
#### response响应
##### 失败响应1
    {
    "code": 1000,
    "msg" : "注册参数错误"
    }
    
##### 失败响应2
    {
    'code': 1001, 
    'msg': '注册手机号不符合规则'
    }
    
##### 失败响应3
    {
    'code': 1002, 
    'msg': '手机号码已注册'
    }
    
##### 失败响应4
    {
    'code': 1003, 
    'msg': '密码两次不一致'
    }
    
##### 失败响应5
    {
    'code': 900, 
    'msg': '数据库访问失败'
    }
  
##### 成功响应
    {
    'code': 200, 
    'msg': '请求成功'
    }