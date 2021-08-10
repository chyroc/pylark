# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetDriveFileStatisticsReqFileType(object):
    pass


@attr.s
class GetDriveFileStatisticsReq(object):
    file_type: GetDriveFileStatisticsReqFileType = attr.ib(
        factory=lambda: GetDriveFileStatisticsReqFileType(),
        metadata={"req_type": "query"},
    )  # 文档类型, 示例值："doc", 可选值有: `doc`：文档, `sheet`：表格, `mindnote`：思维笔记, `bitable`：多维表格, `wiki`：知识库, `file`：文件
    file_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 文件 token, 示例值："doccnRs*******"


@attr.s
class GetDriveFileStatisticsRespStatistics(object):
    uv: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 文件历史访问人数，同一用户（user_id）多次访问按一次计算。
    pv: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 文件历史访问次数，同一用户（user_id）多次访问按多次计算。（注：同一用户相邻两次访问间隔在半小时内视为一次访问）
    like_count: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 文件历史点赞总数，若对应的文档类型不支持点赞，返回 -1
    timestamp: int = attr.ib(default=0, metadata={"req_type": "json"})  # 时间戳（秒）


@attr.s
class GetDriveFileStatisticsRespFileType(object):
    pass


@attr.s
class GetDriveFileStatisticsResp(object):
    file_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件 token
    file_type: GetDriveFileStatisticsRespFileType = attr.ib(
        factory=lambda: GetDriveFileStatisticsRespFileType(),
        metadata={"req_type": "json"},
    )  # 文件类型
    statistics: GetDriveFileStatisticsRespStatistics = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文件统计信息


def _gen_get_drive_file_statistics_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDriveFileStatisticsResp,
        scope="Drive",
        api="GetDriveFileStatistics",
        method="GET",
        url="https://open.feishu.cn/open-apis/drive/v1/files/:file_token/statistics",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
