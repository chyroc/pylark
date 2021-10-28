# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class ImportSheetReqFile(object):
    pass


@attr.s
class ImportSheetReq(object):
    file: bytes = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "file"}
    )  # 需要导入的文件数据，转换成字节数组的形式，支持"xlsx","csv"格式，最大不超过20M
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 文件名，带上文件拓展名，如"hello.csv"、"hello.xlsx"。导入后sheet的标题将去除文件拓展名，如"hello.xlsx"导入后标题为"hello"。
    folder_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "folderToken"}
    )  # 导入的文件夹token，默认导入到根目录下


@attr.s
class ImportSheetResp(object):
    ticket: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ticket"}
    )  # 与导入文件一一对应的凭证，用于查询文件导入的进度，详见[查询导入结果的接口](https://open.feishu.cn/document/ukTMukTMukTM/uETO2YjLxkjN24SM5YjN)


def _gen_import_sheet_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=ImportSheetResp,
        scope="Drive",
        api="ImportSheet",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v2/import",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
