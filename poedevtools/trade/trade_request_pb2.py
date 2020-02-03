# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scripts/protobuf/source/PoeTrade/trade_request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scripts/protobuf/source/PoeTrade/trade_request.proto',
  package='PoETrade.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n4scripts/protobuf/source/PoeTrade/trade_request.proto\x12\x0ePoETrade.proto\"[\n\x0fPoeTradeRequest\x12$\n\x05query\x18\x01 \x01(\x0b\x32\x15.PoETrade.proto.Query\x12\"\n\x04sort\x18\x06 \x01(\x0b\x32\x14.PoETrade.proto.Sort\"\x9b\x01\n\x05Query\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12&\n\x06status\x18\x03 \x01(\x0b\x32\x16.PoETrade.proto.Status\x12(\n\x07\x66ilters\x18\x04 \x01(\x0b\x32\x17.PoETrade.proto.Filters\x12$\n\x05stats\x18\x05 \x03(\x0b\x32\x15.PoETrade.proto.Stats\"\x18\n\x06Status\x12\x0e\n\x06option\x18\x01 \x01(\t\"B\n\x05Stats\x12\x0c\n\x04type\x18\x01 \x01(\t\x12+\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x1a.PoETrade.proto.StatFilter\"V\n\nStatFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\"\xbd\x01\n\x07\x46ilters\x12:\n\x0eweapon_filters\x18\x01 \x01(\x0b\x32\".PoETrade.proto.WeaponRequirements\x12:\n\x0e\x61rmour_filters\x18\x02 \x01(\x0b\x32\".PoETrade.proto.ArmourRequirements\x12:\n\x0esocket_filters\x18\x03 \x01(\x0b\x32\".PoETrade.proto.SocketRequirements\"V\n\x12WeaponRequirements\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12.\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x1d.PoETrade.proto.WeaponFilters\"V\n\x12\x41rmourRequirements\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12.\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x1d.PoETrade.proto.ArmourFilters\"V\n\x12SocketRequirements\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12.\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x1d.PoETrade.proto.SocketFilters\"k\n\rSocketFilters\x12-\n\x07sockets\x18\x01 \x01(\x0b\x32\x1c.PoETrade.proto.SocketValues\x12+\n\x05links\x18\x02 \x01(\x0b\x32\x1c.PoETrade.proto.SocketValues\"T\n\x0cSocketValues\x12\x0b\n\x03min\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03\x12\t\n\x01r\x18\x03 \x01(\x03\x12\t\n\x01g\x18\x04 \x01(\x03\x12\t\n\x01\x62\x18\x05 \x01(\x03\x12\t\n\x01w\x18\x06 \x01(\x03\"\xb6\x01\n\rArmourFilters\x12\'\n\x02\x61r\x18\x01 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12\'\n\x02\x65s\x18\x02 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12\'\n\x02\x65v\x18\x03 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12*\n\x05\x62lock\x18\x04 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\"\x91\x02\n\rWeaponFilters\x12+\n\x06\x64\x61mage\x18\x01 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12)\n\x04\x63rit\x18\x02 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12(\n\x03\x61ps\x18\x03 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12(\n\x03\x64ps\x18\x04 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12)\n\x04\x65\x64ps\x18\x05 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\x12)\n\x04pdps\x18\x06 \x01(\x0b\x32\x1b.PoETrade.proto.FilterRange\"\'\n\x0b\x46ilterRange\x12\x0b\n\x03min\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03\"\x15\n\x04Sort\x12\r\n\x05price\x18\x01 \x01(\tb\x06proto3'
)




_POETRADEREQUEST = _descriptor.Descriptor(
  name='PoeTradeRequest',
  full_name='PoETrade.proto.PoeTradeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='PoETrade.proto.PoeTradeRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='PoETrade.proto.PoeTradeRequest.sort', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=72,
  serialized_end=163,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='PoETrade.proto.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PoETrade.proto.Query.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='PoETrade.proto.Query.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='PoETrade.proto.Query.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='PoETrade.proto.Query.filters', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='PoETrade.proto.Query.stats', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=166,
  serialized_end=321,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='PoETrade.proto.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='option', full_name='PoETrade.proto.Status.option', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=323,
  serialized_end=347,
)


_STATS = _descriptor.Descriptor(
  name='Stats',
  full_name='PoETrade.proto.Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PoETrade.proto.Stats.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='PoETrade.proto.Stats.filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=349,
  serialized_end=415,
)


_STATFILTER = _descriptor.Descriptor(
  name='StatFilter',
  full_name='PoETrade.proto.StatFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PoETrade.proto.StatFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PoETrade.proto.StatFilter.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='PoETrade.proto.StatFilter.disabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=417,
  serialized_end=503,
)


_FILTERS = _descriptor.Descriptor(
  name='Filters',
  full_name='PoETrade.proto.Filters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weapon_filters', full_name='PoETrade.proto.Filters.weapon_filters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='armour_filters', full_name='PoETrade.proto.Filters.armour_filters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='socket_filters', full_name='PoETrade.proto.Filters.socket_filters', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=506,
  serialized_end=695,
)


