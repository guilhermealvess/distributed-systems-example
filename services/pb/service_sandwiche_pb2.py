# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service-sandwiche.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service-sandwiche.proto',
  package='sandwicheService',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17service-sandwiche.proto\x12\x10sandwicheService\"b\n\tSandwiche\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x01\x12\x17\n\x0fpreparationTime\x18\x04 \x01(\x03\x12\x13\n\x0bingredients\x18\x05 \x03(\t\"I\n\x16\x46indSandwichesResponse\x12/\n\nsandwiches\x18\x01 \x03(\x0b\x32\x1b.sandwicheService.Sandwiche\",\n\x15\x46indSandwichesRequest\x12\x13\n\x0btableNumber\x18\x01 \x01(\x05\"\x1a\n\x0cOrderRequest\x12\n\n\x02id\x18\x01 \x03(\t\"7\n\rOrderResponse\x12\r\n\x05\x66oods\x18\x01 \x03(\t\x12\x17\n\x0fpreparationTime\x18\x02 \x01(\x03\x32\xca\x01\n\x10SandwicheService\x12\x65\n\x0e\x46indSandwiches\x12\'.sandwicheService.FindSandwichesRequest\x1a(.sandwicheService.FindSandwichesResponse\"\x00\x12O\n\x0c\x45xecuteOrder\x12\x1e.sandwicheService.OrderRequest\x1a\x1f.sandwicheService.OrderResponseb\x06proto3'
)




_SANDWICHE = _descriptor.Descriptor(
  name='Sandwiche',
  full_name='sandwicheService.Sandwiche',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sandwicheService.Sandwiche.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='sandwicheService.Sandwiche.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='sandwicheService.Sandwiche.price', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preparationTime', full_name='sandwicheService.Sandwiche.preparationTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ingredients', full_name='sandwicheService.Sandwiche.ingredients', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=143,
)


_FINDSANDWICHESRESPONSE = _descriptor.Descriptor(
  name='FindSandwichesResponse',
  full_name='sandwicheService.FindSandwichesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sandwiches', full_name='sandwicheService.FindSandwichesResponse.sandwiches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=218,
)


_FINDSANDWICHESREQUEST = _descriptor.Descriptor(
  name='FindSandwichesRequest',
  full_name='sandwicheService.FindSandwichesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tableNumber', full_name='sandwicheService.FindSandwichesRequest.tableNumber', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=264,
)


_ORDERREQUEST = _descriptor.Descriptor(
  name='OrderRequest',
  full_name='sandwicheService.OrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sandwicheService.OrderRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=292,
)


_ORDERRESPONSE = _descriptor.Descriptor(
  name='OrderResponse',
  full_name='sandwicheService.OrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='foods', full_name='sandwicheService.OrderResponse.foods', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preparationTime', full_name='sandwicheService.OrderResponse.preparationTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=349,
)

_FINDSANDWICHESRESPONSE.fields_by_name['sandwiches'].message_type = _SANDWICHE
DESCRIPTOR.message_types_by_name['Sandwiche'] = _SANDWICHE
DESCRIPTOR.message_types_by_name['FindSandwichesResponse'] = _FINDSANDWICHESRESPONSE
DESCRIPTOR.message_types_by_name['FindSandwichesRequest'] = _FINDSANDWICHESREQUEST
DESCRIPTOR.message_types_by_name['OrderRequest'] = _ORDERREQUEST
DESCRIPTOR.message_types_by_name['OrderResponse'] = _ORDERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sandwiche = _reflection.GeneratedProtocolMessageType('Sandwiche', (_message.Message,), {
  'DESCRIPTOR' : _SANDWICHE,
  '__module__' : 'service_sandwiche_pb2'
  # @@protoc_insertion_point(class_scope:sandwicheService.Sandwiche)
  })
_sym_db.RegisterMessage(Sandwiche)

FindSandwichesResponse = _reflection.GeneratedProtocolMessageType('FindSandwichesResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDSANDWICHESRESPONSE,
  '__module__' : 'service_sandwiche_pb2'
  # @@protoc_insertion_point(class_scope:sandwicheService.FindSandwichesResponse)
  })
_sym_db.RegisterMessage(FindSandwichesResponse)

FindSandwichesRequest = _reflection.GeneratedProtocolMessageType('FindSandwichesRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDSANDWICHESREQUEST,
  '__module__' : 'service_sandwiche_pb2'
  # @@protoc_insertion_point(class_scope:sandwicheService.FindSandwichesRequest)
  })
_sym_db.RegisterMessage(FindSandwichesRequest)

OrderRequest = _reflection.GeneratedProtocolMessageType('OrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERREQUEST,
  '__module__' : 'service_sandwiche_pb2'
  # @@protoc_insertion_point(class_scope:sandwicheService.OrderRequest)
  })
_sym_db.RegisterMessage(OrderRequest)

OrderResponse = _reflection.GeneratedProtocolMessageType('OrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERRESPONSE,
  '__module__' : 'service_sandwiche_pb2'
  # @@protoc_insertion_point(class_scope:sandwicheService.OrderResponse)
  })
_sym_db.RegisterMessage(OrderResponse)



_SANDWICHESERVICE = _descriptor.ServiceDescriptor(
  name='SandwicheService',
  full_name='sandwicheService.SandwicheService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=352,
  serialized_end=554,
  methods=[
  _descriptor.MethodDescriptor(
    name='FindSandwiches',
    full_name='sandwicheService.SandwicheService.FindSandwiches',
    index=0,
    containing_service=None,
    input_type=_FINDSANDWICHESREQUEST,
    output_type=_FINDSANDWICHESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteOrder',
    full_name='sandwicheService.SandwicheService.ExecuteOrder',
    index=1,
    containing_service=None,
    input_type=_ORDERREQUEST,
    output_type=_ORDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SANDWICHESERVICE)

DESCRIPTOR.services_by_name['SandwicheService'] = _SANDWICHESERVICE

# @@protoc_insertion_point(module_scope)
