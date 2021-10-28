# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetApplicationAppListReq(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页起始位置标示，不填表示从头开始
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 单页需求最大个数（最大 100），0 自动最大个数
    lang: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "lang"}
    )  # 优先展示的应用信息的语言版本（zh_cn：中文，en_us：英文，ja_jp：日文）
    status: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "status"}
    )  # 要返回的应用的状态，0:停用；1:启用；-1:全部，默认为 -1


@attr.s
class GetApplicationAppListRespAppList(object):
    app_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "app_id"}
    )  # 应用 ID
    primary_language: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "primary_language"}
    )  # 应用首选语言
    app_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "app_name"}
    )  # 应用名称
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 应用描述
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # 应用 icon
    app_scene_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "app_scene_type"}
    )  # 应用类型，0：企业自建应用；1：应用商店应用
    status: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "status"}
    )  # 启停状态，0：停用；1：启用
    mobile_default_ability: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "mobile_default_ability"}
    )  # 移动端默认的应用功能，0：未开启；1：小程序；2：H5；8：机器人
    pc_default_ability: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "pc_default_ability"}
    )  # PC客户端默认的应用功能，0：未开启；1：小程序；2：H5；8：机器人


@attr.s
class GetApplicationAppListResp(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 下一个请求页应当给的起始位置
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "page_size"}
    )  # 本次请求实际返回的页大小
    total_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "total_count"}
    )  # 可用的应用总数
    has_more: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多应用
    lang: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "lang"}
    )  # 当前选择的版本语言
    app_list: GetApplicationAppListRespAppList = attr.ib(
        default=None, metadata={"req_type": "json", "key": "app_list"}
    )  # 应用列表


def _gen_get_application_app_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApplicationAppListResp,
        scope="Application",
        api="GetApplicationAppList",
        method="GET",
        url="https://open.feishu.cn/open-apis/application/v3/app/list",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
