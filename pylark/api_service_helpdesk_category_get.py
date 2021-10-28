# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetHelpdeskCategoryReq(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "id"}
    )  # 知识库分类ID, 示例值："6948728206392295444"


@attr.s
class GetHelpdeskCategoryResp(object):
    category_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "category_id"}
    )  # 知识库分类ID
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 知识库分类ID，（旧版，请使用category_id）
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 名称
    helpdesk_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk_id"}
    )  # 服务台ID
    language: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "language"}
    )  # 语言


def _gen_get_helpdesk_category_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskCategoryResp,
        scope="Helpdesk",
        api="GetHelpdeskCategory",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/categories/:id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_helpdesk_auth=True,
    )
