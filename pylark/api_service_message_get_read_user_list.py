# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetMessageReadUserListReqUserIDType(object):
    pass


@attr.s
class GetMessageReadUserListReq(object):
    user_id_type: GetMessageReadUserListReqUserIDType = attr.ib(
        factory=lambda: GetMessageReadUserListReqUserIDType(),
        metadata={"req_type": "query"},
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 此次调用中使用的分页的大小, 示例值：20, 取值范围：`1` ～ `100`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 下一页分页的token, 示例值："GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ=="
    message_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 待查询的消息的ID, 示例值："om_dc13264520392913993dd051dba21dcf"


@attr.s
class GetMessageReadUserListRespItemUserIDType(object):
    pass


@attr.s
class GetMessageReadUserListRespItem(object):
    user_id_type: GetMessageReadUserListRespItemUserIDType = attr.ib(
        factory=lambda: GetMessageReadUserListRespItemUserIDType(),
        metadata={"req_type": "json"},
    )  # 用户id类型
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户id
    timestamp: str = attr.ib(default="", metadata={"req_type": "json"})  # 阅读时间


@attr.s
class GetMessageReadUserListResp(object):
    items: typing.List[GetMessageReadUserListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # -
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有下一页
    page_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 下一页分页的token


def _gen_get_message_read_user_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetMessageReadUserListResp,
        scope="Message",
        api="GetMessageReadUserList",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/messages/:message_id/read_users",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
