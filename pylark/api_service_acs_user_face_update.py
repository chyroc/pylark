# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateACSUserFaceReqFileType(object):
    pass


@attr.s
class UpdateACSUserFaceReqFiles(object):
    pass


@attr.s
class UpdateACSUserFaceReqUserIDType(object):
    pass


@attr.s
class UpdateACSUserFaceReq(object):
    user_id_type: UpdateACSUserFaceReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 用户 ID, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    files: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 人脸图片内容, 示例值：jpg图片
    file_type: UpdateACSUserFaceReqFileType = attr.ib(
        factory=lambda: UpdateACSUserFaceReqFileType(), metadata={"req_type": "json"}
    )  # 文件类型,可选的类型有jpg,png, 示例值："jpg"
    file_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 带后缀的文件名, 示例值："efeqz12f.jpg"


@attr.s
class UpdateACSUserFaceResp(object):
    pass


def _gen_update_acs_user_face_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateACSUserFaceResp,
        scope="ACS",
        api="UpdateACSUserFace",
        method="PUT",
        url="https://open.feishu.cn/open-apis/acs/v1/users/:user_id/face",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        is_file=True,
    )
