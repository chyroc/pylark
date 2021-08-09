# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetAttendanceUserFlowReqEmployeeType(object):
    pass


@attr.s
class GetAttendanceUserFlowReq(object):
    employee_type: GetAttendanceUserFlowReqEmployeeType = attr.ib(
        factory=lambda: GetAttendanceUserFlowReqEmployeeType(),
        metadata={"req_type": "query"},
    )  # 请求体中的 user_id 和 creator_id 的员工工号类型，可用值：【employee_id（员工的 employeeId），employee_no（员工工号）】，示例值：“employee_id”
    user_flow_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 打卡流水记录 ID，示例值："6708236686834352397"


@attr.s
class GetAttendanceUserFlowRespLatitude(object):
    pass


@attr.s
class GetAttendanceUserFlowRespLongitude(object):
    pass


@attr.s
class GetAttendanceUserFlowResp(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 员工工号
    creator_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 打卡记录创建者的 employee_no
    location_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 打卡位置名称信息
    check_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 打卡时间，精确到秒的时间戳
    comment: str = attr.ib(default="", metadata={"req_type": "json"})  # 打卡备注
    record_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 打卡记录 ID
    longitude: float = attr.ib(default=None, metadata={"req_type": "json"})  # 打卡经度
    latitude: float = attr.ib(default=None, metadata={"req_type": "json"})  # 打卡纬度
    ssid: str = attr.ib(default="", metadata={"req_type": "json"})  # 打卡 Wi-Fi 的 SSID
    bssid: str = attr.ib(default="", metadata={"req_type": "json"})  # 打卡 Wi-Fi 的 MAC 地址
    is_field: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否为外勤打卡
    is_wifi: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否为 Wi-Fi 打卡
    type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 记录生成方式，可用值：【0（用户自己打卡），1（管理员修改），2（用户补卡），3（系统自动生成），4（下班免打卡），5（考勤机打卡），6（极速打卡），7（考勤开放平台导入），8（飞书自研考勤机），9（飞书门禁考勤机）】
    photo_urls: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 打卡照片列表
    device_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 手机打卡设备ID


def _gen_get_attendance_user_flow_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAttendanceUserFlowResp,
        scope="Attendance",
        api="GetAttendanceUserFlow",
        method="GET",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_flows/:user_flow_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
