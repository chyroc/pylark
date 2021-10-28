# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateHelpdeskCategoryReq(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 名称, 示例值："创建团队和邀请成员"
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_id"}
    )  # 父知识库分类ID, 示例值："0"
    language: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "language"}
    )  # 语言, 示例值："zh_cn"


@attr.s
class CreateHelpdeskCategoryRespCategory(object):
    category_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "category_id"}
    )  # 知识库分类ID
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 知识库分类ID，（旧版，请使用category_id）
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 名称
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_id"}
    )  # 父知识库分类ID
    helpdesk_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk_id"}
    )  # 服务台ID
    language: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "language"}
    )  # 语言


@attr.s
class CreateHelpdeskCategoryResp(object):
    category: CreateHelpdeskCategoryRespCategory = attr.ib(
        default=None, metadata={"req_type": "json", "key": "category"}
    )  # 知识库分类


def _gen_create_helpdesk_category_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateHelpdeskCategoryResp,
        scope="Helpdesk",
        api="CreateHelpdeskCategory",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/categories",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
        need_helpdesk_auth=True,
    )
