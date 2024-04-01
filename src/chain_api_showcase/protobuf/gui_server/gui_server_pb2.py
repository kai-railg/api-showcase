# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gui_server.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

UpdateGroupInSchema = None
DelVesselSchemas = None
SetGhostVehicleCancelPost = None
ContainerSteupSchemas = None
CreatePermissionInSchema = None
GetAllMessageSchemas = None
GetAllMessageCSVSchemas = None
LoadFirstInSchema = None
RedoTaskInSchema = None
CreateGroupInSchema = None
UpdateTaskSchema = None
UpdatePileInfoSchemas = None
LoginInSchema = None
FailTaskSchemas = None
Request = None
EventReport = None
SetVesselSchemas = None
UpdatePermissionInSchema = None
UpdateUserInSchema = None
CRUDTwistlockStation = None
UpdateALlInfoSchemas = None
UpdatePasswdInSchema = None
SetSwitchRequest = None
CreateUserInSchema = None
ForceOvertakeSchemas = None
Response = None

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10gui_server.proto\x12\nGui_Server\x1a\x19google/protobuf/any.proto\"-\n\x07Request\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"r\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\r\"4\n#BodyDenmarkinfoImportContainersPost\x12\r\n\x05\x66iles\x18\x01 \x03(\x0c\",\n\x1b\x42odyFileTransportUploadPost\x12\r\n\x05\x66iles\x18\x01 \x03(\x0c\"\xe3\x01\n\x14\x43RUDTwistlockStation\x12\x0f\n\x07ts_name\x18\x01 \x01(\t\x12\x12\n\ntime_stamp\x18\x02 \x01(\t\x12\x12\n\nts_creator\x18\x03 \x01(\t\x12\x11\n\tts_vessel\x18\x04 \x01(\t\x12\x10\n\x08job_type\x18\x05 \x01(\t\x12\x0f\n\x07ts_lane\x18\x06 \x01(\t\x12\r\n\x05ts_qc\x18\x07 \x01(\t\x12\x12\n\nts_bollard\x18\x08 \x01(\t\x12\x13\n\x0bts_offset_x\x18\t \x01(\x02\x12\x11\n\tts_reason\x18\n \x01(\t\x12\x11\n\tts_status\x18\x0b \x01(\t\"\xa4\x01\n\x15\x43ontainerSteupSchemas\x12\x12\n\ntime_stamp\x18\x01 \x01(\t\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x12\n\nvehicle_id\x18\x03 \x01(\t\x12\x11\n\tunique_id\x18\x04 \x01(\t\x12\x0e\n\x06number\x18\x05 \x01(\t\x12(\n\ncontainers\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\"Q\n\x13\x43reateGroupInSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x17\n\x0fpermission_list\x18\x03 \x03(\x11\"\x86\x01\n\x18\x43reatePermissionInSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0b\x62\x65long_type\x18\x03 \x01(\t\x12\x14\n\x0crequest_type\x18\x04 \x01(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x0e\n\x06method\x18\x06 \x01(\t\"c\n\x13\x43reateSuccessSchema\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"\xdc\x01\n\x12\x43reateUserInSchema\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\x12\x12\n\ndepartment\x18\x06 \x01(\t\x12\x10\n\x08group_id\x18\x07 \x01(\x11\x12\x11\n\tquestion1\x18\x08 \x01(\t\x12\x11\n\tquestion2\x18\t \x01(\t\x12\x0f\n\x07\x61nswer1\x18\n \x01(\t\x12\x0f\n\x07\x61nswer2\x18\x0b \x01(\t\"\x81\x01\n\x13\x43urrentUserGroupOut\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12;\n\x0bpermissions\x18\x04 \x03(\x0b\x32&.Gui_Server.CurrentUserGroupPermission\"Y\n\x1a\x43urrentUserGroupPermission\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x62\x65long_type\x18\x04 \x01(\t\"=\n\x10\x44\x65lVesselSchemas\x12\x15\n\rvesselVisitId\x18\x01 \x01(\t\x12\x12\n\nvesselName\x18\x02 \x01(\t\"c\n\x13\x44\x65leteSuccessSchema\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"\xca\x01\n\x0b\x45ventReport\x12\x11\n\tvehicleID\x18\x01 \x01(\t\x12\x11\n\teventType\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\x11\n\ttimeStamp\x18\x04 \x01(\t\x12/\n\x04\x64\x61ta\x18\x05 \x03(\x0b\x32!.Gui_Server.EventReport.DataEntry\x1a\x41\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"n\n\x0f\x46\x61ilTaskSchemas\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x13\n\x0b\x66rom_server\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x11\"<\n\x14\x46orceOvertakeSchemas\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x10\n\x08overtake\x18\x02 \x01(\x11\"\x9e\x01\n\x17GetAllMessageCSVSchemas\x12\x12\n\nstart_time\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\t\x12\x13\n\x0bmessageType\x18\x03 \x01(\t\x12(\n\ntruck_list\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08per_page\x18\x05 \x01(\x11\x12\x0c\n\x04page\x18\x06 \x01(\x11\"\xaa\x01\n\x14GetAllMessageSchemas\x12\x12\n\nstart_time\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\t\x12\x13\n\x0bmessageType\x18\x03 \x01(\t\x12(\n\ntruck_list\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08per_page\x18\x05 \x01(\x11\x12\r\n\x05level\x18\x06 \x01(\x11\x12\x0c\n\x04page\x18\x07 \x01(\x11\"\x88\x01\n\x14GetGroupAllOutSchema\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.Gui_Server.UpdateGroupOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x11\x12\r\n\x05pages\x18\x06 \x01(\x11\"\x99\x01\n\x0bGetGroupOut\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x12\n\ndepartment\x18\x05 \x01(\t\x12.\n\x05group\x18\x06 \x01(\x0b\x32\x1f.Gui_Server.CurrentUserGroupOut\"d\n\x11GetGroupOutSchema\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.Gui_Server.GetGroupOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"\x92\x01\n\x19GetPermissionAllOutSchema\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1f.Gui_Server.UpdatePermissionOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x11\x12\r\n\x05pages\x18\x06 \x01(\x11\"\x93\x01\n\x1aGetPermissionListOutSchema\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1f.Gui_Server.UpdatePermissionOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x11\x12\r\n\x05pages\x18\x06 \x01(\x11\"q\n\x16GetPermissionOutSchema\x12-\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1f.Gui_Server.UpdatePermissionOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"\xcd\x01\n\nGetSelfOut\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05super\x18\x03 \x01(\x08\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\x12\x12\n\ndepartment\x18\x06 \x01(\t\x12\x12\n\nlast_login\x18\x07 \x01(\t\x12\x13\n\x0blast_logout\x18\x08 \x01(\t\x12.\n\x05group\x18\t \x01(\x0b\x32\x1f.Gui_Server.GetSelfOutWithGroup\"8\n\x10GetSelfOutSchema\x12$\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x16.Gui_Server.GetSelfOut\"\x84\x01\n\x13GetSelfOutWithGroup\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12>\n\x0bpermissions\x18\x04 \x03(\x0b\x32).Gui_Server.GetSelfOutWithGroupPermission\"\\\n\x1dGetSelfOutWithGroupPermission\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x62\x65long_type\x18\x04 \x01(\t\"\x87\x01\n\x13GetUserAllOutSchema\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.Gui_Server.GetUserListOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x11\x12\r\n\x05pages\x18\x06 \x01(\x11\"\xde\x01\n\x0eGetUserListOut\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x12\n\ndepartment\x18\x05 \x01(\t\x12\x16\n\x0eis_first_login\x18\x06 \x01(\x08\x12\x32\n\x05group\x18\x07 \x01(\x0b\x32#.Gui_Server.GetUserListOutWithGroup\x12\x12\n\nlast_login\x18\x08 \x01(\t\x12\x13\n\x0blast_logout\x18\t \x01(\t\"\x88\x01\n\x14GetUserListOutSchema\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.Gui_Server.GetUserListOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x11\x12\r\n\x05pages\x18\x06 \x01(\x11\"H\n\x17GetUserListOutWithGroup\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\xe9\x02\n\nGetUserOut\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\ndepartment\x18\x04 \x01(\t\x12\x12\n\nfirst_name\x18\x05 \x01(\t\x12\x11\n\tlast_name\x18\x06 \x01(\t\x12\x10\n\x08group_id\x18\x07 \x01(\x11\x12\x11\n\tis_active\x18\x08 \x01(\x08\x12\x12\n\nlast_login\x18\t \x01(\t\x12\x13\n\x0blast_logout\x18\n \x01(\t\x12\x11\n\tcreate_id\x18\x0b \x01(\x11\x12\x11\n\tupdate_id\x18\x0c \x01(\x11\x12\x13\n\x0b\x63reate_time\x18\r \x01(\t\x12\x13\n\x0bupdate_time\x18\x0e \x01(\t\x12\x16\n\x0eis_first_login\x18\x0f \x01(\x08\x12\r\n\x05super\x18\x10 \x01(\x08\x12.\n\x05group\x18\x11 \x01(\x0b\x32\x1f.Gui_Server.CurrentUserGroupOut\"b\n\x10GetUserOutSchema\x12$\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x16.Gui_Server.GetUserOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"B\n\x13HTTPValidationError\x12+\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x1b.Gui_Server.ValidationError\"L\n\x11LoadFirstInSchema\x12\x11\n\tvehicleID\x18\x01 \x01(\t\x12\x14\n\x0covertakeLane\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\"3\n\rLoginInSchema\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"5\n\x10RedoTaskInSchema\x12\x11\n\tvehicleID\x18\x01 \x01(\t\x12\x0e\n\x06origin\x18\x02 \x01(\t\"F\n\x19SetGhostVehicleCancelPost\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x15\n\rmanual_cancel\x18\x02 \x01(\x08\"O\n\x10SetSwitchRequest\x12\x17\n\x0fswitch_val_name\x18\x01 \x01(\t\x12\x12\n\nswitch_val\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\"\xa0\x02\n\x10SetVesselSchemas\x12\x15\n\rvesselVisitId\x18\x01 \x01(\t\x12\x12\n\nvesselName\x18\x02 \x01(\t\x12\r\n\x05inVyg\x18\x03 \x01(\t\x12\x0e\n\x06outVyg\x18\x04 \x01(\t\x12\x13\n\x0b\x62ollardFore\x18\x05 \x01(\x11\x12\x14\n\x0c\x62ollardAfter\x18\x06 \x01(\x11\x12\x13\n\x0bvessel_type\x18\x07 \x01(\t\x12%\n\x07\x61t_list\x18\x08 \x03(\x0b\x32\x14.google.protobuf.Any\x12\"\n\x04QCAG\x18\t \x03(\x0b\x32\x14.google.protobuf.Any\x12\x0b\n\x03\x45TA\x18\n \x01(\t\x12\x0b\n\x03\x45TB\x18\x0b \x01(\t\x12\x0b\n\x03\x45TD\x18\x0c \x01(\t\x12\x10\n\x08rta_time\x18\r \x01(\t\"2\n\x14UpdateALlInfoSchemas\x12\x1a\n\x12pile_info_all_code\x18\x01 \x01(\x11\"Q\n\x13UpdateGroupInSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x17\n\x0fpermission_list\x18\x03 \x03(\x11\"z\n\x0eUpdateGroupOut\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x39\n\x0bpermissions\x18\x04 \x03(\x0b\x32$.Gui_Server.UpdateGroupOutPermission\"W\n\x18UpdateGroupOutPermission\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x62\x65long_type\x18\x04 \x01(\t\"j\n\x14UpdateGroupOutSchema\x12(\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1a.Gui_Server.UpdateGroupOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"B\n\x14UpdatePasswdInSchema\x12\x14\n\x0cold_password\x18\x01 \x01(\t\x12\x14\n\x0cnew_password\x18\x02 \x01(\t\"\x86\x01\n\x18UpdatePermissionInSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0b\x62\x65long_type\x18\x03 \x01(\t\x12\x14\n\x0crequest_type\x18\x04 \x01(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x0e\n\x06method\x18\x06 \x01(\t\"\x9b\x01\n\x13UpdatePermissionOut\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0b\x62\x65long_type\x18\x05 \x01(\t\x12\x14\n\x0crequest_type\x18\x06 \x01(\t\x12\x0c\n\x04path\x18\x07 \x01(\t\x12\x0e\n\x06method\x18\x08 \x01(\t\"t\n\x19UpdatePermissionOutSchema\x12-\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1f.Gui_Server.UpdatePermissionOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"l\n\x15UpdatePileInfoSchemas\x12\x1b\n\x13\x63harging_station_id\x18\x01 \x01(\t\x12\x10\n\x08\x66ms_code\x18\x02 \x01(\x11\x12\x0e\n\x06gun_id\x18\x03 \x01(\t\x12\x14\n\x0cgun_fms_code\x18\x04 \x01(\x11\"W\n\x10UpdateTaskSchema\x12\x0c\n\x04qcId\x18\x01 \x01(\t\x12\x12\n\nspreadSize\x18\x02 \x01(\t\x12\x11\n\tvehicleID\x18\x03 \x01(\t\x12\x0e\n\x06origin\x18\x04 \x01(\t\"\xca\x01\n\x12UpdateUserInSchema\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x12\n\ndepartment\x18\x05 \x01(\t\x12\x10\n\x08group_id\x18\x06 \x01(\x11\x12\x11\n\tquestion1\x18\x07 \x01(\t\x12\x11\n\tquestion2\x18\x08 \x01(\t\x12\x0f\n\x07\x61nswer1\x18\t \x01(\t\x12\x0f\n\x07\x61nswer2\x18\n \x01(\t\"W\n\rUpdateUserOut\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\"h\n\x13UpdateUserOutSchema\x12\'\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x19.Gui_Server.UpdateUserOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"\xb4\x01\n\x0eUserInfoSchema\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\ndepartment\x18\x04 \x01(\t\x12\x12\n\nfirst_name\x18\x05 \x01(\t\x12\x11\n\tlast_name\x18\x06 \x01(\t\x12\x16\n\x0eis_first_login\x18\x07 \x01(\x08\x12\x10\n\x08is_super\x18\x08 \x01(\x08\x12\x10\n\x08group_id\x18\t \x01(\x11\"\x83\x01\n\x17UserWithTokenInfoSchema\x12,\n\x08userinfo\x18\x01 \x01(\x0b\x32\x1a.Gui_Server.UserInfoSchema\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x11\"\x81\x01\n\"UserWithTokenOutResponseInfoSchema\x12\x31\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32#.Gui_Server.UserWithTokenInfoSchema\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"9\n\x0fValidationError\x12\x0b\n\x03loc\x18\x01 \x03(\x11\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t2\xc4?\n\nGui_Server\x12\x43\n\x0e\x61uthentication\x12\x19.Gui_Server.LoginInSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x33\n\x04\x61uth\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12I\n\rupdate_passwd\x12 .Gui_Server.UpdatePasswdInSchema\x1a\x14.Gui_Server.Response\"\x00\x12>\n\x04user\x12\x1e.Gui_Server.CreateUserInSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x42\n\x08user_put\x12\x1e.Gui_Server.UpdateUserInSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x37\n\x08user_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12:\n\x0buser_delete\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x33\n\x04list\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x32\n\x03\x61ll\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12@\n\x05group\x12\x1f.Gui_Server.CreateGroupInSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x44\n\tgroup_put\x12\x1f.Gui_Server.UpdateGroupInSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x38\n\tgroup_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12;\n\x0cgroup_delete\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12<\n\rgroup_all_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12J\n\npermission\x12$.Gui_Server.CreatePermissionInSchema\x1a\x14.Gui_Server.Response\"\x00\x12N\n\x0epermission_put\x12$.Gui_Server.UpdatePermissionInSchema\x1a\x14.Gui_Server.Response\"\x00\x12=\n\x0epermission_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12@\n\x11permission_delete\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x41\n\x12permission_all_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x42\n\x13permission_list_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x37\n\x08\x64ownload\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x37\n\x08lockArea\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12I\n\x1a\x61pi_taskInfo_lockArea_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x35\n\x06\x64\x65lete\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12P\n!api_taskInfo_lockArea_delete_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12:\n\x0b\x64\x65leteByTag\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12U\n&api_taskInfo_lockArea_deleteByTag_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x35\n\x06\x63hange\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12P\n!api_taskInfo_lockArea_change_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x38\n\tresendJob\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12U\n&api_taskInfo_vehicleJob_resendJob_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x46\n\x17message_event_start_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12G\n\x18message_event_start_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x46\n\x17message_event_abort_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12G\n\x18message_event_abort_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12Q\n\"api_taskInfo_vehicleJob_delete_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12R\n#api_taskInfo_vehicleJob_delete_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12;\n\x0crunImmediate\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12V\n\'api_taskInfo_taskPool_runImmediate_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12N\n\x1f\x61pi_taskInfo_taskPool_abort_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12O\n api_taskInfo_taskPool_abort_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12<\n\rtrailerStatus\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12^\n/api_deviceInfo_vehicleStatus_trailerStatus_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x33\n\x04mode\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12U\n&api_deviceInfo_vehicleStatus_mode_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12<\n\rcontainerInfo\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12N\n\x1f\x61pi_taskInfo_containerInfo_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x44\n\x15message_event_rch_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x45\n\x16message_event_rch_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x34\n\x05query\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12L\n\x1d\x66ms_area_inventory_query_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12K\n\x1c\x61pi_vehicleManager_power_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12L\n\x1d\x61pi_vehicleManager_power_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12O\n api_vehicleManager_handshake_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12P\n!api_vehicleManager_handshake_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12;\n\x0cSetOperation\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12]\n.api_deviceInfo_vehicleStatus_SetOperation_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12X\n)api_vehicleManager_report_speed_ratio_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12Y\n*api_vehicleManager_report_speed_ratio_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12P\n!api_container_InventoryUpdate_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12Q\n\"api_container_InventoryUpdate_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x42\n\x13SetVesselInfoStatus\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12_\n0api_taskInfo_VesselInfo_SetVesselInfoStatus_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x38\n\tquery_all\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12U\n&api_taskInfo_vehicleJob_query_all_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x39\n\nPaceGlobal\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12K\n\x1c\x61pi_taskInfo_PaceGlobal_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x36\n\x07SetLane\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12R\n#api_taskInfo_quayCrane_SetLane_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12O\n message_event_update_qc_task_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12P\n!message_event_update_qc_task_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x39\n\nvehicleJob\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12K\n\x1c\x61pi_taskInfo_vehicleJob_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12>\n\x0f\x61ll_current_job\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12[\n,api_taskInfo_vehicleJob_all_current_job_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12O\n api_container_EditContainers_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12P\n!api_container_EditContainers_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12J\n\x1b\x61pi_vehicleManager_stop_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12K\n\x1c\x61pi_vehicleManager_stop_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x35\n\x06\x65ngine\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12>\n\x0f\x61pi_engine_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x42\n\x13response_mixed_area\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12K\n\x1c\x61pi_response_mixed_area_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x35\n\x06points\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12M\n\x1e\x61pi_vehicleManager_points_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x35\n\x06GetAll\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12W\n(api_taskInfo_EquipmentStatus_GetAll_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x36\n\x07rc_task\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x44\n\x15\x61pi_task_rc_task_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12<\n\rapi_telep_get\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12=\n\x0e\x61pi_telep_post\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12\x45\n\rSetVesselInfo\x12\x1c.Gui_Server.SetVesselSchemas\x1a\x14.Gui_Server.Response\"\x00\x12I\n\x11ReleaseVesselInfo\x12\x1c.Gui_Server.DelVesselSchemas\x1a\x14.Gui_Server.Response\"\x00\x12\x38\n\tGetBertNO\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12=\n\x0e\x45\x64itVesselInfo\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12S\n\x12ghostVehicleCancel\x12%.Gui_Server.SetGhostVehicleCancelPost\x1a\x14.Gui_Server.Response\"\x00\x12G\n\x0f\x45quipmentStatus\x12\x1c.Gui_Server.SetSwitchRequest\x1a\x14.Gui_Server.Response\"\x00\x12\x44\n\x0cSpreaderSize\x12\x1c.Gui_Server.SetSwitchRequest\x1a\x14.Gui_Server.Response\"\x00\x12I\n\rGetAllMessage\x12 .Gui_Server.GetAllMessageSchemas\x1a\x14.Gui_Server.Response\"\x00\x12M\n\x0eGetFileMessage\x12#.Gui_Server.GetAllMessageCSVSchemas\x1a\x14.Gui_Server.Response\"\x00\x12K\n\x0eUpdatePileInfo\x12!.Gui_Server.UpdatePileInfoSchemas\x1a\x14.Gui_Server.Response\"\x00\x12M\n\x11UpdateAllPileInfo\x12 .Gui_Server.UpdateALlInfoSchemas\x1a\x14.Gui_Server.Response\"\x00\x12O\n\x12\x43ontainerInfoSetup\x12!.Gui_Server.ContainerSteupSchemas\x1a\x14.Gui_Server.Response\"\x00\x12\x38\n\tPlcStatus\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12<\n\rServerVersion\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12I\n\rForceOverTake\x12 .Gui_Server.ForceOvertakeSchemas\x1a\x14.Gui_Server.Response\"\x00\x12\x43\n\x0bupdate_task\x12\x1c.Gui_Server.UpdateTaskSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x43\n\nload_first\x12\x1d.Gui_Server.LoadFirstInSchema\x1a\x14.Gui_Server.Response\"\x00\x12\x41\n\tredo_task\x12\x1c.Gui_Server.RedoTaskInSchema\x1a\x14.Gui_Server.Response\"\x00\x12I\n\x12\x43ollectionFailTask\x12\x1b.Gui_Server.FailTaskSchemas\x1a\x14.Gui_Server.Response\"\x00\x12?\n\x0c\x65vent_report\x12\x17.Gui_Server.EventReport\x1a\x14.Gui_Server.Response\"\x00\x12=\n\x0eTosLoginStatus\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x12M\n\x11twistlock_station\x12 .Gui_Server.CRUDTwistlockStation\x1a\x14.Gui_Server.Response\"\x00\x12\x38\n\tGetPtions\x12\x13.Gui_Server.Request\x1a\x14.Gui_Server.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gui_server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EVENTREPORT_DATAENTRY']._options = None
  _globals['_EVENTREPORT_DATAENTRY']._serialized_options = b'8\001'
  _globals['_REQUEST']._serialized_start=59
  _globals['_REQUEST']._serialized_end=104
  _globals['_RESPONSE']._serialized_start=106
  _globals['_RESPONSE']._serialized_end=220
  _globals['_BODYDENMARKINFOIMPORTCONTAINERSPOST']._serialized_start=222
  _globals['_BODYDENMARKINFOIMPORTCONTAINERSPOST']._serialized_end=274
  _globals['_BODYFILETRANSPORTUPLOADPOST']._serialized_start=276
  _globals['_BODYFILETRANSPORTUPLOADPOST']._serialized_end=320
  _globals['_CRUDTWISTLOCKSTATION']._serialized_start=323
  _globals['_CRUDTWISTLOCKSTATION']._serialized_end=550
  _globals['_CONTAINERSTEUPSCHEMAS']._serialized_start=553
  _globals['_CONTAINERSTEUPSCHEMAS']._serialized_end=717
  _globals['_CREATEGROUPINSCHEMA']._serialized_start=719
  _globals['_CREATEGROUPINSCHEMA']._serialized_end=800
  _globals['_CREATEPERMISSIONINSCHEMA']._serialized_start=803
  _globals['_CREATEPERMISSIONINSCHEMA']._serialized_end=937
  _globals['_CREATESUCCESSSCHEMA']._serialized_start=939
  _globals['_CREATESUCCESSSCHEMA']._serialized_end=1038
  _globals['_CREATEUSERINSCHEMA']._serialized_start=1041
  _globals['_CREATEUSERINSCHEMA']._serialized_end=1261
  _globals['_CURRENTUSERGROUPOUT']._serialized_start=1264
  _globals['_CURRENTUSERGROUPOUT']._serialized_end=1393
  _globals['_CURRENTUSERGROUPPERMISSION']._serialized_start=1395
  _globals['_CURRENTUSERGROUPPERMISSION']._serialized_end=1484
  _globals['_DELVESSELSCHEMAS']._serialized_start=1486
  _globals['_DELVESSELSCHEMAS']._serialized_end=1547
  _globals['_DELETESUCCESSSCHEMA']._serialized_start=1549
  _globals['_DELETESUCCESSSCHEMA']._serialized_end=1648
  _globals['_EVENTREPORT']._serialized_start=1651
  _globals['_EVENTREPORT']._serialized_end=1853
  _globals['_EVENTREPORT_DATAENTRY']._serialized_start=1788
  _globals['_EVENTREPORT_DATAENTRY']._serialized_end=1853
  _globals['_FAILTASKSCHEMAS']._serialized_start=1855
  _globals['_FAILTASKSCHEMAS']._serialized_end=1965
  _globals['_FORCEOVERTAKESCHEMAS']._serialized_start=1967
  _globals['_FORCEOVERTAKESCHEMAS']._serialized_end=2027
  _globals['_GETALLMESSAGECSVSCHEMAS']._serialized_start=2030
  _globals['_GETALLMESSAGECSVSCHEMAS']._serialized_end=2188
  _globals['_GETALLMESSAGESCHEMAS']._serialized_start=2191
  _globals['_GETALLMESSAGESCHEMAS']._serialized_end=2361
  _globals['_GETGROUPALLOUTSCHEMA']._serialized_start=2364
  _globals['_GETGROUPALLOUTSCHEMA']._serialized_end=2500
  _globals['_GETGROUPOUT']._serialized_start=2503
  _globals['_GETGROUPOUT']._serialized_end=2656
  _globals['_GETGROUPOUTSCHEMA']._serialized_start=2658
  _globals['_GETGROUPOUTSCHEMA']._serialized_end=2758
  _globals['_GETPERMISSIONALLOUTSCHEMA']._serialized_start=2761
  _globals['_GETPERMISSIONALLOUTSCHEMA']._serialized_end=2907
  _globals['_GETPERMISSIONLISTOUTSCHEMA']._serialized_start=2910
  _globals['_GETPERMISSIONLISTOUTSCHEMA']._serialized_end=3057
  _globals['_GETPERMISSIONOUTSCHEMA']._serialized_start=3059
  _globals['_GETPERMISSIONOUTSCHEMA']._serialized_end=3172
  _globals['_GETSELFOUT']._serialized_start=3175
  _globals['_GETSELFOUT']._serialized_end=3380
  _globals['_GETSELFOUTSCHEMA']._serialized_start=3382
  _globals['_GETSELFOUTSCHEMA']._serialized_end=3438
  _globals['_GETSELFOUTWITHGROUP']._serialized_start=3441
  _globals['_GETSELFOUTWITHGROUP']._serialized_end=3573
  _globals['_GETSELFOUTWITHGROUPPERMISSION']._serialized_start=3575
  _globals['_GETSELFOUTWITHGROUPPERMISSION']._serialized_end=3667
  _globals['_GETUSERALLOUTSCHEMA']._serialized_start=3670
  _globals['_GETUSERALLOUTSCHEMA']._serialized_end=3805
  _globals['_GETUSERLISTOUT']._serialized_start=3808
  _globals['_GETUSERLISTOUT']._serialized_end=4030
  _globals['_GETUSERLISTOUTSCHEMA']._serialized_start=4033
  _globals['_GETUSERLISTOUTSCHEMA']._serialized_end=4169
  _globals['_GETUSERLISTOUTWITHGROUP']._serialized_start=4171
  _globals['_GETUSERLISTOUTWITHGROUP']._serialized_end=4243
  _globals['_GETUSEROUT']._serialized_start=4246
  _globals['_GETUSEROUT']._serialized_end=4607
  _globals['_GETUSEROUTSCHEMA']._serialized_start=4609
  _globals['_GETUSEROUTSCHEMA']._serialized_end=4707
  _globals['_HTTPVALIDATIONERROR']._serialized_start=4709
  _globals['_HTTPVALIDATIONERROR']._serialized_end=4775
  _globals['_LOADFIRSTINSCHEMA']._serialized_start=4777
  _globals['_LOADFIRSTINSCHEMA']._serialized_end=4853
  _globals['_LOGININSCHEMA']._serialized_start=4855
  _globals['_LOGININSCHEMA']._serialized_end=4906
  _globals['_REDOTASKINSCHEMA']._serialized_start=4908
  _globals['_REDOTASKINSCHEMA']._serialized_end=4961
  _globals['_SETGHOSTVEHICLECANCELPOST']._serialized_start=4963
  _globals['_SETGHOSTVEHICLECANCELPOST']._serialized_end=5033
  _globals['_SETSWITCHREQUEST']._serialized_start=5035
  _globals['_SETSWITCHREQUEST']._serialized_end=5114
  _globals['_SETVESSELSCHEMAS']._serialized_start=5117
  _globals['_SETVESSELSCHEMAS']._serialized_end=5405
  _globals['_UPDATEALLINFOSCHEMAS']._serialized_start=5407
  _globals['_UPDATEALLINFOSCHEMAS']._serialized_end=5457
  _globals['_UPDATEGROUPINSCHEMA']._serialized_start=5459
  _globals['_UPDATEGROUPINSCHEMA']._serialized_end=5540
  _globals['_UPDATEGROUPOUT']._serialized_start=5542
  _globals['_UPDATEGROUPOUT']._serialized_end=5664
  _globals['_UPDATEGROUPOUTPERMISSION']._serialized_start=5666
  _globals['_UPDATEGROUPOUTPERMISSION']._serialized_end=5753
  _globals['_UPDATEGROUPOUTSCHEMA']._serialized_start=5755
  _globals['_UPDATEGROUPOUTSCHEMA']._serialized_end=5861
  _globals['_UPDATEPASSWDINSCHEMA']._serialized_start=5863
  _globals['_UPDATEPASSWDINSCHEMA']._serialized_end=5929
  _globals['_UPDATEPERMISSIONINSCHEMA']._serialized_start=5932
  _globals['_UPDATEPERMISSIONINSCHEMA']._serialized_end=6066
  _globals['_UPDATEPERMISSIONOUT']._serialized_start=6069
  _globals['_UPDATEPERMISSIONOUT']._serialized_end=6224
  _globals['_UPDATEPERMISSIONOUTSCHEMA']._serialized_start=6226
  _globals['_UPDATEPERMISSIONOUTSCHEMA']._serialized_end=6342
  _globals['_UPDATEPILEINFOSCHEMAS']._serialized_start=6344
  _globals['_UPDATEPILEINFOSCHEMAS']._serialized_end=6452
  _globals['_UPDATETASKSCHEMA']._serialized_start=6454
  _globals['_UPDATETASKSCHEMA']._serialized_end=6541
  _globals['_UPDATEUSERINSCHEMA']._serialized_start=6544
  _globals['_UPDATEUSERINSCHEMA']._serialized_end=6746
  _globals['_UPDATEUSEROUT']._serialized_start=6748
  _globals['_UPDATEUSEROUT']._serialized_end=6835
  _globals['_UPDATEUSEROUTSCHEMA']._serialized_start=6837
  _globals['_UPDATEUSEROUTSCHEMA']._serialized_end=6941
  _globals['_USERINFOSCHEMA']._serialized_start=6944
  _globals['_USERINFOSCHEMA']._serialized_end=7124
  _globals['_USERWITHTOKENINFOSCHEMA']._serialized_start=7127
  _globals['_USERWITHTOKENINFOSCHEMA']._serialized_end=7258
  _globals['_USERWITHTOKENOUTRESPONSEINFOSCHEMA']._serialized_start=7261
  _globals['_USERWITHTOKENOUTRESPONSEINFOSCHEMA']._serialized_end=7390
  _globals['_VALIDATIONERROR']._serialized_start=7392
  _globals['_VALIDATIONERROR']._serialized_end=7449
  _globals['_GUI_SERVER']._serialized_start=7452
  _globals['_GUI_SERVER']._serialized_end=15584
# @@protoc_insertion_point(module_scope)