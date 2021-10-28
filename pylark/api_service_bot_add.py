# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class AddBotToChatReq(object):
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "chat_id"}
    )  # 群的id


@attr.s
class AddBotToChatResp(object):
    pass


def _gen_add_bot_to_chat_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=AddBotToChatResp,
        scope="Bot",
        api="AddBotToChat",
        method="POST",
        url="https://open.feishu.cn/open-apis/bot/v4/add",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
