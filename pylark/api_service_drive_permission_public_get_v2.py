# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetDrivePublicPermissionV2Req(object):
    token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "token"}
    )  # 文件的 token，获取方式见 [概述](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)
    type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "type"}
    )  # 文档类型 "doc", "sheet" or "isv"


@attr.s
class GetDrivePublicPermissionV2Resp(object):
    security_entity: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "security_entity"}
    )  # 可创建副本/打印/导出/复制设置：<br>"anyone_can_view" - 所有可访问此文档的用户<br>"anyone_can_edit" - 有编辑权限的用户
    comment_entity: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "comment_entity"}
    )  # 可评论设置：<br>"anyone_can_view" - 所有可访问此文档的用户<br>"anyone_can_edit" - 有编辑权限的用户
    share_entity: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "share_entity"}
    )  # 谁可以添加和管理协作者：<br>"anyone"-所有可阅读或编辑此文档的用户<br>"same_tenant"-组织内所有可阅读或编辑此文档的用户<br>"only_me"-只有我可以
    link_share_entity: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "link_share_entity"}
    )  # 链接共享：<br>"tenant_readable" - 组织内获得链接的人可阅读<br>"tenant_editable" - 组织内获得链接的人可编辑<br>"anyone_readable" - 获得链接的任何人可阅读<br>"anyone_editable" - 获得链接的任何人可编辑
    external_access: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "external_access"}
    )  # 是否允许分享到租户外开关
    invite_external: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "invite_external"}
    )  # 非owner是否允许邀请外部人
    permission_version: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "permission_version"}
    )  # 权限版本号


def _gen_get_drive_public_permission_v2_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDrivePublicPermissionV2Resp,
        scope="Drive",
        api="GetDrivePublicPermissionV2",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/permission/v2/public/",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
