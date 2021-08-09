# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class SearchChatReqUserIDType(object):
    pass


@attr.s
class SearchChatReq(object):
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    query: str = attr.ib(default="", metadata={"req_type": "query"})  # 关键词, 示例值："abc"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："dmJCRHhpd3JRbGV1VEVNRFFyTitRWDY5ZFkybmYrMEUwMUFYT0VMMWdENEtuYUhsNUxGMDIwemtvdE5ORjBNQQ=="
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`


@attr.s
class SearchChatRespItemOwnerIDType(object):
    pass


@attr.s
class SearchChatRespItem(object):
    chat_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 群组 ID
    avatar: str = attr.ib(default="", metadata={"req_type": "json"})  # 群头像 URL
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 群名称
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 群描述
    owner_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 群主 ID
    owner_id_type: SearchChatRespItemOwnerIDType = attr.ib(
        factory=lambda: SearchChatRespItemOwnerIDType(), metadata={"req_type": "json"}
    )  # 群主 ID 类型


@attr.s
class SearchChatResp(object):
    items: typing.List[SearchChatRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # chat 列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项


def _gen_search_chat_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SearchChatResp,
        scope="Chat",
        api="SearchChat",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/chats/search",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
