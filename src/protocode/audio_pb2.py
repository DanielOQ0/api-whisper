# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61udio.proto\x12\x0btranscribir\"\x82\x01\n\x12TranscribirRequest\x12\x0e\n\x06modelo\x18\x01 \x01(\t\x12\x0f\n\x07tamLote\x18\x02 \x01(\x05\x12\x13\n\x0btipoComputo\x18\x03 \x01(\t\x12\x13\n\x0b\x64ispositivo\x18\x04 \x01(\t\x12\r\n\x05\x61udio\x18\x05 \x01(\x0c\x12\x12\n\nfrecuencia\x18\x06 \x01(\x05\"B\n\x10TranscribirReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05texto\x18\x02 \x01(\t\x12\x0e\n\x06tiempo\x18\x03 \x01(\x02\x32_\n\x07Greeter\x12T\n\x10RouteTranscribir\x12\x1f.transcribir.TranscribirRequest\x1a\x1d.transcribir.TranscribirReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRANSCRIBIRREQUEST']._serialized_start=29
  _globals['_TRANSCRIBIRREQUEST']._serialized_end=159
  _globals['_TRANSCRIBIRREPLY']._serialized_start=161
  _globals['_TRANSCRIBIRREPLY']._serialized_end=227
  _globals['_GREETER']._serialized_start=229
  _globals['_GREETER']._serialized_end=324
# @@protoc_insertion_point(module_scope)
