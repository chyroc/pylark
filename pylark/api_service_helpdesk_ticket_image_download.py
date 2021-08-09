# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class DownloadHelpdeskTicketImageReq(object):
    ticket_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 工单ID, 示例值："12345"
    msg_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 消息ID, 示例值："12345"
    index: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # index，当消息类型为post时，需指定图片index，index从0开始。当消息类型为img时，无需index, 示例值：0


@attr.s
class DownloadHelpdeskTicketImageRespFile(object):
    pass


@attr.s
class DownloadHelpdeskTicketImageResp(object):
    file: DownloadHelpdeskTicketImageRespFile = attr.ib(
        factory=lambda: DownloadHelpdeskTicketImageRespFile(),
        metadata={"req_type": "json"},
    )


@attr.s
class DownloadHelpdeskTicketImageResp(object):
    is_file: bool = attr.ib(factory=lambda: bool(), metadata={"req_type": "json"})
    code: int = attr.ib(default=0, metadata={"req_type": "json"})
    msg: str = attr.ib(default="", metadata={"req_type": "json"})
    data: DownloadHelpdeskTicketImageResp = attr.ib(
        default=None, metadata={"req_type": "json"}
    )


def _gen_download_helpdesk_ticket_image_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DownloadHelpdeskTicketImageResp,
        scope="Helpdesk",
        api="DownloadHelpdeskTicketImage",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/ticket_images",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
