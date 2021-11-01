# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetContactUnitListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小，默认50，取值范围 1-100, 示例值：50, 默认值: `50`, 最大值：`100`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："AQD9/Rn9eij9Pm39ED40/dk53s4Ebp882DYfFaPFbz00L4CMZJrqGdzNyc8BcZtDbwVUvRmQTvyMYicnGWrde9X56TgdBuS+JKiSIkdexPw="


@attr.s
class GetContactUnitListRespUnit(object):
    unit_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "unit_id"}
    )  # 单位的自定义ID
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 单位的名字
    unit_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "unit_type"}
    )  # 单位的类型


@attr.s
class GetContactUnitListResp(object):
    unitlist: typing.List[GetContactUnitListRespUnit] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "unitlist"}
    )  # 单位列表
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有分页数据
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页下次调用的page_token值


def _gen_get_contact_unit_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetContactUnitListResp,
        scope="Contact",
        api="GetContactUnitList",
        method="GET",
        url="https://open.feishu.cn/open-apis/contact/v3/unit",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )