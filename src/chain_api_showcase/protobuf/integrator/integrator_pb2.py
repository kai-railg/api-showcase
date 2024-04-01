# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: integrator.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

EventCallback = None
Request = None
Response = None

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10integrator.proto\x12\nIntegrator\x1a\x19google/protobuf/any.proto\"-\n\x07Request\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"r\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\r\"#\n\rEventCallback\x12\x12\n\nevent_name\x18\x01 \x01(\t\"B\n\x13HTTPValidationError\x12+\n\x06\x64\x65tail\x18\x01 \x03(\x0b\x32\x1b.Integrator.ValidationError\"G\n\x06StdRes\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\"9\n\x0fValidationError\x12\x0b\n\x03loc\x18\x01 \x03(\x11\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t2\xb5\x07\n\nIntegrator\x12\x35\n\x06insert\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x34\n\x05\x63lear\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x36\n\x07get_all\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x35\n\x06rotate\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x37\n\x08\x63omplete\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12<\n\rexclusiveZone\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12?\n\x10\x63heck_block_used\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x39\n\nlock_block\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12<\n\rrelease_block\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12=\n\x0eselect_holding\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x34\n\x05telep\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x36\n\x07shuffle\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x34\n\x05start\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12;\n\x0cstart_teleop\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x12\x43\n\x0e\x65vent_callback\x12\x19.Integrator.EventCallback\x1a\x14.Integrator.Response\"\x00\x12\x35\n\x06report\x12\x13.Integrator.Request\x1a\x14.Integrator.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'integrator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=59
  _globals['_REQUEST']._serialized_end=104
  _globals['_RESPONSE']._serialized_start=106
  _globals['_RESPONSE']._serialized_end=220
  _globals['_EVENTCALLBACK']._serialized_start=222
  _globals['_EVENTCALLBACK']._serialized_end=257
  _globals['_HTTPVALIDATIONERROR']._serialized_start=259
  _globals['_HTTPVALIDATIONERROR']._serialized_end=325
  _globals['_STDRES']._serialized_start=327
  _globals['_STDRES']._serialized_end=398
  _globals['_VALIDATIONERROR']._serialized_start=400
  _globals['_VALIDATIONERROR']._serialized_end=457
  _globals['_INTEGRATOR']._serialized_start=460
  _globals['_INTEGRATOR']._serialized_end=1409
# @@protoc_insertion_point(module_scope)
