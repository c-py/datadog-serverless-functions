# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trace_payload.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import trace_pb2 as trace__pb2
import span_pb2 as span__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="trace_payload.proto",
    package="pb",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x13trace_payload.proto\x12\x02pb\x1a\x0btrace.proto\x1a\nspan.proto"k\n\x0cTracePayload\x12\x10\n\x08hostName\x18\x01 \x01(\t\x12\x0b\n\x03\x65nv\x18\x02 \x01(\t\x12\x1c\n\x06traces\x18\x03 \x03(\x0b\x32\x0c.pb.APITrace\x12\x1e\n\x0ctransactions\x18\x04 \x03(\x0b\x32\x08.pb.Spanb\x06proto3',
    dependencies=[
        trace__pb2.DESCRIPTOR,
        span__pb2.DESCRIPTOR,
    ],
)


_TRACEPAYLOAD = _descriptor.Descriptor(
    name="TracePayload",
    full_name="pb.TracePayload",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="hostName",
            full_name="pb.TracePayload.hostName",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="env",
            full_name="pb.TracePayload.env",
            index=1,
            number=2,
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
            name="traces",
            full_name="pb.TracePayload.traces",
            index=2,
            number=3,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="transactions",
            full_name="pb.TracePayload.transactions",
            index=3,
            number=4,
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
    serialized_start=52,
    serialized_end=159,
)

_TRACEPAYLOAD.fields_by_name["traces"].message_type = trace__pb2._APITRACE
_TRACEPAYLOAD.fields_by_name["transactions"].message_type = span__pb2._SPAN
DESCRIPTOR.message_types_by_name["TracePayload"] = _TRACEPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TracePayload = _reflection.GeneratedProtocolMessageType(
    "TracePayload",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRACEPAYLOAD,
        "__module__": "trace_payload_pb2"
        # @@protoc_insertion_point(class_scope:pb.TracePayload)
    },
)
_sym_db.RegisterMessage(TracePayload)


# @@protoc_insertion_point(module_scope)
