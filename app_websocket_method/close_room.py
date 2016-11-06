# -*- coding:UTF-8 -*-
# 删除相应房间和房间内所有玩家的信息

from app_db.models import RoomInfo
from app_db.models import PlayerInfo
from django.core.exceptions import ObjectDoesNotExist
import glob

def close(room_id,user_name):
    if glob.room_id[room_id] == 0:
        return False

    # 操作数据库
    r = RoomInfo.objects.get(r_id=room_id)
    r.delete()

    players = glob.room_mark[room_id].keys()    # 结果是一个列表

    for i in players:
        p = PlayerInfo.objects.get(name=i)
        p.delete()

    # 更改glob
    del glob.room_request_id[room_id]
    del glob.room_player_num[room_id]
    del glob.room_mark[room_id]

    return True