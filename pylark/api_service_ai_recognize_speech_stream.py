# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from dataclasses import dataclass, field


@dataclass
class RecognizeSpeechStreamReqConfig(object):
    stream_id: str = field(
        default="", metadata={"req_type": "json"}
    )  # 仅包含字母数字和下划线的 16 位字符串作为同一数据流的标识，用户生成, 示例值："asd1234567890ddd"
    sequence_id: int = field(
        default=0, metadata={"req_type": "json"}
    )  # 数据流分片的序号，序号从 0 开始，每次请求递增 1, 示例值：1
    action: int = field(
        default=0, metadata={"req_type": "json"}
    )  # 数据流标记：1 首包，2 正常结束，等待结果返回，3 中断数据流不返回最终结果, 示例值：1
    format: str = field(
        default="", metadata={"req_type": "json"}
    )  # 语音格式，目前仅支持：pcm, 示例值："pcm"
    engine_type: str = field(
        default="", metadata={"req_type": "json"}
    )  # 引擎类型，目前仅支持：16k_auto 中英混合, 示例值："16k_auto"


@dataclass
class RecognizeSpeechStreamReqSpeech(object):
    speech: str = field(
        default="", metadata={"req_type": "json"}
    )  # base64 后的音频文件进行, 示例值："base64 后的音频内容"


@dataclass
class RecognizeSpeechStreamReq(object):
    speech: RecognizeSpeechStreamReqSpeech = field(
        default_factory=RecognizeSpeechStreamReqSpeech(), metadata={"req_type": "json"}
    )  # 语音资源
    config: RecognizeSpeechStreamReqConfig = field(
        default_factory=RecognizeSpeechStreamReqConfig(), metadata={"req_type": "json"}
    )  # 配置属性


@dataclass
class RecognizeSpeechStreamResp(object):
    stream_id: str = field(
        default="", metadata={"req_type": "json"}
    )  # 16 位 String 随机串作为同一数据流的标识
    sequence_id: int = field(
        default=0, metadata={"req_type": "json"}
    )  # 数据流分片的序号，序号从 0 开始，每次请求递增 1
    recognition_text: str = field(
        default="", metadata={"req_type": "json"}
    )  # 语音流识别后的文本信息


def _gen_recognize_speech_stream_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=RecognizeSpeechStreamResp,
        scope="AI",
        api="RecognizeSpeechStream",
        method="POST",
        url="https://open.feishu.cn/open-apis/speech_to_text/v1/speech/stream_recognize",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )