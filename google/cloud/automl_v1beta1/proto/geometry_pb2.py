# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/geometry.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/geometry.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1"
    ),
    serialized_pb=_b(
        '\n0google/cloud/automl_v1beta1/proto/geometry.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"Z\n\x0c\x42oundingPoly\x12J\n\x13normalized_vertices\x18\x02 \x03(\x0b\x32-.google.cloud.automl.v1beta1.NormalizedVertexB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_NORMALIZEDVERTEX = _descriptor.Descriptor(
    name="NormalizedVertex",
    full_name="google.cloud.automl.v1beta1.NormalizedVertex",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="x",
            full_name="google.cloud.automl.v1beta1.NormalizedVertex.x",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="y",
            full_name="google.cloud.automl.v1beta1.NormalizedVertex.y",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    oneofs=[],
    serialized_start=111,
    serialized_end=151,
)


_BOUNDINGPOLY = _descriptor.Descriptor(
    name="BoundingPoly",
    full_name="google.cloud.automl.v1beta1.BoundingPoly",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="normalized_vertices",
            full_name="google.cloud.automl.v1beta1.BoundingPoly.normalized_vertices",
            index=0,
            number=2,
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
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=153,
    serialized_end=243,
)

_BOUNDINGPOLY.fields_by_name["normalized_vertices"].message_type = _NORMALIZEDVERTEX
DESCRIPTOR.message_types_by_name["NormalizedVertex"] = _NORMALIZEDVERTEX
DESCRIPTOR.message_types_by_name["BoundingPoly"] = _BOUNDINGPOLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NormalizedVertex = _reflection.GeneratedProtocolMessageType(
    "NormalizedVertex",
    (_message.Message,),
    dict(
        DESCRIPTOR=_NORMALIZEDVERTEX,
        __module__="google.cloud.automl_v1beta1.proto.geometry_pb2",
        __doc__="""Required. Horizontal coordinate.
  Attributes:
      y:
          Required. Vertical coordinate.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.NormalizedVertex)
    ),
)
_sym_db.RegisterMessage(NormalizedVertex)

BoundingPoly = _reflection.GeneratedProtocolMessageType(
    "BoundingPoly",
    (_message.Message,),
    dict(
        DESCRIPTOR=_BOUNDINGPOLY,
        __module__="google.cloud.automl_v1beta1.proto.geometry_pb2",
        __doc__="""A bounding polygon of a detected object on a plane. On output both
  vertices and normalized\_vertices are provided. The polygon is formed
  by connecting vertices in the order they are listed.
  Attributes:
      normalized_vertices:
          Output only . The bounding polygon normalized vertices.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.BoundingPoly)
    ),
)
_sym_db.RegisterMessage(BoundingPoly)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
