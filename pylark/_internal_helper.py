# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import inspect
from copy import deepcopy
from enum import Enum
from io import BytesIO
from typing import List, TypeVar, Type, Any

import attr

T = TypeVar("T")


def _to_file_like(image):
    if isinstance(image, bytes):
        return BytesIO(image)

    if isinstance(image, str):
        return open(image, "rb")

    return image


def _to_attr_dict(data):
    if isinstance(data, dict):
        return {k: _to_attr_dict(v) for k, v in data.items()}
    if isinstance(data, list):
        return [_to_attr_dict(v) for v in data]
    if attr.has(data):
        return attr.asdict(data)
    return data


def _to_json(cls):
    def _f(self):
        if not hasattr(self, "__dict__"):
            return self

        d = {}
        for k, v in self.__dict__.items():
            if hasattr(v, "json"):
                d[k] = v.json()
            elif isinstance(v, list):
                d[k] = [_f(i) for i in v]
            elif isinstance(v, dict):
                d[k] = {kk: _f(vv) for kk, vv in v.items()}
            elif isinstance(v, Enum):
                d[k] = v.value
            else:
                d[k] = v

        return d

    cls.json = _f
    return cls


def _make_dataclass_from_dict(t: Type[T], kwargs: Any) -> T:
    kwargs = deepcopy(kwargs)

    if inspect.isclass(t) and issubclass(t, Enum):
        return t(kwargs)

    if isinstance(kwargs, (int, str, bool)):
        return kwargs

    if t.__class__ == List.__class__ and isinstance(kwargs, list):
        return [_make_dataclass_from_dict(t.__args__[0], i) for i in kwargs]

    if not hasattr(t, "__attrs_attrs__"):
        return kwargs

    d = {}
    attr_field = attr.fields(t)
    for att in getattr(t, "__attrs_attrs__", []):
        att_name = att.name
        json_name = getattr(attr_field, att.name).metadata.get("json") or att_name
        att_default = att.default
        att_value = kwargs.get(json_name)
        if att_value:
            d[att_name] = _make_dataclass_from_dict(att.type, att_value)
            del kwargs[json_name]
        elif att_default is attr.NOTHING:
            d[att_name] = None

    return t(**d)
