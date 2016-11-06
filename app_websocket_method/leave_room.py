# -*- coding:UTF-8 -*-
# 将其从相应房间删除，并将该玩家的信息删除

from app_db.models import RoomInfo
from app_db.models import PlayerInfo
from django.core.exceptions import ObjectDoesNotExist
import glob

def leave(room_id,user_name):
    if glob.room_id[room_id] == 0:
        return False
    elif glob.room_mark[room_id].get(user_name,default=-1) == -1:   #该房间不存在该用户
        return False

    # 操作数据库
    r = RoomInfo.objects.get(r_id=room_id)
    #...
    r.save()

    p = PlayerInfo.objects.get(name = user_name)
    p.delete()

    # 更改glob
    del glob.room_mark[room_id][user_name]

    return True