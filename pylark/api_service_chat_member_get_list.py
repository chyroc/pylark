# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetChatMemberListReqMemberIDType(object):
    pass


@attr.s
class GetChatMemberListReq(object):
    member_id_type: GetChatMemberListReqMemberIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 群成员 id 类型 open_id/user_id/union_id, 示例值："user_id", 可选值有: `user_id`：以 user_id 来识别成员, `union_id`：以 union_id 来识别成员, `open_id`：以 open_id 来识别成员
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："dmJCRHhpd3JRbGV1VEVNRFFyTitRWDY5ZFkybmYrMEUwMUFYT0VMMWdENEtuYUhsNUxGMDIwemtvdE5ORjBNQQ=="
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 群 ID, 示例值："oc_a0553eda9014c201e6969b478895c230"


@attr.s
class GetChatMemberListRespItemMemberIDType(object):
    pass


@attr.s
class GetChatMemberListRespItem(object):
    member_id_type: GetChatMemberListRespItemMemberIDType = attr.ib(
        factory=lambda: GetChatMemberListRespItemMemberIDType(),
        metadata={"req_type": "json"},
    )  # member id 类型
    member_id: str = attr.ib(default="", metadata={"req_type": "json"})  # member id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名字


@attr.s
class GetChatMemberListResp(object):
    items: typing.List[GetChatMemberListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # member 列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项


def _gen_get_chat_member_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetChatMemberListResp,
        scope="Chat",
        api="GetChatMemberList",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/chats/:chat_id/members",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
