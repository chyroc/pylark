# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateTaskFollowerReqUserIDType(object):
    pass


@attr.s
class CreateTaskFollowerReq(object):
    user_id_type: IDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 任务 ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务关注者 ID, 示例值："ou_99e1a581b36ecc4862cbfbce473f3123"


@attr.s
class CreateTaskFollowerRespFollower(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 任务关注者 ID


@attr.s
class CreateTaskFollowerResp(object):
    follower: CreateTaskFollowerRespFollower = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 创建后的任务关注者


def _gen_create_task_follower_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateTaskFollowerResp,
        scope="Task",
        api="CreateTaskFollower",
        method="POST",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/followers",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )