'''
day2
日期：2026/1/15
第题
题目：
'''
from uuid import main

#from distutils.command.install import main_key

#from http.client import responses

#get请求
import requests  # 导入库
import uvicorn
# response = requests.get("https://www.baidu.com") #发送Get请求获取网址
# print(response.status_code) # 打印状态码,200表示成功
# print(response.text) #打印获取到的网页内容

#使用request库去除并打印网址内所有用户姓名
# name = requests.get("https://jsonplaceholder.typicode.com/users")
# print(name.json())
# for i in name.json():
#     print(i['name'])

#用request库向网址内提交一条新的帖子，并打印出服务器返回新id
# data = {
#     'title': '这位是我的新帖子',
#     'body': '这是内容',
#     "userId": 1
# }
# response = requests.post("https://jsonplaceholder.typicode.com/posts",data= data)
# print(f"新帖子id为：",response.json()['id'])

#发送post请求
# import requests  # 导入库
# data = {'username':'admin','password':'112233'}
# response = requests.post("https://httpbin.org/post",data=data)
# print(response.text)
#


#import requests
#
# # 1213-根据城市查询天气 - 代码参考（根据实际业务情况修改）
#
# # 基本参数配置
# apiUrl = 'http://apis.juhe.cn/simpleWeather/query'  # 接口请求URL
# apiKey = '11de60ad8a5ecb6efe7b2d70cafae3f0'  # 在个人中心->我的数据,接口名称上方查看
#
# # 接口请求入参配置
# requestParams = {
#     'key': apiKey,
#     'city': '郑州',
# }
#
# # 发起接口网络请求
# response = requests.get(apiUrl, params=requestParams)
#
# # 解析响应结果
# if response.status_code == 200:
#     responseResult = response.json()
#     # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
#     print(responseResult)
# else:
#     # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
#     print('请求异常')


# import requests
# # 准备要提交的帖子数据 → 字典格式
# post_data = {
#     "title": "我的第一篇Python帖子",  # 帖子标题
#     "body": "我用Python的POST请求发帖子啦！",  # 帖子内容
#     "userId": 1  # 发布用户的ID
# }
# response = requests.post("https://jsonplaceholder.typicode.com/posts", data=post_data)
# print("提交的帖子反馈：")
# print(response.json())
# print("新帖子的ID是：", response.json()["id"])


#创建第一个Flask Api（get）
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return "hello sss"
# if __name__ == '__main__':
#     app.run(debug=True)

#创建第二个Api（post）
# from flask import Flask,request,jsonify
# app = Flask(__name__)
# @app.route('/register',methods=['POST'])
# def register_user():
#     try:
#         data = request.get_json()
#         user_name = data.get('username')
#         email = data.get('email')
#         return jsonify({
#             'code' : 200,
#             'username':f'用户{user_name}注册成功',
#             'user_info':{
#                 'name':user_name,
#                 'email':email
#             }
#         })
#     except Exception as e:
#         return jsonify({
#             'code': 500,
#             'error': '服务器处理请求失败',
#             'detial': str(e)
#         }),500
# if __name__ == '__main__':
#     app.run(debug=True)

#Api实战用户管理
from flask import Flask, request, jsonify

# 1. 初始化Flask应用
app = Flask(__name__)

# 2. 模拟数据库（实际项目用MySQL/SQLite，这里用列表存数据）
# 数据格式：每个用户是一个字典，包含id、name、email
users = [
    {"id": 1, "name": "Alice", "email": "alice@test.com"},
    {"id": 2, "name": "Bob", "email": "bob@test.com"}
]


# ------------------- 接口1：获取所有用户（GET /users） -------------------
@app.route('/users', methods=['GET'])
def get_all_users():
    """返回所有用户的列表"""
    # 直接把模拟数据库的users列表转成JSON返回
    return jsonify({
        "code": 200,
        "message": "获取所有用户成功",
        "data": users
    })


# ------------------- 接口2：获取单个用户（GET /users/<int:user_id>） -------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    """根据ID查询单个用户"""
    # 遍历模拟数据库，找到id匹配的用户
    for user in users:
        if user["id"] == user_id:
            return jsonify({
                "code": 200,
                "message": "获取用户成功",
                "data": user
            })
    # 如果遍历完没找到，返回“用户不存在”
    return jsonify({
        "code": 404,
        "message": f"用户ID {user_id} 不存在"
    }), 404  # 404是HTTP状态码，表示“资源不存在”


# ------------------- 接口3：创建用户（POST /users） -------------------
@app.route('/users', methods=['POST'])
def create_user():
    """添加新用户"""
    # 1. 接收前端传的JSON数据（包含name和email）
    new_user_data = request.get_json()
    # 2. 校验必填字段（name和email不能为空）
    if not new_user_data.get("name") or not new_user_data.get("email"):
        return jsonify({
            "code": 400,
            "message": "姓名和邮箱不能为空"
        }), 400  # 400表示“请求参数错误”

    # 3. 生成新用户的ID（取当前最大ID+1）
    new_user_id = max(user["id"] for user in users) + 1 if users else 1
    # 4. 构造新用户字典
    new_user = {
        "id": new_user_id,
        "name": new_user_data["name"],
        "email": new_user_data["email"]
    }
    # 5. 把新用户加入模拟数据库
    users.append(new_user)
    # 6. 返回成功响应
    return jsonify({
        "code": 201,  # 201表示“资源创建成功”（比200更精准）
        "message": "用户创建成功",
        "data": new_user
    }), 201


# ------------------- 接口4：更新用户（PUT /users/<int:user_id>） -------------------
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """更新用户信息（name/email）"""
    # 1. 接收前端传的更新数据
    update_data = request.get_json()
    # 2. 找到要更新的用户
    for user in users:
        if user["id"] == user_id:
            # 3. 更新字段（只更新传了的字段，没传的保持原来的值）
            if "name" in update_data:
                user["name"] = update_data["name"]
            if "email" in update_data:
                user["email"] = update_data["email"]
            # 4. 返回更新后的用户
            return jsonify({
                "code": 200,
                "message": "用户更新成功",
                "data": user
            })
    # 没找到用户，返回404
    return jsonify({
        "code": 404,
        "message": f"用户ID {user_id} 不存在"
    }), 404


# ------------------- 接口5：删除用户（DELETE /users/<int:user_id>） -------------------
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """删除指定ID的用户"""
    global users  # 声明用全局的users列表
    # 遍历找到要删除的用户
    for index, user in enumerate(users):
        if user["id"] == user_id:
            # 从列表中删除该用户
            del users[index]
            return jsonify({
                "code": 200,
                "message": f"用户ID {user_id} 删除成功"
            })
    # 没找到用户，返回404
    return jsonify({
        "code": 404,
        "message": f"用户ID {user_id} 不存在"
    }), 404


# 启动服务器
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


#创建第一个FastApi
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# uvicorn.run(app, host="0.0.0.0", port=8000)
#

#创建第二个FastApi
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str
#     price: float
#     tax: float
# @app.post('/items')
# async def create_item(item: Item):
#     return {'name': item.name, 'price': item.price, 'tax': item.tax}

#FastAPI实现待办事项API
