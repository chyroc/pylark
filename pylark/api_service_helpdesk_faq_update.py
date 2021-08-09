# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class UpdateHelpdeskFAQReqFAQ(object):
    category_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 知识库分类ID, 示例值："6836004780707807251"
    question: str = attr.ib(default="", metadata={"req_type": "json"})  # 问题, 示例值："问题"
    answer: str = attr.ib(default="", metadata={"req_type": "json"})  # 答案, 示例值："答案"
    answer_richtext: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 富文本答案和答案必须有一个必填。Json Array格式，富文本结构请见[了解更多: 富文本](https://open.feishu.cn/document/ukTMukTMukTM/uITM0YjLyEDN24iMxQjN), 示例值："[{,                        "content": "这只是一个测试，医保问题",,                        "type": "text",                    }]"
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 关联词


@attr.s
class UpdateHelpdeskFAQReq(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 知识库ID, 示例值："6856395634652479491"
    faq: UpdateHelpdeskFAQReqFAQ = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 修改的知识库内容


@attr.s
class UpdateHelpdeskFAQResp(object):
    pass


def _gen_update_helpdesk_faq_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateHelpdeskFAQResp,
        scope="Helpdesk",
        api="UpdateHelpdeskFAQ",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/faqs/:id",
        body=request,
        method_option=_new_method_option(options),
    )