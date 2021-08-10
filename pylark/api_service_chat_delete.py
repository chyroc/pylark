# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteChatReq(object):
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 群 ID, 示例值："oc_a0553eda9014c201e6969b478895c230"


@attr.s
class DeleteChatResp(object):
    pass


def _gen_delete_chat_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteChatResp,
        scope="Chat",
        api="DeleteChat",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/im/v1/chats/:chat_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
