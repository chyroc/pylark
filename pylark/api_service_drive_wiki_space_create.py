# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateWikiSpaceReq(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 知识空间名称, 示例值："知识空间"
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 知识空间描述, 示例值："知识空间描述"


@attr.s
class CreateWikiSpaceRespSpace(object):
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
class CreateWikiSpaceResp(object):
    space: CreateWikiSpaceRespSpace = attr.ib(
        default=None, metadata={"req_type": "json", "key": "space"}
    )  # 知识空间


def _gen_create_wiki_space_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateWikiSpaceResp,
        scope="Drive",
        api="CreateWikiSpace",
        method="POST",
        url="https://open.feishu.cn/open-apis/wiki/v2/spaces",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )
