# -*- coding:UTF-8 -*-
from app_db.models import UserInfo
from django.core.exceptions import ObjectDoesNotExist

def updata(u_id,type,data):
    try:
        user = UserInfo.objects.get(id=u_id)
        if type == 0:
            user.nick_name = data
        else:
            user.introduce = data
    except ObjectDoesNotExist:
        return 1

    return 0