# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class TranslateTextReqGlossary(object):
    from_: str = attr.ib(default="", metadata={"req_type": "json"})  # 原文, 示例值："飞书"
    to: str = attr.ib(default="", metadata={"req_type": "json"})  # 译文, 示例值："Lark"


@attr.s
class TranslateTextReq(object):
    source_language: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 源语言, 示例值："zh"
    text: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 源文本, 示例值："尝试使用一下飞书吧"
    target_language: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 目标语言, 示例值："en"
    glossary: TranslateTextReqGlossary = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 请求级术语表，携带术语，仅在本次翻译中生效（最多能携带 128个术语词）


@attr.s
class TranslateTextResp(object):
    text: str = attr.ib(default="", metadata={"req_type": "json"})  # 翻译后的文本


def _gen_translate_text_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=TranslateTextResp,
        scope="AI",
        api="TranslateText",
        method="POST",
        url="https://open.feishu.cn/open-apis/translation/v1/text/translate",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
