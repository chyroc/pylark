# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetTaskFollowerListReqUserIDType(object):
    pass


@attr.s
class GetTaskFollowerListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`50`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："「上次返回的page_token」"
    user_id_type: lark_type_enum.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "task_id"}
    )  # 任务 ID, 示例值："0d38e26e-190a-49e9-93a2-35067763ed1f"


@attr.s
class GetTaskFollowerListRespItem(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 任务关注者 ID


@attr.s
class GetTaskFollowerListResp(object):
    items: typing.List[GetTaskFollowerListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 返回的关注者列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项


def _gen_get_task_follower_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetTaskFollowerListResp,
        scope="Task",
        api="GetTaskFollowerList",
        method="GET",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/followers",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
