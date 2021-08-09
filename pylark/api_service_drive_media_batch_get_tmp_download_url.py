# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class BatchGetDriveMediaTmpDownloadURLReq(object):
    file_tokens: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 文件标识符列表, 示例值：boxcnabcdefg
    extra: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 拓展信息(可选), 示例值："[请参考-上传点类型及对应Extra说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/introduction)"


@attr.s
class BatchGetDriveMediaTmpDownloadURLRespTmpDownloadURL(object):
    file_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件标识符
    tmp_download_url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文件临时下载链接


@attr.s
class BatchGetDriveMediaTmpDownloadURLResp(object):
    tmp_download_urls: typing.List[
        BatchGetDriveMediaTmpDownloadURLRespTmpDownloadURL
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 临时下载列表


def _gen_batch_get_drive_media_tmp_download_url_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchGetDriveMediaTmpDownloadURLResp,
        scope="Drive",
        api="BatchGetDriveMediaTmpDownloadURL",
        method="GET",
        url="https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )