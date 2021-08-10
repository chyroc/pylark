# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetEmployeeTypeEnumListReq(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："3"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`


@attr.s
class GetEmployeeTypeEnumListRespItemI18nContent(object):
    locale: str = attr.ib(default="", metadata={"req_type": "json"})  # 语言
    value: str = attr.ib(default="", metadata={"req_type": "json"})  # i18n内容


@attr.s
class GetEmployeeTypeEnumListRespItem(object):
    enum_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 枚举值id
    enum_value: str = attr.ib(default="", metadata={"req_type": "json"})  # 枚举值
    content: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 枚举内容, 长度范围：`1` ～ `100` 字符
    enum_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 类型, 可选值有: `1`：内置类型, `2`：自定义
    enum_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 类型, 可选值有: `1`：激活, `2`：未激活
    i18n_content: GetEmployeeTypeEnumListRespItemI18nContent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # i18n定义


@attr.s
class GetEmployeeTypeEnumListResp(object):
    items: typing.List[GetEmployeeTypeEnumListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 枚举数据
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token


def _gen_get_employee_type_enum_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetEmployeeTypeEnumListResp,
        scope="Contact",
        api="GetEmployeeTypeEnumList",
        method="GET",
        url="https://open.feishu.cn/open-apis/contact/v3/employee_type_enums",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
