# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/data_types.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/data_types.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1",
    serialized_pb=b'\n2google/cloud/automl_v1beta1/proto/data_types.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto"\xfc\x01\n\x08\x44\x61taType\x12\x42\n\x11list_element_type\x18\x02 \x01(\x0b\x32%.google.cloud.automl.v1beta1.DataTypeH\x00\x12>\n\x0bstruct_type\x18\x03 \x01(\x0b\x32\'.google.cloud.automl.v1beta1.StructTypeH\x00\x12\x15\n\x0btime_format\x18\x05 \x01(\tH\x00\x12\x38\n\ttype_code\x18\x01 \x01(\x0e\x32%.google.cloud.automl.v1beta1.TypeCode\x12\x10\n\x08nullable\x18\x04 \x01(\x08\x42\t\n\x07\x64\x65tails"\xa7\x01\n\nStructType\x12\x43\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x33.google.cloud.automl.v1beta1.StructType.FieldsEntry\x1aT\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.google.cloud.automl.v1beta1.DataType:\x02\x38\x01*r\n\x08TypeCode\x12\x19\n\x15TYPE_CODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x46LOAT64\x10\x03\x12\r\n\tTIMESTAMP\x10\x04\x12\n\n\x06STRING\x10\x06\x12\t\n\x05\x41RRAY\x10\x08\x12\n\n\x06STRUCT\x10\t\x12\x0c\n\x08\x43\x41TEGORY\x10\nB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3',
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)

_TYPECODE = _descriptor.EnumDescriptor(
    name="TypeCode",
    full_name="google.cloud.automl.v1beta1.TypeCode",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="TYPE_CODE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FLOAT64", index=1, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TIMESTAMP", index=2, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="STRING", index=3, number=6, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ARRAY", index=4, number=8, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="STRUCT", index=5, number=9, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CATEGORY", index=6, number=10, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=538,
    serialized_end=652,
)
_sym_db.RegisterEnumDescriptor(_TYPECODE)

TypeCode = enum_type_wrapper.EnumTypeWrapper(_TYPECODE)
TYPE_CODE_UNSPECIFIED = 0
FLOAT64 = 3
TIMESTAMP = 4
STRING = 6
ARRAY = 8
STRUCT = 9
CATEGORY = 10


_DATATYPE = _descriptor.Descriptor(
    name="DataType",
    full_name="google.cloud.automl.v1beta1.DataType",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="list_element_type",
            full_name="google.cloud.automl.v1beta1.DataType.list_element_type",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="struct_type",
            full_name="google.cloud.automl.v1beta1.DataType.struct_type",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="time_format",
            full_name="google.cloud.automl.v1beta1.DataType.time_format",
            index=2,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="type_code",
            full_name="google.cloud.automl.v1beta1.DataType.type_code",
            index=3,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="nullable",
            full_name="google.cloud.automl.v1beta1.DataType.nullable",
            index=4,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="details",
            full_name="google.cloud.automl.v1beta1.DataType.details",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=114,
    serialized_end=366,
)


_STRUCTTYPE_FIELDSENTRY = _descriptor.Descriptor(
    name="FieldsEntry",
    full_name="google.cloud.automl.v1beta1.StructType.FieldsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1beta1.StructType.FieldsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1beta1.StructType.FieldsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=452,
    serialized_end=536,
)

_STRUCTTYPE = _descriptor.Descriptor(
    name="StructType",
    full_name="google.cloud.automl.v1beta1.StructType",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="fields",
            full_name="google.cloud.automl.v1beta1.StructType.fields",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_STRUCTTYPE_FIELDSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=369,
    serialized_end=536,
)

