from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from utils.hashing import verify_passwd, bcrypt
from app.models.user import login, register, change_password
from utils.validate import is_valid_username, is_valid_password
from utils.database import copy_database
import pymysql
import shutil
import os

router = APIRouter()


@router.get('/user')
async def get_current_user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return Authorize.get_jwt_subject()


@router.post('/register')
async def Register(request: register):
    username = request.username
    password = request.password
    reason = is_valid_username(username)
    if reason != "success":
        return {"status": "failure", "reason": reason}
    reason = is_valid_password(password)
    if reason != "success":
        return {'status': "failure", "reason": reason}
    # 查询该用户名是否已存在
    sql1 = "SELECT * FROM user WHERE name = '" + username + "';"
    db_user = pymysql.connect(host='localhost', user='root', password='zyy917382', database='user')
    cursor = db_user.cursor()
    cursor.execute(sql1)
    result = cursor.fetchone()
    if result:
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": "该用户名已存在！"}
    # 插入新用户信息
    hashed = bcrypt(password)
    sql2 = "INSERT INTO user(name, password) VALUES ('" + username + "', '" + hashed + "');"
    try:
        cursor.execute(sql2)
        db_user.commit()
    except:
        db_user.rollback()
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": "内部错误"}
    cursor.close()
    db_user.close()
    # 为新用户复制一份数据库
    try:
        copy_database(username)
    except:
        return {"status": "failure", "reason": "内部错误"}
    os.makedirs("data/" + username)
    shutil.copyfile("data/col_names.json", "data/"+username+"/col_names.json")
    return {"status": "success"}


@router.post('/login')
async def Login(request: login, Authorize: AuthJWT = Depends()):
    username = request.username
    password = request.password
    sql1 = "SELECT * FROM user WHERE name = '" + username + "';"
    db_user = pymysql.connect(host='localhost', user='root', password='zyy917382', database='user')
    cursor = db_user.cursor()
    cursor.execute(sql1)
    result = cursor.fetchone()
    if not result:
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": "该用户不存在"}
    if not verify_passwd(result[1], password):
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": '密码错误'}
    access_token = Authorize.create_access_token(subject=username, fresh=True)
    refresh_token = Authorize.create_refresh_token(subject=username)
    cursor.close()
    db_user.close()
    return {"status": "success", "access_token": access_token, "token_type": "bearer",
            "refresh_token": refresh_token}


@router.post('/change_password')
async def change_password(request: change_password):
    new_password = request.new_password
    username = request.username
    sql1 = "SELECT * FROM user WHERE name = '" + username + "';"
    db_user = pymysql.connect(host='localhost', user='root', password='zyy917382', database='user')
    cursor = db_user.cursor()
    cursor.execute(sql1)
    result = cursor.fetchone()
    if not result:
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": "该用户不存在"}
    reason = is_valid_password(new_password)
    if reason != "success":
        cursor.close()
        db_user.close()
        return {'status': "failure", "reason": reason}
    hashed = bcrypt(new_password)
    if hashed == result[1]:
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": "密码不能与修改前相同"}
    sql2 = "UPDATE user SET password = '" + hashed + "' WHERE name = '" + username + "';"
    try:
        cursor.execute(sql2)
        db_user.commit()
    except:
        db_user.rollback()
        cursor.close()
        db_user.close()
        return {"status": "failure", "reason": "内部错误"}
    cursor.close()
    db_user.close()
    return {"status": "success"}

