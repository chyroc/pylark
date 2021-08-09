# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateHelpdeskFAQReqFAQ(object):
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
class CreateHelpdeskFAQReq(object):
    faq: CreateHelpdeskFAQReqFAQ = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 知识库详情


@attr.s
class CreateHelpdeskFAQRespFAQCreateUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名


@attr.s
class CreateHelpdeskFAQRespFAQUpdateUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名


@attr.s
class CreateHelpdeskFAQRespFAQCategorie(object):
    category_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库分类ID
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 知识库分类ID，（旧版，请使用category_id）
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    parent_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 父知识库分类ID
    helpdesk_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 服务台ID
    language: str = attr.ib(default="", metadata={"req_type": "json"})  # 语言


@attr.s
class CreateHelpdeskFAQRespFAQ(object):
    faq_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库ID
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库旧版ID，请使用faq_id
    helpdesk_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 服务台ID
    question: str = attr.ib(default="", metadata={"req_type": "json"})  # 问题
    answer: str = attr.ib(default="", metadata={"req_type": "json"})  # 答案
    answer_richtext: str = attr.ib(default="", metadata={"req_type": "json"})  # 富文本答案
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 修改时间
    categories: typing.List[HelpdeskCategory] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 分类
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 关联词列表
    expire_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 失效时间
    update_user: CreateHelpdeskFAQRespFAQUpdateUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 更新用户
    create_user: CreateHelpdeskFAQRespFAQCreateUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 创建用户


@attr.s
class CreateHelpdeskFAQResp(object):
    faq: CreateHelpdeskFAQRespFAQ = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 知识库详情


def _gen_create_helpdesk_faq_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateHelpdeskFAQResp,
        scope="Helpdesk",
        api="CreateHelpdeskFAQ",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/faqs",
        body=request,
        method_option=_new_method_option(options),
    )
