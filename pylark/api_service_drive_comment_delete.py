# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteDriveCommentReqFileType(object):
    pass


@attr.s
class DeleteDriveCommentReq(object):
    file_type: DeleteDriveCommentReqFileType = attr.ib(
        factory=lambda: DeleteDriveCommentReqFileType(),
        metadata={"req_type": "query", "key": "file_type"},
    )  # 文档类型, 示例值："doc", 可选值有: `doc`：文档, `sheet`：表格, `file`：文件
    file_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "file_token"}
    )  # 文档token, 示例值："doccnHh7U87HOFpii5u5G*****"
    comment_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "comment_id"}
    )  # 评论ID, 示例值："6916106822734578184"
    reply_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "reply_id"}
    )  # 回复ID, 示例值："6916106822734594568"


@attr.s
class DeleteDriveCommentResp(object):
    pass


def _gen_delete_drive_comment_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteDriveCommentResp,
        scope="Drive",
        api="DeleteDriveComment",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments/:comment_id/replies/:reply_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