_WEAPONREQUIREMENTS = _descriptor.Descriptor(
  name='WeaponRequirements',
  full_name='PoETrade.proto.WeaponRequirements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disabled', full_name='PoETrade.proto.WeaponRequirements.disabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='PoETrade.proto.WeaponRequirements.filters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=697,
  serialized_end=783,
)


_ARMOURREQUIREMENTS = _descriptor.Descriptor(
  name='ArmourRequirements',
  full_name='PoETrade.proto.ArmourRequirements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disabled', full_name='PoETrade.proto.ArmourRequirements.disabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='PoETrade.proto.ArmourRequirements.filters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=785,
  serialized_end=871,
)


_SOCKETREQUIREMENTS = _descriptor.Descriptor(
  name='SocketRequirements',
  full_name='PoETrade.proto.SocketRequirements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disabled', full_name='PoETrade.proto.SocketRequirements.disabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='PoETrade.proto.SocketRequirements.filters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=873,
  serialized_end=959,
)


_SOCKETFILTERS = _descriptor.Descriptor(
  name='SocketFilters',
  full_name='PoETrade.proto.SocketFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sockets', full_name='PoETrade.proto.SocketFilters.sockets', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='links', full_name='PoETrade.proto.SocketFilters.links', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=961,
  serialized_end=1068,
)


_SOCKETVALUES = _descriptor.Descriptor(
  name='SocketValues',
  full_name='PoETrade.proto.SocketValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='PoETrade.proto.SocketValues.min', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='PoETrade.proto.SocketValues.max', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r', full_name='PoETrade.proto.SocketValues.r', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='g', full_name='PoETrade.proto.SocketValues.g', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='PoETrade.proto.SocketValues.b', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='PoETrade.proto.SocketValues.w', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1070,
  serialized_end=1154,
)


_ARMOURFILTERS = _descriptor.Descriptor(
  name='ArmourFilters',
  full_name='PoETrade.proto.ArmourFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ar', full_name='PoETrade.proto.ArmourFilters.ar', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='es', full_name='PoETrade.proto.ArmourFilters.es', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ev', full_name='PoETrade.proto.ArmourFilters.ev', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='PoETrade.proto.ArmourFilters.block', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1157,
  serialized_end=1339,
)


_WEAPONFILTERS = _descriptor.Descriptor(
  name='WeaponFilters',
  full_name='PoETrade.proto.WeaponFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='damage', full_name='PoETrade.proto.WeaponFilters.damage', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crit', full_name='PoETrade.proto.WeaponFilters.crit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aps', full_name='PoETrade.proto.WeaponFilters.aps', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dps', full_name='PoETrade.proto.WeaponFilters.dps', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edps', full_name='PoETrade.proto.WeaponFilters.edps', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pdps', full_name='PoETrade.proto.WeaponFilters.pdps', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1342,
  serialized_end=1615,
)


_FILTERRANGE = _descriptor.Descriptor(
  name='FilterRange',
  full_name='PoETrade.proto.FilterRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='PoETrade.proto.FilterRange.min', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='PoETrade.proto.FilterRange.max', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1617,
  serialized_end=1656,
)


_SORT = _descriptor.Descriptor(
  name='Sort',
  full_name='PoETrade.proto.Sort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='PoETrade.proto.Sort.price', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1658,
  serialized_end=1679,
)

