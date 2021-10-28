# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class OpenChatReq(object):
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "openId"}
    )  # 用户 openId
    open_chat_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "openChatId"}
    )  # 会话ID，包括单聊会话和群聊会话。示例：oc_41e7bdf4877cfc316136f4ccf6c32613


@attr.s
class OpenChatResp(object):
    pass


def _gen_open_chat_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=OpenChatResp,
        scope="AppLink",
        api="OpenChat",
        method="",
        url="https://applink.feishu.cn/client/chat/open",
        body=request,
        method_option=_new_method_option(options),
    )
