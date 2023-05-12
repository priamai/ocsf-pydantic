"""
Module Docstring
"""

__author__ = "Paolo Di Prodi"
__version__ = "0.1.0"
__license__ = "Apache GPL 2"

from typing import List

from pydantic import BaseModel

class Product(BaseModel):
    lang: str
    name: str
    uid: str
    vendor_name: str
    version: str


class Metadata(BaseModel):
    correlation_uid: str
    original_time: str
    product: Product
    profiles: List[str]
    version: str


class Model(BaseModel):
    activity_id: int
    activity_name: str
    category_name: str
    category_uid: int
    class_name: str
    class_uid: int
    message: str
    metadata: Metadata
    severity: str
    severity_id: int
    start_time: int
    status: str
    status_id: int
    time: int
    timezone_offset: int
    type_name: str
    type_uid: int
