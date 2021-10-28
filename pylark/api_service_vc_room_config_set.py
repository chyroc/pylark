# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type_enum, lark_type_sheet
import attr
import typing
import io


@attr.s
class SetVCRoomConfigReqRoomConfigDigitalSignageMaterial(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 素材ID, 示例值："7847784676276"
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 素材名称, 示例值："name"
    material_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "material_type"}
    )  # 素材类型, 示例值：0, 可选值有: `1`：图片, `2`：视频, `3`：GIF
    url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "url"}
    )  # 素材url, 示例值："url"
    duration: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "duration"}
    )  # 播放时长（单位sec）, 示例值：15
    cover: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "cover"}
    )  # 素材封面url, 示例值："url"
    md5: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "md5"}
    )  # 素材文件md5, 示例值："md5"


@attr.s
class SetVCRoomConfigReqRoomConfigDigitalSignage(object):
    enable: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "enable"}
    )  # 是否开启数字标牌功能, 示例值：true
    mute: bool = attr.ib(
        default=None, metadata={"req_type": "json", "key": "mute"}
    )  # 是否静音播放, 示例值：true
    start_display: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "start_display"}
    )  # 日程会议开始前n分钟结束播放, 示例值：3
    stop_display: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "stop_display"}
    )  # 会议结束后n分钟开始播放, 示例值：3
    materials: typing.List[
        SetVCRoomConfigReqRoomConfigDigitalSignageMaterial
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "materials"}
    )  # 素材列表


@attr.s
class SetVCRoomConfigReqRoomConfig(object):
    room_background: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "room_background"}
    )  # 飞书会议室背景图, 示例值："https://lf1-ttcdn-tos.pstatp.com/obj/xxx"
    display_background: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "display_background"}
    )  # 飞书签到板背景图, 示例值："https://lf1-ttcdn-tos.pstatp.com/obj/xxx"
    digital_signage: SetVCRoomConfigReqRoomConfigDigitalSignage = attr.ib(
        default=None, metadata={"req_type": "json", "key": "digital_signage"}
    )  # 飞书会议室数字标牌


@attr.s
class SetVCRoomConfigReq(object):
    scope: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "scope"}
    )  # 设置节点范围, 示例值：5, 可选值有: `1`：租户, `2`：国家/地区, `3`：城市, `4`：建筑, `5`：楼层, `6`：会议室
    country_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "country_id"}
    )  # 国家/地区ID scope为2，3时需要此参数, 示例值："086"
    district_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "district_id"}
    )  # 城市ID scope为3时需要此参数, 示例值："223"
    building_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "building_id"}
    )  # 建筑ID scope为4，5时需要此参数, 示例值："66"
    floor_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "floor_name"}
    )  # 楼层 scope为5时需要此参数, 示例值："3"
    room_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "room_id"}
    )  # 会议室ID scope为6时需要此参数, 示例值："67687262867363"
    room_config: SetVCRoomConfigReqRoomConfig = attr.ib(
        default=None, metadata={"req_type": "json", "key": "room_config"}
    )  # 会议室设置


@attr.s
class SetVCRoomConfigResp(object):
    pass


def _gen_set_vc_room_config_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SetVCRoomConfigResp,
        scope="VC",
        api="SetVCRoomConfig",
        method="POST",
        url="https://open.feishu.cn/open-apis/vc/v1/room_configs/set",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
