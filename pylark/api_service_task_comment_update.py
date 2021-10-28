# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class UpdateTaskCommentReq(object):
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "task_id"}
    )  # 任务ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"
    comment_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "comment_id"}
    )  # 评论 ID, 示例值："6937231762296684564"
    content: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "content"}
    )  # 新的评论内容, 示例值："飞流直下三千尺，疑是银河落九天"


@attr.s
class UpdateTaskCommentRespComment(object):
    content: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "content"}
    )  # 评论内容
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_id"}
    )  # 评论的父ID，创建评论时若不为空则为某条评论的回复，若不为空则不是回复
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 评论ID，由飞书服务器发号


@attr.s
class UpdateTaskCommentResp(object):
    comment: UpdateTaskCommentRespComment = attr.ib(
        default=None, metadata={"req_type": "json", "key": "comment"}
    )  # 返回修改后的任务评论详情


def _gen_update_task_comment_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateTaskCommentResp,
        scope="Task",
        api="UpdateTaskComment",
        method="PUT",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/comments/:comment_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
