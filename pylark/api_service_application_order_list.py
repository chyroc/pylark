# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetApplicationOrderListReq(object):
    status: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 获取用户购买套餐信息设置的过滤条件, normal为正常状态，refunded为已退款，该字段为空或者all表示所有，未支付的订单无法查到
    page_size: int = attr.ib(default=0, metadata={"req_type": "query"})  # `每页显示的订单数量`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 翻页标识，可以从上次请求的响应中获取，不填或者为空时表示从开头获取
    tenant_key: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 购买应用的租户唯一标识，为空表示获取应用下所有订单，有值表示获取应用下该租户购买的订单


@attr.s
class GetApplicationOrderListRespOrderList(object):
    order_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 订单ID，唯一标识
    price_plan_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 价格方案ID，唯一标识
    price_plan_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 价格方案类型 "trial" -试用；"permanent"-一次性付费；"per_year"-企业年付费；"per_month"-企业月付费；"per_seat_per_year"-按人按年付费；"per_seat_per_month"-按人按月付费；"permanent_count"-按次付费；
    seats: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 实际购买人数 仅对price_plan_type为per_seat_per_year和per_seat_per_month 有效
    buy_count: int = attr.ib(default=0, metadata={"req_type": "json"})  # 购买数量 总是为1
    create_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 订单创建时间戳
    pay_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 订单支付时间戳
    status: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 订单当前状态，"normal" -正常；"refund"-已退款；
    buy_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 购买类型，"buy" - 普通购买;"upgrade"-为升级购买(仅price_plan_type 为per_year，per_month，per_seat_per_year，per_seat_per_month时可升级购买);"renew" - 续费购买；
    src_order_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 源订单ID，当前订单为升级购买时，即buy_type为upgrade时，此字段记录源订单等ID
    dst_order_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 升级后的新订单ID，当前订单如果做过升级购买，此字段记录升级购买后生成的新订单ID，当前订单仍然有效
    order_pay_price: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 订单实际支付金额, 单位分
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # 租户唯一标识


@attr.s
class GetApplicationOrderListResp(object):
    total: int = attr.ib(default=0, metadata={"req_type": "json"})  # 总订单数
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有数据，true还有数据，false没有数据
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 下一页数据的标识，可作为请求下一页数据的参数，当has_more为false时该字段为空
    order_list: GetApplicationOrderListRespOrderList = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 订单信息列表


def _gen_get_application_order_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApplicationOrderListResp,
        scope="Application",
        api="GetApplicationOrderList",
        method="GET",
        url="https://open.feishu.cn/open-apis/pay/v1/order/list",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )