# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetWikiSpaceReq(object):
    space_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "space_id"}
    )  # 知识空间id, 示例值："6870403571079249922"


@attr.s
class GetWikiSpaceRespSpace(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 知识空间名称
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 知识空间描述
    space_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "space_id"}
    )  # 知识空间id


@attr.s
class GetWikiSpaceResp(object):
    space: GetWikiSpaceRespSpace = attr.ib(
        default=None, metadata={"req_type": "json", "key": "space"}
    )  # 知识空间


def _gen_get_wiki_space_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetWikiSpaceResp,
        scope="Drive",
        api="GetWikiSpace",
        method="GET",
        url="https://open.feishu.cn/open-apis/wiki/v2/spaces/:space_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
