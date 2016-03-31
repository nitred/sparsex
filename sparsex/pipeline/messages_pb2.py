# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='sparsex',
  serialized_pb='\n\x0emessages.proto\x12\x07sparsex\"\xe8\x03\n\x07Request\x12\x41\n\x0crequest_type\x18\x01 \x02(\x0e\x32\x1c.sparsex.Request.RequestType:\rEMPTY_REQUEST\x12\x42\n\ninput_type\x18\x02 \x01(\x0e\x32\x1a.sparsex.Request.InputType:\x12UNKNOWN_INPUT_TYPE\x12?\n\tdata_type\x18\x03 \x01(\x0e\x32\x19.sparsex.Request.DataType:\x11UNKNOWN_DATA_TYPE\x12\x12\n\ndata_shape\x18\x04 \x03(\x03\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\x15\n\rdata_checksum\x18\x06 \x01(\t\"U\n\x0bRequestType\x12\x11\n\rEMPTY_REQUEST\x10\x00\x12\x0c\n\x08SHUTDOWN\x10\x01\x12\x10\n\x0cGET_FEATURES\x10\x02\x12\x13\n\x0fGET_PREDICTIONS\x10\x03\"?\n\tInputType\x12\x16\n\x12UNKNOWN_INPUT_TYPE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x0f\n\x0bIMAGE_ARRAY\x10\x02\"D\n\x08\x44\x61taType\x12\x15\n\x11UNKNOWN_DATA_TYPE\x10\x00\x12\t\n\x05UINT8\x10\x01\x12\t\n\x05INT64\x10\x02\x12\x0b\n\x07\x46LOAT64\x10\x03\"\x89\x03\n\x08Response\x12\x45\n\rresponse_type\x18\x01 \x02(\x0e\x32\x1e.sparsex.Response.ResponseType:\x0e\x45MPTY_RESPONSE\x12@\n\tdata_type\x18\x02 \x01(\x0e\x32\x1a.sparsex.Response.DataType:\x11UNKNOWN_DATA_TYPE\x12\x12\n\ndata_shape\x18\x03 \x03(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x10\n\x08\x63hecksum\x18\x05 \x01(\t\x12\x1e\n\x16\x61\x64\x64itional_information\x18\x06 \x01(\t\"Z\n\x0cResponseType\x12\x12\n\x0e\x45MPTY_RESPONSE\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0c\n\x08SHUTDOWN\x10\x02\x12\x0c\n\x08\x46\x45\x41TURES\x10\x03\x12\x0f\n\x0bPREDICTIONS\x10\x04\"D\n\x08\x44\x61taType\x12\x15\n\x11UNKNOWN_DATA_TYPE\x10\x00\x12\t\n\x05UINT8\x10\x01\x12\t\n\x05INT64\x10\x02\x12\x0b\n\x07\x46LOAT64\x10\x03')



_REQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='sparsex.Request.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMPTY_REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FEATURES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PREDICTIONS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=296,
  serialized_end=381,
)

_REQUEST_INPUTTYPE = _descriptor.EnumDescriptor(
  name='InputType',
  full_name='sparsex.Request.InputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_INPUT_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_ARRAY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=383,
  serialized_end=446,
)

_REQUEST_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='sparsex.Request.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DATA_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT64', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=448,
  serialized_end=516,
)

_RESPONSE_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='sparsex.Response.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMPTY_RESPONSE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDICTIONS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=752,
  serialized_end=842,
)

_RESPONSE_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='sparsex.Response.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DATA_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT64', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=448,
  serialized_end=516,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='sparsex.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='sparsex.Request.request_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_type', full_name='sparsex.Request.input_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='sparsex.Request.data_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_shape', full_name='sparsex.Request.data_shape', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='sparsex.Request.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_checksum', full_name='sparsex.Request.data_checksum', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_REQUESTTYPE,
    _REQUEST_INPUTTYPE,
    _REQUEST_DATATYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=28,
  serialized_end=516,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='sparsex.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_type', full_name='sparsex.Response.response_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='sparsex.Response.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_shape', full_name='sparsex.Response.data_shape', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='sparsex.Response.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='sparsex.Response.checksum', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_information', full_name='sparsex.Response.additional_information', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSE_RESPONSETYPE,
    _RESPONSE_DATATYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=519,
  serialized_end=912,
)

_REQUEST.fields_by_name['request_type'].enum_type = _REQUEST_REQUESTTYPE
_REQUEST.fields_by_name['input_type'].enum_type = _REQUEST_INPUTTYPE
_REQUEST.fields_by_name['data_type'].enum_type = _REQUEST_DATATYPE
_REQUEST_REQUESTTYPE.containing_type = _REQUEST;
_REQUEST_INPUTTYPE.containing_type = _REQUEST;
_REQUEST_DATATYPE.containing_type = _REQUEST;
_RESPONSE.fields_by_name['response_type'].enum_type = _RESPONSE_RESPONSETYPE
_RESPONSE.fields_by_name['data_type'].enum_type = _RESPONSE_DATATYPE
_RESPONSE_RESPONSETYPE.containing_type = _RESPONSE;
_RESPONSE_DATATYPE.containing_type = _RESPONSE;
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:sparsex.Request)

class Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE

  # @@protoc_insertion_point(class_scope:sparsex.Response)


# @@protoc_insertion_point(module_scope)
