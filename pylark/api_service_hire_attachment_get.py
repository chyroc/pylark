# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHireAttachmentReq(object):
    attachment_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "attachment_id"}
    )  # 附件id, 示例值："6435242341238"


@attr.s
class GetHireAttachmentRespAttachment(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 附件id
    url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "url"}
    )  # 附件的url
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 附件文件名
    mime: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "mime"}
    )  # 媒体类型/MIME
    create_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "create_time"}
    )  # 附件创建时间（单位ms）


@attr.s
class GetHireAttachmentResp(object):
    attachment: GetHireAttachmentRespAttachment = attr.ib(
        default=None, metadata={"req_type": "json", "key": "attachment"}
    )  # 附件信息


def _gen_get_hire_attachment_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireAttachmentResp,
        scope="Hire",
        api="GetHireAttachment",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/attachments/:attachment_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
