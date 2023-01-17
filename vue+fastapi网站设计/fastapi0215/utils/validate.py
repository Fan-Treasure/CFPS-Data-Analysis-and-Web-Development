import json

VALID_USERNAME_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'


def is_valid_username(name):
    if 3 <= len(name) <= 12:
        for x in name:
            if x not in VALID_USERNAME_CHARACTERS:
                return '用户名只能由字母、数字和下划线组成'
        return 'success'
    else:
        return '用户名长度应不少于3位，不得多于12位'


def is_valid_password(password):
    if 6 <= len(password) <= 16:
        return 'success'
    else:
        return '密码长度应该在6位和16位之间'
