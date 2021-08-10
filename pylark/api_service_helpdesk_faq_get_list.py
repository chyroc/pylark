# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHelpdeskFAQListReq(object):
    category_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 知识库分类ID, 示例值："6856395522433908739"
    status: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件: 知识库状态 1:在线 0:删除，可恢复 2：删除，不可恢复	, 示例值："1"
    search: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件: 关键词，匹配问题标题，问题关键字，用户姓名	, 示例值："点餐"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："6856395634652479491"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`


@attr.s
class GetHelpdeskFAQListRespItemCreateUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名


@attr.s
class GetHelpdeskFAQListRespItemUpdateUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名


@attr.s
class GetHelpdeskFAQListRespItemCategorie(object):
    category_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库分类ID
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 知识库分类ID，（旧版，请使用category_id）
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    parent_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 父知识库分类ID
    helpdesk_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 服务台ID
    language: str = attr.ib(default="", metadata={"req_type": "json"})  # 语言


@attr.s
class GetHelpdeskFAQListRespItem(object):
    faq_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库ID
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库旧版ID，请使用faq_id
    helpdesk_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 服务台ID
    question: str = attr.ib(default="", metadata={"req_type": "json"})  # 问题
    answer: str = attr.ib(default="", metadata={"req_type": "json"})  # 答案
    answer_richtext: str = attr.ib(default="", metadata={"req_type": "json"})  # 富文本答案
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 修改时间
    categories: typing.List[GetHelpdeskFAQListRespItemCategorie] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 分类
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 关联词列表
    expire_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 失效时间
    update_user: GetHelpdeskFAQListRespItemUpdateUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 更新用户
    create_user: GetHelpdeskFAQListRespItemCreateUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 创建用户


@attr.s
class GetHelpdeskFAQListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    page_size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 实际返回的FAQ数量
    total: int = attr.ib(default=0, metadata={"req_type": "json"})  # 总数
    items: typing.List[GetHelpdeskFAQListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 知识库列表


def _gen_get_helpdesk_faq_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskFAQListResp,
        scope="Helpdesk",
        api="GetHelpdeskFAQList",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/faqs",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_helpdesk_auth=True,
    )