_DATATYPE.fields_by_name["list_element_type"].message_type = _DATATYPE
_DATATYPE.fields_by_name["struct_type"].message_type = _STRUCTTYPE
_DATATYPE.fields_by_name["type_code"].enum_type = _TYPECODE
_DATATYPE.oneofs_by_name["details"].fields.append(
    _DATATYPE.fields_by_name["list_element_type"]
)
_DATATYPE.fields_by_name[
    "list_element_type"
].containing_oneof = _DATATYPE.oneofs_by_name["details"]
_DATATYPE.oneofs_by_name["details"].fields.append(
    _DATATYPE.fields_by_name["struct_type"]
)
_DATATYPE.fields_by_name["struct_type"].containing_oneof = _DATATYPE.oneofs_by_name[
    "details"
]
_DATATYPE.oneofs_by_name["details"].fields.append(
    _DATATYPE.fields_by_name["time_format"]
)
_DATATYPE.fields_by_name["time_format"].containing_oneof = _DATATYPE.oneofs_by_name[
    "details"
]
_STRUCTTYPE_FIELDSENTRY.fields_by_name["value"].message_type = _DATATYPE
_STRUCTTYPE_FIELDSENTRY.containing_type = _STRUCTTYPE
_STRUCTTYPE.fields_by_name["fields"].message_type = _STRUCTTYPE_FIELDSENTRY
DESCRIPTOR.message_types_by_name["DataType"] = _DATATYPE
DESCRIPTOR.message_types_by_name["StructType"] = _STRUCTTYPE
DESCRIPTOR.enum_types_by_name["TypeCode"] = _TYPECODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataType = _reflection.GeneratedProtocolMessageType(
    "DataType",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATATYPE,
        "__module__": "google.cloud.automl_v1beta1.proto.data_types_pb2",
        "__doc__": """Indicated the type of data that can be stored in a
  structured data entity (e.g. a table).
  
  
  Attributes:
      details:
          Details of DataType-s that need additional specification.
      list_element_type:
          If [type_code][google.cloud.automl.v1beta1.DataType.type_code]
          == [ARRAY][google.cloud.automl.v1beta1.TypeCode.ARRAY], then
          ``list_element_type`` is the type of the elements.
      struct_type:
          If [type_code][google.cloud.automl.v1beta1.DataType.type_code]
          == [STRUCT][google.cloud.automl.v1beta1.TypeCode.STRUCT], then
          ``struct_type`` provides type information for the struct’s
          fields.
      time_format:
          If [type_code][google.cloud.automl.v1beta1.DataType.type_code]
          == [TIMESTAMP][google.cloud.automl.v1beta1.TypeCode.TIMESTAMP]
          then ``time_format`` provides the format in which that time
          field is expressed. The time_format must either be one of: \*
          ``UNIX_SECONDS`` \* ``UNIX_MILLISECONDS`` \*
          ``UNIX_MICROSECONDS`` \* ``UNIX_NANOSECONDS`` (for
          respectively number of seconds, milliseconds, microseconds and
          nanoseconds since start of the Unix epoch); or be written in
          ``strftime`` syntax. If time_format is not set, then the
          default format as described on the type_code is used.
      type_code:
          Required. The [TypeCode][google.cloud.automl.v1beta1.TypeCode]
          for this type.
      nullable:
          If true, this DataType can also be ``NULL``. In .CSV files
          ``NULL`` value is expressed as an empty string.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.DataType)
    },
)
_sym_db.RegisterMessage(DataType)

StructType = _reflection.GeneratedProtocolMessageType(
    "StructType",
    (_message.Message,),
    {
        "FieldsEntry": _reflection.GeneratedProtocolMessageType(
            "FieldsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _STRUCTTYPE_FIELDSENTRY,
                "__module__": "google.cloud.automl_v1beta1.proto.data_types_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.StructType.FieldsEntry)
            },
        ),
        "DESCRIPTOR": _STRUCTTYPE,
        "__module__": "google.cloud.automl_v1beta1.proto.data_types_pb2",
        "__doc__": """\ ``StructType`` defines the DataType-s of a
  [STRUCT][google.cloud.automl.v1beta1.TypeCode.STRUCT] type.
  
  
  Attributes:
      fields:
          Unordered map of struct field names to their data types.
          Fields cannot be added or removed via Update. Their names and
          data types are still mutable.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.StructType)
    },
)
_sym_db.RegisterMessage(StructType)
_sym_db.RegisterMessage(StructType.FieldsEntry)


DESCRIPTOR._options = None
_STRUCTTYPE_FIELDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
