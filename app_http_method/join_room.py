# -*- coding:UTF-8 -*-
# 加入房间并创建新玩家

from app_db.models import RoomInfo
from app_db.models import UserInfo
from django.core.exceptions import ObjectDoesNotExist
import app_websocket_method.glob

#如何确定房间已满？？？？？？？？？？

def join(u_id,r_id):

    if app_websocket_method.glob.room_id[r_id] == 0:
        return 1
    #elif len(glob.room_mark[room_id]) >= glob.room_player_num[room_id]:
    #    return 2


    # 操作数据库
    user = UserInfo.objects.get(id = u_id)
    # 修改房间信息
    r = RoomInfo.objects.get(room_id=r_id)
    r.player_num = r.player_num+1
    r.player_id = r.player_id + ',' + str(u_id)
    r.player_nick = r.player_nick + ',' + user.nick_name
    r.player_role = r.player_role + ',' + "village"
    r.player_alive = r.player_alive + ',' + 'true'
    r.save()

    # 添加玩家信息
    #newPlayer = PlayerInfo(name=user_name, room_id=room_id, alive=True)
    #newPlayer.save()

    # 更改glob
    app_websocket_method.glob.room_mark[r_id][u_id] = 0

    return 0