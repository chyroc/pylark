# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class MoveDocsToWikiReq(object):
    space_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "space_id"}
    )  # 知识库id, 示例值："1565676577122621"
    parent_wiki_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_wiki_token"}
    )  # 节点的父亲token, 示例值："wikbcOHIFxB0PJS2UTd2kF2SP6c"
    obj_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "obj_type"}
    )  # 文档类型, 示例值："doc", 可选值有: `doc`：doc, `sheet`：sheet, `bitable`：bitable, `mindnote`：mindnote
    obj_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "obj_token"}
    )  # 文档token, 示例值："docbc6e1qBqt1O5mCBVA1QUKVEg"


@attr.s
class MoveDocsToWikiResp(object):
    wiki_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "wiki_token"}
    )  # 移动后的知识库token


def _gen_move_docs_to_wiki_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=MoveDocsToWikiResp,
        scope="Drive",
        api="MoveDocsToWiki",
        method="POST",
        url="https://open.feishu.cn/open-apis/wiki/v2/spaces/:space_id/nodes/move_docs_to_wiki",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
