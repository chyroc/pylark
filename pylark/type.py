# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from enum import Enum


class DepartmentIDType(Enum):
    """ID类型"""

    department_id = "department_id"  # 以 department_id 来识别
    open_department_id = "open_department_id"  # open_department_id
