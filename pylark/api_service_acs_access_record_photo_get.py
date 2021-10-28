# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class GetACSAccessRecordPhotoReq(object):
    access_record_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "access_record_id"}
    )  # 门禁访问记录 ID, 示例值："6939433228970082591"


@attr.s
class GetACSAccessRecordPhotoRespFile(object):
    pass


@attr.s
class GetACSAccessRecordPhotoResp(object):
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json", "key": "file"}
    )


@attr.s
class GetACSAccessRecordPhotoResp(object):
    is_file: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_file"}
    )
    code: int = attr.ib(default=0, metadata={"req_type": "json", "key": "code"})
    msg: str = attr.ib(default="", metadata={"req_type": "json", "key": "msg"})
    data: GetACSAccessRecordPhotoResp = attr.ib(
        default=None, metadata={"req_type": "json", "key": "data"}
    )


def _gen_get_acs_access_record_photo_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetACSAccessRecordPhotoResp,
        scope="ACS",
        api="GetACSAccessRecordPhoto",
        method="GET",
        url="https://open.feishu.cn/open-apis/acs/v1/access_records/:access_record_id/access_photo",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
