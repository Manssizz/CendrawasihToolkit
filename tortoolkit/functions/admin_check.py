# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin,ChannelParticipantCreator,ChannelParticipantsAdmins
import logging,traceback
from ..core.getVars import get_val
torlog = logging.getLogger(__name__)

#todo add alpha admin if needed

async def is_admin(client,user_id,chat_id, force_owner=False):
    if force_owner:
        if user_id == get_val("OWNER_ID"):
            return True
        else:
            return False
        
    try:
        res = await client(GetParticipantRequest(
            channel=chat_id,
            user_id=user_id
        ))

        try:
            if isinstance(res.participant,(ChannelParticipantAdmin,ChannelParticipantCreator,ChannelParticipantsAdmins)):
                return True
            else:
                
                if user_id in get_val("AUTHORIZED_CHATS"):
                    return True
                else:
                    return False
        except:
            torlog.info("Bot Accessed in Private {}".format(traceback.format_exc()))
            return False
    except Exception as e:
        torlog.info("Bot Accessed in Private {}".format(e))
        if user_id in get_val("AUTHORIZED_CHATS"):
            return True
        else:
            return False
