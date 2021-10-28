# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateTaskCollaboratorReqUserIDType(object):
    pass


@attr.s
class CreateTaskCollaboratorReq(object):
    user_id_type: CreateTaskCollaboratorReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "task_id"}
    )  # 任务 ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 任务协作者的 ID, 示例值："ou_99e1a581b36ecc4862cbfbce473f1234"


@attr.s
class CreateTaskCollaboratorRespCollaborator(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 任务协作者的 ID


@attr.s
class CreateTaskCollaboratorResp(object):
    collaborator: CreateTaskCollaboratorRespCollaborator = attr.ib(
        default=None, metadata={"req_type": "json", "key": "collaborator"}
    )  # 返回创建成功后的任务协作者


def _gen_create_task_collaborator_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateTaskCollaboratorResp,
        scope="Task",
        api="CreateTaskCollaborator",
        method="POST",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/collaborators",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
