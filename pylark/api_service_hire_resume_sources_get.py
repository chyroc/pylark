# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHireResumeSourceReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："1"


@attr.s
class GetHireResumeSourceRespItem(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 简历来源id
    zh_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文名
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名
    resume_source_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 简历源类型, 可选值有: `10000`：内推, `10001`：猎头, `10002`：内部来源, `10003`：第三方招聘网站, `10004`：社交媒体, `10005`：线下来源, `10006`：其他


@attr.s
class GetHireResumeSourceResp(object):
    items: typing.List[GetHireResumeSourceRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 数据
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项


def _gen_get_hire_resume_source_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireResumeSourceResp,
        scope="Hire",
        api="GetHireResumeSource",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/resume_sources",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
