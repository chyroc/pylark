# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetAttendanceGroupReqEmployeeType(object):
    pass


@attr.s
class GetAttendanceGroupReq(object):
    employee_type: GetAttendanceGroupReqEmployeeType = attr.ib(
        factory=lambda: GetAttendanceGroupReqEmployeeType(),
        metadata={"req_type": "query", "key": "employee_type"},
    )  # 用户 ID 的类型，可用值：【employee_id（员工的 employeeId），employee_no（员工工号）】
    dept_type: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "dept_type"}
    )  # 部门 ID 的类型，可用值：【open_id（暂时只支持部门的 openid）】，示例值：“od-fcb45c28a45311afd441b8869541ece8”
    group_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "group_id"}
    )  # 考勤组的 ID，需要从获取打卡结果的接口中获取 group_id，示例值："6919358128597097404"


@attr.s
class GetAttendanceGroupRespGroupIDNoNeedPunchSpecialDay(object):
    punch_day: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "punch_day"}
    )  # 打卡日期，格式 20190101
    shift_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "shift_id"}
    )  # 班次 ID


@attr.s
class GetAttendanceGroupRespGroupIDNeedPunchSpecialDay(object):
    punch_day: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "punch_day"}
    )  # 打卡日期，格式 20190101
    shift_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "shift_id"}
    )  # 班次 ID


@attr.s
class GetAttendanceGroupRespGroupIDFreePunchCfg(object):
    free_start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "free_start_time"}
    )  # 自由班制的打卡开始时间
    free_end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "free_end_time"}
    )  # 自由班制的打卡结束时间
    punch_day: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "punch_day"}
    )  # 打卡时间：7 位数字，从左到右依次代表周一到周日，0 为不上班，1 为上班。例如：周一到周五上班 1111100
    work_day_no_punch_as_lack: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "work_day_no_punch_as_lack"},
    )  # 工作日不打卡是否记为缺卡


@attr.s
class GetAttendanceGroupRespGroupIDLocationLongitude(object):
    pass


@attr.s
class GetAttendanceGroupRespGroupIDLocationLatitude(object):
    pass


@attr.s
class GetAttendanceGroupRespGroupIDLocation(object):
    location_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "location_id"}
    )  # 地址 ID
    location_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "location_name"}
    )  # 地址名称
    location_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "location_type"}
    )  # 地址类型，1：GPS，2：Wifi，8：IP
    latitude: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "latitude"}
    )  # 地址纬度
    longitude: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "longitude"}
    )  # 地址经度
    ssid: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ssid"}
    )  # Wi-Fi 名称
    bssid: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "bssid"}
    )  # Wi-Fi 的 MAC 地址
    map_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "map_type"}
    )  # 地图类型，1：高德，2：谷歌
    address: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "address"}
    )  # 地址名称
    ip: str = attr.ib(default="", metadata={"req_type": "json", "key": "ip"})  # IP 地址
    feature: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "feature"}
    )  # 额外信息，例如运营商信息
    gps_range: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "gps_range"}
    )  # GPS 打卡的有效范围


@attr.s
class GetAttendanceGroupRespGroupIDMachine(object):
    machine_sn: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "machine_sn"}
    )  # 考勤机序列号
    machine_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "machine_name"}
    )  # 考勤机名称


