# -*- coding:UTF-8 -*-
#向客户端发送数据

from channels import Group
from channels.sessions import channel_session

import check_recive

def send(room_id,message):

    while (check_recive.check(room_id) != True):
        Group("room-%s" % room_id).send({
            "data": message,
        })


    return