# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/text_segment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/text_segment.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=b"\n\032com.google.cloud.automl.v1B\020TextSegmentProtoP\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/google/cloud/automl_v1/proto/text_segment.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto"H\n\x0bTextSegment\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x14\n\x0cstart_offset\x18\x01 \x01(\x03\x12\x12\n\nend_offset\x18\x02 \x01(\x03\x42\xbc\x01\n\x1a\x63om.google.cloud.automl.v1B\x10TextSegmentProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3',
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,],
)


_TEXTSEGMENT = _descriptor.Descriptor(
    name="TextSegment",
    full_name="google.cloud.automl.v1.TextSegment",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="google.cloud.automl.v1.TextSegment.content",
            index=0,
            number=3,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="start_offset",
            full_name="google.cloud.automl.v1.TextSegment.start_offset",
            index=1,
            number=1,
            type=3,
            cpp_type=2,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="end_offset",
            full_name="google.cloud.automl.v1.TextSegment.end_offset",
            index=2,
            number=2,
            type=3,
            cpp_type=2,
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=177,
)

DESCRIPTOR.message_types_by_name["TextSegment"] = _TEXTSEGMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextSegment = _reflection.GeneratedProtocolMessageType(
    "TextSegment",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTSEGMENT,
        "__module__": "google.cloud.automl_v1.proto.text_segment_pb2",
        "__doc__": """A contiguous part of a text (string), assuming it has an UTF-8 NFC
  encoding.
  
  Attributes:
      content:
          Output only. The content of the TextSegment.
      start_offset:
          Required. Zero-based character index of the first character of
          the text segment (counting characters from the beginning of
          the text).
      end_offset:
          Required. Zero-based character index of the first character
          past the end of the text segment (counting character from the
          beginning of the text). The character at the end_offset is NOT
          included in the text segment.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.TextSegment)
    },
)
_sym_db.RegisterMessage(TextSegment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