@attr.s
class GetAttendanceGroupRespGroupID(object):
    group_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "group_name"}
    )  # 考勤组名称
    time_zone: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "time_zone"}
    )  # 时区
    bind_dept_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "bind_dept_ids"}
    )  # 绑定的部门 ID
    except_dept_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "except_dept_ids"}
    )  # 排除的部门 ID
    bind_user_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "bind_user_ids"}
    )  # 绑定的用户 ID
    except_user_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "except_user_ids"}
    )  # 排除的用户 ID
    group_leader_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "group_leader_ids"}
    )  # 考勤负责人 ID 列表，必选字段
    punch_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "punch_type"}
    )  # 考勤方式，0：考勤组人员可在任意地点、任意网络环境下打卡，1：GPS 打卡，2：Wi-Fi 打卡，4：考勤机打卡，8：IP 打卡。位运算，累加可支持多种考勤方式，比如，3：支持 GPS 打卡和 Wi-Fi 打卡，7：支持 GPS 打卡、Wi-Fi 打卡和考勤机打卡
    allow_out_punch: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "allow_out_punch"}
    )  # 是否允许外勤打卡
    allow_pc_punch: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "allow_pc_punch"}
    )  # 是否允许 PC 端打卡
    allow_remedy: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "allow_remedy"}
    )  # 是否允许补卡
    remedy_limit: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "remedy_limit"}
    )  # 是否限制补卡次数
    remedy_limit_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "remedy_limit_count"}
    )  # 补卡次数
    remedy_period_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "remedy_period_type"}
    )  # 补卡次数周期类型，0：自然月，1：自定义周期
    remedy_period_custom_date: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "remedy_period_custom_date"}
    )  # 补卡自定义周期每月起始日
    remedy_date_limit: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "remedy_date_limit"},
    )  # 是否限制补卡时间
    remedy_date_num: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "remedy_date_num"}
    )  # 补卡时间
    show_cumulative_time: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "show_cumulative_time"},
    )  # 是否展示上班累计时长
    show_over_time: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "show_over_time"}
    )  # 是否展示加班累计时长
    hide_staff_punch_time: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "hide_staff_punch_time"},
    )  # 是否隐藏员工打卡具体时间
    face_punch: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "face_punch"}
    )  # 是否开启人脸识别打卡
    face_punch_cfg: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "face_punch_cfg"}
    )  # 人脸识别打卡规则，1：每次打卡均需人脸识别，2：疑似作弊打卡时需要人脸识别
    face_downgrade: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "face_downgrade"}
    )  # 人脸识别失败时是否允许普通拍照打卡
    replace_basic_pic: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "replace_basic_pic"},
    )  # 人脸识别失败时是否允许替换基准图片
    machines: typing.List[GetAttendanceGroupRespGroupIDMachine] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "machines"}
    )  # 考勤机列表
    gps_range: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "gps_range"}
    )  # GPS 打卡的有效范围（不建议使用）
    locations: typing.List[GetAttendanceGroupRespGroupIDLocation] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "locations"}
    )  # 地址列表
    group_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "group_type"}
    )  # 考勤类型，0：固定班制，2：排班制，3：自由班制
    punch_day_shift_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "punch_day_shift_ids"}
    )  # 固定班制必须填
    free_punch_cfg: GetAttendanceGroupRespGroupIDFreePunchCfg = attr.ib(
        default=None, metadata={"req_type": "json", "key": "free_punch_cfg"}
    )  # 配置自由班制
    calendar_id: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "calendar_id"}
    )  # 国家法定节假日历 ID，0：不根据国家法定节假日历排休，1：中国，2：美国，3：日本，4：印度，5：新加坡，默认为 1
    need_punch_special_days: typing.List[
        GetAttendanceGroupRespGroupIDNeedPunchSpecialDay
    ] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "need_punch_special_days"},
    )  # 必须打卡的特殊日期
    no_need_punch_special_days: typing.List[
        GetAttendanceGroupRespGroupIDNoNeedPunchSpecialDay
    ] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "no_need_punch_special_days"},
    )  # 无需打卡的特殊日期
    work_day_no_punch_as_lack: bool = attr.ib(
        factory=lambda: bool(),
        metadata={"req_type": "json", "key": "work_day_no_punch_as_lack"},
    )  # 自由班制下，工作日不打卡是否记为缺卡


@attr.s
class GetAttendanceGroupResp(object):
    group_id: GetAttendanceGroupRespGroupID = attr.ib(
        default=None, metadata={"req_type": "json", "key": "group_id"}
    )  # 考勤组的 ID，需要从获取用户打卡结果的接口中获取 groupId


def _gen_get_attendance_group_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAttendanceGroupResp,
        scope="Attendance",
        api="GetAttendanceGroup",
        method="GET",
        url="https://open.feishu.cn/open-apis/attendance/v1/groups/:group_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
