# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class SearchDriveFileReq(object):
    search_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "search_key"}
    )  # 搜索关键字
    count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "count"}
    )  # 搜索返回数量，0 <= count <= 50
    offset: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "offset"}
    )  # 搜索偏移位，offset >= 0，offset + count < 200
    owner_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "owner_ids"}
    )  # 文档所有者的userid
    chat_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "chat_ids"}
    )  # 文档所在群的chatid
    docs_types: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "docs_types"}
    )  # 文档类型，支持："doc", "sheet", "slide", "bitable", "mindnote", "file"


@attr.s
class SearchDriveFileRespDocsEntity(object):
    docs_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "docs_token"}
    )  # 文档token
    docs_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "docs_type"}
    )  # 文档类型
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 标题
    owner_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "owner_id"}
    )  # 文件所有者


@attr.s
class SearchDriveFileResp(object):
    docs_entities: typing.List[SearchDriveFileRespDocsEntity] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "docs_entities"}
    )  # 搜索匹配文档列表
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 搜索偏移位结果列表后是否还有数据
    total: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "total"}
    )  # 搜索匹配文档总数量


def _gen_search_drive_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SearchDriveFileResp,
        scope="Drive",
        api="SearchDriveFile",
        method="POST",
        url="https://open.feishu.cn/open-apis/suite/docs-api/search/object",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )
