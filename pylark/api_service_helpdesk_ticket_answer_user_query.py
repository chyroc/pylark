# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class AnswerHelpdeskTicketUserQueryReqFAQScore(object):
    pass


@attr.s
class AnswerHelpdeskTicketUserQueryReqFAQ(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # faq服务台内唯一标识, 示例值："12345"
    score: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # faq匹配得分, 示例值：0.9


@attr.s
class AnswerHelpdeskTicketUserQueryReq(object):
    ticket_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 工单ID, 示例值："6945345902185807891"
    event_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 事件ID,可从订阅事件中提取, 示例值："abcd"
    faqs: typing.List[AnswerHelpdeskTicketUserQueryReqFAQ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # faq结果列表


@attr.s
class AnswerHelpdeskTicketUserQueryResp(object):
    pass


def _gen_answer_helpdesk_ticket_user_query_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=AnswerHelpdeskTicketUserQueryResp,
        scope="Helpdesk",
        api="AnswerHelpdeskTicketUserQuery",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/tickets/:ticket_id/answer_user_query",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )