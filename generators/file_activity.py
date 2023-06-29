# generated by datamodel-codegen:
#   filename:  https://schema.ocsf.io/api/1.0.0-rc.3/classes/file_activity?profiles=security_control
#   timestamp: 2023-06-29T17:39:43+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Associations(BaseModel):
    actor_user: List[str] = Field(..., alias='actor.user')
    device: List[str]


class AccessMask(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Count(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    default: int
    description: str
    group: str
    type: str
    type_name: str


class CategoryName(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class TypeName(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class FileDiff(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Time(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Disposition(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    profile: str
    requirement: str
    type: str
    type_name: str


class ConnectionUid(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Field0(BaseModel):
    caption: str
    description: str


class Field1(BaseModel):
    caption: str
    description: str


class Field10(BaseModel):
    caption: str
    description: str


class Field11(BaseModel):
    caption: str
    description: str


class Field12(BaseModel):
    caption: str
    description: str


class Field13(BaseModel):
    caption: str
    description: str


class Field14(BaseModel):
    caption: str
    description: str


class Field2(BaseModel):
    caption: str
    description: str


class Field3(BaseModel):
    caption: str
    description: str


class Field4(BaseModel):
    caption: str
    description: str


class Field5(BaseModel):
    caption: str
    description: str


class Field6(BaseModel):
    caption: str
    description: str


class Field7(BaseModel):
    caption: str
    description: str


class Field8(BaseModel):
    caption: str
    description: str


class Field9(BaseModel):
    caption: str
    description: str


class Field99(BaseModel):
    caption: str
    description: str


class Enum(BaseModel):
    field_0: Field0 = Field(..., alias='0')
    field_1: Field1 = Field(..., alias='1')
    field_10: Field10 = Field(..., alias='10')
    field_11: Field11 = Field(..., alias='11')
    field_12: Field12 = Field(..., alias='12')
    field_13: Field13 = Field(..., alias='13')
    field_14: Field14 = Field(..., alias='14')
    field_2: Field2 = Field(..., alias='2')
    field_3: Field3 = Field(..., alias='3')
    field_4: Field4 = Field(..., alias='4')
    field_5: Field5 = Field(..., alias='5')
    field_6: Field6 = Field(..., alias='6')
    field_7: Field7 = Field(..., alias='7')
    field_8: Field8 = Field(..., alias='8')
    field_9: Field9 = Field(..., alias='9')
    field_99: Field99 = Field(..., alias='99')


class ActivityId(BaseModel):
    field_source: str = Field(..., alias='_source')
    attributes: List
    caption: str
    description: str
    enum: Enum
    group: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class FileResult(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    object_name: str
    object_type: str
    requirement: str
    type: str


class CreateMask(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class ClassName(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Actor(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    object_name: str
    object_type: str
    requirement: str
    type: str


class ActivityName(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class EndTime(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    type: str
    type_name: str


class Field01(BaseModel):
    caption: str


class Field15(BaseModel):
    caption: str


class Field21(BaseModel):
    caption: str


class Enum1(BaseModel):
    field_0: Field01 = Field(..., alias='0')
    field_1: Field15 = Field(..., alias='1')
    field_2: Field21 = Field(..., alias='2')
    field_99: Field99 = Field(..., alias='99')


class StatusId(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    enum: Enum1
    group: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class Component(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Observables(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    is_array: bool
    object_name: str
    object_type: str
    requirement: str
    type: str


class TimezoneOffset(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Field02(BaseModel):
    caption: str
    description: str


class Field16(BaseModel):
    caption: str
    description: str


class Field22(BaseModel):
    caption: str
    description: str


class Enum2(BaseModel):
    field_0: Field02 = Field(..., alias='0')
    field_1: Field16 = Field(..., alias='1')
    field_2: Field22 = Field(..., alias='2')
    field_3: Field3 = Field(..., alias='3')
    field_4: Field4 = Field(..., alias='4')
    field_5: Field5 = Field(..., alias='5')
    field_6: Field6 = Field(..., alias='6')
    field_99: Field99 = Field(..., alias='99')


class SeverityId(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    enum: Enum2
    group: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class Attacks(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    is_array: bool
    object_name: str
    object_type: str
    profile: str
    requirement: str
    type: str


class File(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    object_name: str
    object_type: str
    requirement: str
    type: str


class Field1001(BaseModel):
    caption: str
    description: str


class Enum3(BaseModel):
    field_1001: Field1001 = Field(..., alias='1001')


class ClassUid(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    default: int
    description: str
    enum: Enum3
    group: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class Device(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    object_name: str
    object_type: str
    requirement: str
    type: str


class Malware(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    is_array: bool
    object_name: str
    object_type: str
    profile: str
    requirement: str
    type: str


class Field100100(BaseModel):
    caption: str


class Field100101(BaseModel):
    caption: str
    description: str


class Field100102(BaseModel):
    caption: str
    description: str


class Field100103(BaseModel):
    caption: str
    description: str


class Field100104(BaseModel):
    caption: str
    description: str


class Field100105(BaseModel):
    caption: str
    description: str


class Field100106(BaseModel):
    caption: str
    description: str


class Field100107(BaseModel):
    caption: str
    description: str


class Field100108(BaseModel):
    caption: str
    description: str


class Field100109(BaseModel):
    caption: str
    description: str


class Field100110(BaseModel):
    caption: str
    description: str


class Field100111(BaseModel):
    caption: str
    description: str


class Field100112(BaseModel):
    caption: str
    description: str


class Field100113(BaseModel):
    caption: str
    description: str


class Field100114(BaseModel):
    caption: str
    description: str


class Field100199(BaseModel):
    caption: str


class Enum4(BaseModel):
    field_100100: Field100100 = Field(..., alias='100100')
    field_100101: Field100101 = Field(..., alias='100101')
    field_100102: Field100102 = Field(..., alias='100102')
    field_100103: Field100103 = Field(..., alias='100103')
    field_100104: Field100104 = Field(..., alias='100104')
    field_100105: Field100105 = Field(..., alias='100105')
    field_100106: Field100106 = Field(..., alias='100106')
    field_100107: Field100107 = Field(..., alias='100107')
    field_100108: Field100108 = Field(..., alias='100108')
    field_100109: Field100109 = Field(..., alias='100109')
    field_100110: Field100110 = Field(..., alias='100110')
    field_100111: Field100111 = Field(..., alias='100111')
    field_100112: Field100112 = Field(..., alias='100112')
    field_100113: Field100113 = Field(..., alias='100113')
    field_100114: Field100114 = Field(..., alias='100114')
    field_100199: Field100199 = Field(..., alias='100199')


class TypeUid(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    enum: Enum4
    group: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class StatusDetail(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    type: str
    type_name: str


class Field03(BaseModel):
    caption: str


class Field17(BaseModel):
    caption: str


class Field111(BaseModel):
    caption: str


class Field121(BaseModel):
    caption: str


class Field131(BaseModel):
    caption: str


class Field151(BaseModel):
    caption: str


class Field161(BaseModel):
    caption: str


class Field171(BaseModel):
    caption: str


class Field18(BaseModel):
    caption: str
    description: str


class Field23(BaseModel):
    caption: str


class Field32(BaseModel):
    caption: str


class Field42(BaseModel):
    caption: str


class Field52(BaseModel):
    caption: str


class Field62(BaseModel):
    caption: str


class Field81(BaseModel):
    caption: str


class Field91(BaseModel):
    caption: str


class Field993(BaseModel):
    caption: str


class Enum5(BaseModel):
    field_0: Field03 = Field(..., alias='0')
    field_1: Field17 = Field(..., alias='1')
    field_10: Field10 = Field(..., alias='10')
    field_11: Field111 = Field(..., alias='11')
    field_12: Field121 = Field(..., alias='12')
    field_13: Field131 = Field(..., alias='13')
    field_14: Field14 = Field(..., alias='14')
    field_15: Field151 = Field(..., alias='15')
    field_16: Field161 = Field(..., alias='16')
    field_17: Field171 = Field(..., alias='17')
    field_18: Field18 = Field(..., alias='18')
    field_2: Field23 = Field(..., alias='2')
    field_3: Field32 = Field(..., alias='3')
    field_4: Field42 = Field(..., alias='4')
    field_5: Field52 = Field(..., alias='5')
    field_6: Field62 = Field(..., alias='6')
    field_7: Field7 = Field(..., alias='7')
    field_8: Field81 = Field(..., alias='8')
    field_9: Field91 = Field(..., alias='9')
    field_99: Field993 = Field(..., alias='99')


class DispositionId(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    enum: Enum5
    group: str
    profile: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class Field19(BaseModel):
    caption: str
    description: str
    uid: int


class Enum6(BaseModel):
    field_1: Field19 = Field(..., alias='1')


class CategoryUid(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    default: int
    description: str
    enum: Enum6
    group: str
    requirement: str
    sibling: str
    type: str
    type_name: str


class Unmapped(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    object_name: str
    object_type: str
    type: str


class Enrichments(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    is_array: bool
    object_name: str
    object_type: str
    type: str


class Severity(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Duration(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    type: str
    type_name: str


class Message(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class StatusCode(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    type: str
    type_name: str


class Metadata(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    object_name: str
    object_type: str
    requirement: str
    type: str


class RawData(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    type: str
    type_name: str


class StartTime(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    type: str
    type_name: str


class Status(BaseModel):
    field_source: str = Field(..., alias='_source')
    caption: str
    description: str
    group: str
    requirement: str
    type: str
    type_name: str


class Attribute(BaseModel):
    access_mask: Optional[AccessMask] = None
    count: Optional[Count] = None
    category_name: Optional[CategoryName] = None
    type_name: Optional[TypeName] = None
    file_diff: Optional[FileDiff] = None
    time: Optional[Time] = None
    disposition: Optional[Disposition] = None
    connection_uid: Optional[ConnectionUid] = None
    activity_id: Optional[ActivityId] = None
    file_result: Optional[FileResult] = None
    create_mask: Optional[CreateMask] = None
    class_name: Optional[ClassName] = None
    actor: Optional[Actor] = None
    activity_name: Optional[ActivityName] = None
    end_time: Optional[EndTime] = None
    status_id: Optional[StatusId] = None
    component: Optional[Component] = None
    observables: Optional[Observables] = None
    timezone_offset: Optional[TimezoneOffset] = None
    severity_id: Optional[SeverityId] = None
    attacks: Optional[Attacks] = None
    file: Optional[File] = None
    class_uid: Optional[ClassUid] = None
    device: Optional[Device] = None
    malware: Optional[Malware] = None
    type_uid: Optional[TypeUid] = None
    status_detail: Optional[StatusDetail] = None
    disposition_id: Optional[DispositionId] = None
    category_uid: Optional[CategoryUid] = None
    unmapped: Optional[Unmapped] = None
    enrichments: Optional[Enrichments] = None
    severity: Optional[Severity] = None
    duration: Optional[Duration] = None
    message: Optional[Message] = None
    status_code: Optional[StatusCode] = None
    metadata: Optional[Metadata] = None
    raw_data: Optional[RawData] = None
    start_time: Optional[StartTime] = None
    status: Optional[Status] = None


class Model(BaseModel):
    associations: Associations
    attributes: List[Attribute]
    caption: str
    category: str
    category_name: str
    description: str
    extends: str
    name: str
    profiles: List[str]
    uid: int