_POETRADEREQUEST.fields_by_name['query'].message_type = _QUERY
_POETRADEREQUEST.fields_by_name['sort'].message_type = _SORT
_QUERY.fields_by_name['status'].message_type = _STATUS
_QUERY.fields_by_name['filters'].message_type = _FILTERS
_QUERY.fields_by_name['stats'].message_type = _STATS
_STATS.fields_by_name['filters'].message_type = _STATFILTER
_STATFILTER.fields_by_name['value'].message_type = _FILTERRANGE
_FILTERS.fields_by_name['weapon_filters'].message_type = _WEAPONREQUIREMENTS
_FILTERS.fields_by_name['armour_filters'].message_type = _ARMOURREQUIREMENTS
_FILTERS.fields_by_name['socket_filters'].message_type = _SOCKETREQUIREMENTS
_WEAPONREQUIREMENTS.fields_by_name['filters'].message_type = _WEAPONFILTERS
_ARMOURREQUIREMENTS.fields_by_name['filters'].message_type = _ARMOURFILTERS
_SOCKETREQUIREMENTS.fields_by_name['filters'].message_type = _SOCKETFILTERS
_SOCKETFILTERS.fields_by_name['sockets'].message_type = _SOCKETVALUES
_SOCKETFILTERS.fields_by_name['links'].message_type = _SOCKETVALUES
_ARMOURFILTERS.fields_by_name['ar'].message_type = _FILTERRANGE
_ARMOURFILTERS.fields_by_name['es'].message_type = _FILTERRANGE
_ARMOURFILTERS.fields_by_name['ev'].message_type = _FILTERRANGE
_ARMOURFILTERS.fields_by_name['block'].message_type = _FILTERRANGE
_WEAPONFILTERS.fields_by_name['damage'].message_type = _FILTERRANGE
_WEAPONFILTERS.fields_by_name['crit'].message_type = _FILTERRANGE
_WEAPONFILTERS.fields_by_name['aps'].message_type = _FILTERRANGE
_WEAPONFILTERS.fields_by_name['dps'].message_type = _FILTERRANGE
_WEAPONFILTERS.fields_by_name['edps'].message_type = _FILTERRANGE
_WEAPONFILTERS.fields_by_name['pdps'].message_type = _FILTERRANGE
DESCRIPTOR.message_types_by_name['PoeTradeRequest'] = _POETRADEREQUEST
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Stats'] = _STATS
DESCRIPTOR.message_types_by_name['StatFilter'] = _STATFILTER
DESCRIPTOR.message_types_by_name['Filters'] = _FILTERS
DESCRIPTOR.message_types_by_name['WeaponRequirements'] = _WEAPONREQUIREMENTS
DESCRIPTOR.message_types_by_name['ArmourRequirements'] = _ARMOURREQUIREMENTS
DESCRIPTOR.message_types_by_name['SocketRequirements'] = _SOCKETREQUIREMENTS
DESCRIPTOR.message_types_by_name['SocketFilters'] = _SOCKETFILTERS
DESCRIPTOR.message_types_by_name['SocketValues'] = _SOCKETVALUES
DESCRIPTOR.message_types_by_name['ArmourFilters'] = _ARMOURFILTERS
DESCRIPTOR.message_types_by_name['WeaponFilters'] = _WEAPONFILTERS
DESCRIPTOR.message_types_by_name['FilterRange'] = _FILTERRANGE
DESCRIPTOR.message_types_by_name['Sort'] = _SORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoeTradeRequest = _reflection.GeneratedProtocolMessageType('PoeTradeRequest', (_message.Message,), {
  'DESCRIPTOR' : _POETRADEREQUEST,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.PoeTradeRequest)
  })
_sym_db.RegisterMessage(PoeTradeRequest)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.Query)
  })
_sym_db.RegisterMessage(Query)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.Status)
  })
_sym_db.RegisterMessage(Status)

Stats = _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {
  'DESCRIPTOR' : _STATS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.Stats)
  })
_sym_db.RegisterMessage(Stats)

StatFilter = _reflection.GeneratedProtocolMessageType('StatFilter', (_message.Message,), {
  'DESCRIPTOR' : _STATFILTER,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.StatFilter)
  })
_sym_db.RegisterMessage(StatFilter)

Filters = _reflection.GeneratedProtocolMessageType('Filters', (_message.Message,), {
  'DESCRIPTOR' : _FILTERS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.Filters)
  })
_sym_db.RegisterMessage(Filters)

WeaponRequirements = _reflection.GeneratedProtocolMessageType('WeaponRequirements', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONREQUIREMENTS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.WeaponRequirements)
  })
_sym_db.RegisterMessage(WeaponRequirements)

ArmourRequirements = _reflection.GeneratedProtocolMessageType('ArmourRequirements', (_message.Message,), {
  'DESCRIPTOR' : _ARMOURREQUIREMENTS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.ArmourRequirements)
  })
_sym_db.RegisterMessage(ArmourRequirements)

SocketRequirements = _reflection.GeneratedProtocolMessageType('SocketRequirements', (_message.Message,), {
  'DESCRIPTOR' : _SOCKETREQUIREMENTS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.SocketRequirements)
  })
_sym_db.RegisterMessage(SocketRequirements)

SocketFilters = _reflection.GeneratedProtocolMessageType('SocketFilters', (_message.Message,), {
  'DESCRIPTOR' : _SOCKETFILTERS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.SocketFilters)
  })
_sym_db.RegisterMessage(SocketFilters)

SocketValues = _reflection.GeneratedProtocolMessageType('SocketValues', (_message.Message,), {
  'DESCRIPTOR' : _SOCKETVALUES,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.SocketValues)
  })
_sym_db.RegisterMessage(SocketValues)

ArmourFilters = _reflection.GeneratedProtocolMessageType('ArmourFilters', (_message.Message,), {
  'DESCRIPTOR' : _ARMOURFILTERS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.ArmourFilters)
  })
_sym_db.RegisterMessage(ArmourFilters)

WeaponFilters = _reflection.GeneratedProtocolMessageType('WeaponFilters', (_message.Message,), {
  'DESCRIPTOR' : _WEAPONFILTERS,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.WeaponFilters)
  })
_sym_db.RegisterMessage(WeaponFilters)

FilterRange = _reflection.GeneratedProtocolMessageType('FilterRange', (_message.Message,), {
  'DESCRIPTOR' : _FILTERRANGE,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.FilterRange)
  })
_sym_db.RegisterMessage(FilterRange)

Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), {
  'DESCRIPTOR' : _SORT,
  '__module__' : 'scripts.protobuf.source.PoeTrade.trade_request_pb2'
  # @@protoc_insertion_point(class_scope:PoETrade.proto.Sort)
  })
_sym_db.RegisterMessage(Sort)


# @@protoc_insertion_point(module_scope)
