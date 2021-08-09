# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class SendHelpdeskTicketMessageReqMsgType(object):
    pass


@attr.s
class SendHelpdeskTicketMessageReq(object):
    ticket_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 工单ID, 示例值："6948728206392295444"
    msg_type: SendHelpdeskTicketMessageReqMsgType = attr.ib(
        factory=lambda: SendHelpdeskTicketMessageReqMsgType(),
        metadata={"req_type": "json"},
    )  # 消息类型；text：纯文本；post：富文本, 示例值："post"
    content: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # - 纯文本，参考[发送文本消息](https://open.feishu.cn/document/ukTMukTMukTM/uUjNz4SN2MjL1YzM)中的content；, 富文本，参考[发送富文本消息](https://open.feishu.cn/document/ukTMukTMukTM/uMDMxEjLzATMx4yMwETM)中的content, 示例值："{,        "post": {,            "zh_cn": {,                "title": "this is title",,                "content": [,                    [,                        {,                            "tag": "text",,                            "un_escape": true,,                            "text": "第一行&nbsp;:",                        },,                        {,                            "tag": "a",,                            "text": "超链接",,                            "href": "http://www.feishu.cn",                        },                    ],,                    [,                        {,                            "tag": "text",,                            "text": "第二行 :",                        },,                        {,                            "tag": "text",,                            "text": "文本测试",                        },                    ],                ],            },        },    }"


@attr.s
class SendHelpdeskTicketMessageResp(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # chat消息open ID


def _gen_send_helpdesk_ticket_message_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SendHelpdeskTicketMessageResp,
        scope="Helpdesk",
        api="SendHelpdeskTicketMessage",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/tickets/:ticket_id/messages",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )