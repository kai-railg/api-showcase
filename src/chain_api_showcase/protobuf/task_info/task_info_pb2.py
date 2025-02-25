# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_info.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

SetKvStoreInSchema = None
QueryJobAllPost = None
FullStopStatus = None
LockSwitchInSchema = None
DeleteKvStore = None
GetTsSchemas = None
QueryJobPost = None
DeleteJobPost = None
SetKvStoreListInSchema = None
SetLaneInSchema = None
FinishFenceEvent = None
SetAlarmMessage = None
VirtualPointsPost = None
DelVesselInfoSchemas = None
Request = None
AlarmMessageSchema = None
SetFMSMessage = None
StopAlarmMessage = None
SetBusProcessInSchema = None
ResendJobPost = None
UpdateJobDest = None
SetVesselInfoSchemas = None
CreateFence = None
SetVesselInfoStatusSchemas = None
PreArriveInSchema = None
UpdatePlanContainers = None
SetContainerInfoInSchema = None
Response = None

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftask_info.proto\x12\tTask_Info\x1a\x19google/protobuf/any.proto\"-\n\x07Request\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"r\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\r\"\x93\x01\n\x12\x41larmMessageSchema\x12\x12\n\nstart_time\x18\x01 \x01(\x11\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x11\x12(\n\ntruck_list\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05level\x18\x04 \x01(\x11\x12\x10\n\x08per_page\x18\x05 \x01(\x11\x12\x0c\n\x04page\x18\x06 \x01(\x11\"\xc7\x01\n\x13\x43ontainerInfoSchema\x12\x16\n\x0e\x63ontainerStack\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainerNum\x18\x02 \x01(\t\x12\x14\n\x0c\x63ontainerIso\x18\x03 \x01(\t\x12\x15\n\rdoorDirection\x18\x04 \x01(\t\x12\x13\n\x0breferenceId\x18\x05 \x01(\t\x12\x0e\n\x06weight\x18\x06 \x01(\t\x12\x0f\n\x07sealing\x18\x07 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12\x11\n\temptyFull\x18\t \x01(\t\"d\n\x0b\x43reateFence\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x18\n\x10passing_location\x18\x02 \x01(\t\x12\x15\n\rpassing_event\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\"c\n\x13\x43reateSuccessSchema\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"w\n\x18\x43reateSuccessSchemaCount\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x11\"-\n\x14\x44\x65lVesselInfoSchemas\x12\x15\n\rvesselVisitId\x18\x01 \x01(\t\" \n\rDeleteJobPost\x12\x0f\n\x07job_ids\x18\x01 \x03(\t\"/\n\rDeleteKvStore\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"j\n\x10\x46inishFenceEvent\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x18\n\x10passing_location\x18\x02 \x01(\t\x12\x15\n\rpassing_event\x18\x03 \x01(\t\x12\x12\n\njob_finish\x18\x04 \x01(\x11\" \n\x0e\x46ullStopStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\"P\n\x10GetBusProcessOut\x12\x17\n\x0fprocess_def_key\x18\x01 \x01(\t\x12\x11\n\ttenant_id\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\"m\n\x16GetBusProcessOutSchema\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.Task_Info.GetBusProcessOut\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x11\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"h\n\x0cGetTsSchemas\x12\x0f\n\x07ts_name\x18\x01 \x01(\t\x12\x11\n\tts_vessel\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\x12\x11\n\tts_status\x18\x04 \x01(\t\x12\x0f\n\x07ts_lane\x18\x05 \x01(\t\"A\n\x13HTTPValidationError\x12*\n\x06\x64\x65tail\x18\x01 \x03(\x0b\x32\x1a.Task_Info.ValidationError\"o\n\x12LockSwitchInSchema\x12\x0f\n\x07ts_name\x18\x01 \x01(\t\x12\x10\n\x08ts_state\x18\x02 \x01(\t\x12\x0f\n\x07ts_type\x18\x03 \x01(\t\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01y\x18\x05 \x01(\x02\x12\x0f\n\x07heading\x18\x06 \x01(\x02\"Y\n\x0fLogicalLocation\x12\x0c\n\x04\x61rea\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x0c\n\x04lane\x18\x03 \x01(\t\x12\r\n\x05stack\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\t\"\'\n\x11PreArriveInSchema\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\"\x88\x01\n\x0fQueryJobAllPost\x12\x12\n\nstart_time\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x03(\x11\x12\x10\n\x08vehicles\x18\x04 \x03(\t\x12\x0c\n\x04\x61rea\x18\x05 \x01(\t\x12\x0c\n\x04page\x18\x06 \x01(\x11\x12\x11\n\tpage_size\x18\x07 \x01(\x11\"_\n\x0cQueryJobPost\x12\x0e\n\x06status\x18\x01 \x03(\x11\x12\x10\n\x08vehicles\x18\x02 \x03(\t\x12\x0c\n\x04\x61rea\x18\x03 \x01(\t\x12\x0c\n\x04page\x18\x04 \x01(\x11\x12\x11\n\tpage_size\x18\x05 \x01(\x11\"T\n\rResendJobPost\x12\x15\n\rbusiness_keys\x18\x01 \x03(\t\x12,\n\x0bresend_jobs\x18\x02 \x03(\x0b\x32\x17.Task_Info.ResendOneJob\"1\n\x0cResendOneJob\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x11\n\tassign_to\x18\x02 \x01(\t\"l\n\x0fSetAlarmMessage\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x14\n\x0c\x65rror_origin\x18\x02 \x01(\t\x12\x31\n\nerror_info\x18\x03 \x03(\x0b\x32\x1d.Task_Info.SetAlarmMessageBak\"\xc6\x01\n\x12SetAlarmMessageBak\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x12\n\nalarmLevel\x18\x03 \x01(\x11\x12\x11\n\talarmCode\x18\x04 \x01(\x11\x12\x11\n\talarmType\x18\x05 \x01(\x11\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0f\n\x07subCode\x18\x07 \x01(\x11\x12\x16\n\x0esubDescription\x18\x08 \x01(\t\x12\x13\n\x0bmessageType\x18\t \x01(\t\"U\n\x15SetBusProcessInSchema\x12\x17\n\x0fprocess_def_key\x18\x01 \x01(\t\x12\x11\n\ttenant_id\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\"\x86\x01\n\x18SetContainerInfoInSchema\x12\x12\n\nvehicle_id\x18\x01 \x01(\t\x12\x1f\n\x17is_reference_id_updated\x18\x02 \x01(\x08\x12\x35\n\rcontainerList\x18\x03 \x03(\x0b\x32\x1e.Task_Info.ContainerInfoSchema\"}\n\rSetFMSMessage\x12\x17\n\x0fmessageUniqueID\x18\x01 \x01(\t\x12\x11\n\tvehicleID\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\r\n\x05level\x18\x06 \x01(\x11\"Y\n\x12SetKvStoreInSchema\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12#\n\x05value\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\x89\x01\n\x16SetKvStoreListInSchema\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12#\n\x05value\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\toperation\x18\x04 \x01(\t\x12\x17\n\x0f\x61llow_duplicate\x18\x05 \x01(\x08\"H\n\x0fSetLaneInSchema\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0f\n\x07lane_id\x18\x02 \x01(\t\x12\x11\n\tlane_type\x18\x03 \x01(\t\"\x82\x04\n\x14SetVesselInfoSchemas\x12\x15\n\rvesselVisitId\x18\x01 \x01(\t\x12\x12\n\nvesselName\x18\x02 \x01(\t\x12\r\n\x05inVyg\x18\x03 \x01(\t\x12\x0e\n\x06outVyg\x18\x04 \x01(\t\x12\r\n\x05phase\x18\x05 \x01(\t\x12\x13\n\x0b\x62ollardFore\x18\x06 \x01(\x11\x12\x14\n\x0c\x62ollardAfter\x18\x07 \x01(\x11\x12\x12\n\nvessl_type\x18\x08 \x01(\t\x12\x15\n\rinitializedAt\x18\t \x01(\t\x12\x17\n\x0fvesselDirection\x18\n \x01(\t\x12%\n\x07\x61t_list\x18\x0b \x03(\x0b\x32\x14.google.protobuf.Any\x12\"\n\x04QCAG\x18\x0c \x03(\x0b\x32\x14.google.protobuf.Any\x12#\n\x05\x62owPB\x18\r \x03(\x0b\x32\x14.google.protobuf.Any\x12#\n\x05stnPB\x18\x0e \x03(\x0b\x32\x14.google.protobuf.Any\x12\x0b\n\x03\x45TA\x18\x0f \x01(\t\x12\x0b\n\x03\x45TB\x18\x10 \x01(\t\x12\x0b\n\x03\x45TD\x18\x11 \x01(\t\x12\x10\n\x08rta_time\x18\x12 \x01(\t\x12(\n\ncoordinate\x18\x13 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x13\n\x0bmesses_type\x18\x14 \x01(\t\x12\x15\n\rupdate_status\x18\x15 \x01(\t\"I\n\x1aSetVesselInfoStatusSchemas\x12\x15\n\rvesselVisitId\x18\x01 \x01(\t\x12\x14\n\x0cVesselStatus\x18\x02 \x01(\t\"J\n\x10StopAlarmMessage\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x11\n\talarmCode\x18\x03 \x01(\x11\"V\n\rUpdateJobDest\x12\x14\n\x0c\x62usiness_key\x18\x01 \x01(\t\x12/\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32\x1a.Task_Info.LogicalLocation\"\xf9\x01\n\x14UpdatePlanContainers\x12\x14\n\x0c\x62usiness_key\x18\x01 \x01(\t\x12m\n\x1fplannedContainerDestinationList\x18\x02 \x03(\x0b\x32\x44.Task_Info.UpdatePlanContainers.PlannedContainerDestinationListEntry\x1a\\\n$PlannedContainerDestinationListEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"9\n\x0fValidationError\x12\x0b\n\x03loc\x18\x01 \x03(\x11\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"=\n\x11VirtualPointsPost\x12\x14\n\x0cvirtual_type\x18\x01 \x01(\t\x12\x12\n\nkey_points\x18\x02 \x03(\t2\xa0\x30\n\tTask_Info\x12N\n!api_taskInfo_maintain_status_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12:\n\rdeleteAllArea\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x38\n\x0b\x61\x62ortAllJob\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x34\n\x07kvStore\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12Q\n\x19\x61pi_taskInfo_kvStore_post\x12\x1d.Task_Info.SetKvStoreInSchema\x1a\x13.Task_Info.Response\"\x00\x12S\n api_taskInfo_kvStore_delete_post\x12\x18.Task_Info.DeleteKvStore\x1a\x13.Task_Info.Response\"\x00\x12J\n\x1d\x61pi_taskInfo_kvStore_list_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12Z\n\x1e\x61pi_taskInfo_kvStore_list_post\x12!.Task_Info.SetKvStoreListInSchema\x1a\x13.Task_Info.Response\"\x00\x12\x35\n\x08listFind\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x34\n\x07process\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12T\n\x19\x61pi_taskInfo_process_post\x12 .Task_Info.SetBusProcessInSchema\x1a\x13.Task_Info.Response\"\x00\x12K\n\x1e\x61pi_taskInfo_containerInfo_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12]\n\x1f\x61pi_taskInfo_containerInfo_post\x12#.Task_Info.SetContainerInfoInSchema\x1a\x13.Task_Info.Response\"\x00\x12\x33\n\x06\x63reate\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12P\n#api_taskInfo_vehicleJob_status_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x32\n\x05stage\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x38\n\x0b\x62usinessKey\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12H\n\x1b\x61pi_taskInfo_vehicleJob_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x30\n\x03get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x33\n\x06getStd\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x39\n\x0cgetByMission\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12O\n\"api_taskInfo_vehicleJob_abort_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12@\n\rupdateJobDest\x12\x18.Task_Info.UpdateJobDest\x1a\x13.Task_Info.Response\"\x00\x12N\n\x14updatePlanContainers\x12\x1f.Task_Info.UpdatePlanContainers\x1a\x13.Task_Info.Response\"\x00\x12R\n%api_taskInfo_vehicleJob_complete_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x37\n\njobMission\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12T\n\'api_taskInfo_vehicleJob_jobMission_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x35\n\x08stageTag\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12Y\n&api_taskInfo_vehicleJob_resendJob_post\x12\x18.Task_Info.ResendJobPost\x1a\x13.Task_Info.Response\"\x00\x12V\n#api_taskInfo_vehicleJob_delete_post\x12\x18.Task_Info.DeleteJobPost\x1a\x13.Task_Info.Response\"\x00\x12T\n\"api_taskInfo_vehicleJob_query_post\x12\x17.Task_Info.QueryJobPost\x1a\x13.Task_Info.Response\"\x00\x12\x33\n\x06newest\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12;\n\x0e\x61ll_newest_job\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12X\n+api_taskInfo_vehicleJob_all_current_job_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12[\n&api_taskInfo_vehicleJob_query_all_post\x12\x1a.Task_Info.QueryJobAllPost\x1a\x13.Task_Info.Response\"\x00\x12\x42\n\x15\x61ll_newest_job_filter\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12;\n\x0evirtual_points\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x62\n+api_taskInfo_vehicleJob_virtual_points_post\x12\x1c.Task_Info.VirtualPointsPost\x1a\x13.Task_Info.Response\"\x00\x12;\n\x0eworkflowConfig\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12M\n api_taskInfo_workflowConfig_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x46\n\x19\x61pi_taskInfo_lockArea_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12G\n\x1a\x61pi_taskInfo_lockArea_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12N\n!api_taskInfo_lockArea_delete_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12S\n&api_taskInfo_lockArea_deleteByTag_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12N\n!api_taskInfo_lockArea_change_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x38\n\x0b\x63hangeByTag\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x64\n*api_taskInfo_VesselInfo_SetVesselInfo_post\x12\x1f.Task_Info.SetVesselInfoSchemas\x1a\x13.Task_Info.Response\"\x00\x12X\n+api_taskInfo_VesselInfo_EditVesselInfo_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12:\n\rGetVesselInfo\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12J\n\x10\x44\x65leteVesselInfo\x12\x1f.Task_Info.DelVesselInfoSchemas\x1a\x13.Task_Info.Response\"\x00\x12p\n0api_taskInfo_VesselInfo_SetVesselInfoStatus_post\x12%.Task_Info.SetVesselInfoStatusSchemas\x1a\x13.Task_Info.Response\"\x00\x12\x46\n\x11\x41larmMessageStart\x12\x1a.Task_Info.SetAlarmMessage\x1a\x13.Task_Info.Response\"\x00\x12J\n\x15\x41larmMessageStart_bak\x12\x1a.Task_Info.SetAlarmMessage\x1a\x13.Task_Info.Response\"\x00\x12\x46\n\x10\x41larmMessageStop\x12\x1b.Task_Info.StopAlarmMessage\x1a\x13.Task_Info.Response\"\x00\x12G\n\x0fGetAlarmMessage\x12\x1d.Task_Info.AlarmMessageSchema\x1a\x13.Task_Info.Response\"\x00\x12@\n\rSetFmsMessage\x12\x18.Task_Info.SetFMSMessage\x1a\x13.Task_Info.Response\"\x00\x12\x45\n\rGetFmsMessage\x12\x1d.Task_Info.AlarmMessageSchema\x1a\x13.Task_Info.Response\"\x00\x12\x30\n\x03set\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12I\n\x1c\x61pi_taskInfo_subTask_get_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12L\n\x1f\x61pi_taskInfo_subTask_clear_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12;\n\nfenceEvent\x12\x16.Task_Info.CreateFence\x1a\x13.Task_Info.Response\"\x00\x12<\n\x06\x66inish\x12\x1b.Task_Info.FinishFenceEvent\x1a\x13.Task_Info.Response\"\x00\x12M\n api_taskInfo_fenceEvent_get_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12K\n\x1e\x61pi_taskInfo_taskPool_get_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x30\n\x03\x61\x64\x64\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12N\n!api_taskInfo_taskPool_update_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12M\n api_taskInfo_taskPool_abort_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12T\n\'api_taskInfo_taskPool_runImmediate_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12N\n!api_taskInfo_taskPool_delete_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x36\n\tTsRelated\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12O\n\"api_taskInfo_TsRelated_delete_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x31\n\x04\x45\x64it\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12\x35\n\x03Get\x12\x17.Task_Info.GetTsSchemas\x1a\x13.Task_Info.Response\"\x00\x12N\n!api_taskInfo_EquipmentStatus_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12Q\n$api_taskInfo_EquipmentStatus_Get_get\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12[\n.api_taskInfo_EquipmentStatus_SpreaderSize_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12<\n\x0fGetSpreaderSize\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12I\n\x1c\x61pi_taskInfo_PaceGlobal_post\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12X\n#api_taskInfo_quayCrane_SetLane_post\x12\x1a.Task_Info.SetLaneInSchema\x1a\x13.Task_Info.Response\"\x00\x12\x34\n\x07GetLane\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12@\n\tpreArrive\x12\x1c.Task_Info.PreArriveInSchema\x1a\x13.Task_Info.Response\"\x00\x12\x36\n\tts_switch\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12S\n\x1b\x61pi_taskInfo_ts_switch_post\x12\x1d.Task_Info.LockSwitchInSchema\x1a\x13.Task_Info.Response\"\x00\x12:\n\rsim_start_job\x12\x12.Task_Info.Request\x1a\x13.Task_Info.Response\"\x00\x12?\n\x0b\x66ullControl\x12\x19.Task_Info.FullStopStatus\x1a\x13.Task_Info.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_info_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_UPDATEPLANCONTAINERS_PLANNEDCONTAINERDESTINATIONLISTENTRY']._options = None
  _globals['_UPDATEPLANCONTAINERS_PLANNEDCONTAINERDESTINATIONLISTENTRY']._serialized_options = b'8\001'
  _globals['_REQUEST']._serialized_start=57
  _globals['_REQUEST']._serialized_end=102
  _globals['_RESPONSE']._serialized_start=104
  _globals['_RESPONSE']._serialized_end=218
  _globals['_ALARMMESSAGESCHEMA']._serialized_start=221
  _globals['_ALARMMESSAGESCHEMA']._serialized_end=368
  _globals['_CONTAINERINFOSCHEMA']._serialized_start=371
  _globals['_CONTAINERINFOSCHEMA']._serialized_end=570
  _globals['_CREATEFENCE']._serialized_start=572
  _globals['_CREATEFENCE']._serialized_end=672
  _globals['_CREATESUCCESSSCHEMA']._serialized_start=674
  _globals['_CREATESUCCESSSCHEMA']._serialized_end=773
  _globals['_CREATESUCCESSSCHEMACOUNT']._serialized_start=775
  _globals['_CREATESUCCESSSCHEMACOUNT']._serialized_end=894
  _globals['_DELVESSELINFOSCHEMAS']._serialized_start=896
  _globals['_DELVESSELINFOSCHEMAS']._serialized_end=941
  _globals['_DELETEJOBPOST']._serialized_start=943
  _globals['_DELETEJOBPOST']._serialized_end=975
  _globals['_DELETEKVSTORE']._serialized_start=977
  _globals['_DELETEKVSTORE']._serialized_end=1024
  _globals['_FINISHFENCEEVENT']._serialized_start=1026
  _globals['_FINISHFENCEEVENT']._serialized_end=1132
  _globals['_FULLSTOPSTATUS']._serialized_start=1134
  _globals['_FULLSTOPSTATUS']._serialized_end=1166
  _globals['_GETBUSPROCESSOUT']._serialized_start=1168
  _globals['_GETBUSPROCESSOUT']._serialized_end=1248
  _globals['_GETBUSPROCESSOUTSCHEMA']._serialized_start=1250
  _globals['_GETBUSPROCESSOUTSCHEMA']._serialized_end=1359
  _globals['_GETTSSCHEMAS']._serialized_start=1361
  _globals['_GETTSSCHEMAS']._serialized_end=1465
  _globals['_HTTPVALIDATIONERROR']._serialized_start=1467
  _globals['_HTTPVALIDATIONERROR']._serialized_end=1532
  _globals['_LOCKSWITCHINSCHEMA']._serialized_start=1534
  _globals['_LOCKSWITCHINSCHEMA']._serialized_end=1645
  _globals['_LOGICALLOCATION']._serialized_start=1647
  _globals['_LOGICALLOCATION']._serialized_end=1736
  _globals['_PREARRIVEINSCHEMA']._serialized_start=1738
  _globals['_PREARRIVEINSCHEMA']._serialized_end=1777
  _globals['_QUERYJOBALLPOST']._serialized_start=1780
  _globals['_QUERYJOBALLPOST']._serialized_end=1916
  _globals['_QUERYJOBPOST']._serialized_start=1918
  _globals['_QUERYJOBPOST']._serialized_end=2013
  _globals['_RESENDJOBPOST']._serialized_start=2015
  _globals['_RESENDJOBPOST']._serialized_end=2099
  _globals['_RESENDONEJOB']._serialized_start=2101
  _globals['_RESENDONEJOB']._serialized_end=2150
  _globals['_SETALARMMESSAGE']._serialized_start=2152
  _globals['_SETALARMMESSAGE']._serialized_end=2260
  _globals['_SETALARMMESSAGEBAK']._serialized_start=2263
  _globals['_SETALARMMESSAGEBAK']._serialized_end=2461
  _globals['_SETBUSPROCESSINSCHEMA']._serialized_start=2463
  _globals['_SETBUSPROCESSINSCHEMA']._serialized_end=2548
  _globals['_SETCONTAINERINFOINSCHEMA']._serialized_start=2551
  _globals['_SETCONTAINERINFOINSCHEMA']._serialized_end=2685
  _globals['_SETFMSMESSAGE']._serialized_start=2687
  _globals['_SETFMSMESSAGE']._serialized_end=2812
  _globals['_SETKVSTOREINSCHEMA']._serialized_start=2814
  _globals['_SETKVSTOREINSCHEMA']._serialized_end=2903
  _globals['_SETKVSTORELISTINSCHEMA']._serialized_start=2906
  _globals['_SETKVSTORELISTINSCHEMA']._serialized_end=3043
  _globals['_SETLANEINSCHEMA']._serialized_start=3045
  _globals['_SETLANEINSCHEMA']._serialized_end=3117
  _globals['_SETVESSELINFOSCHEMAS']._serialized_start=3120
  _globals['_SETVESSELINFOSCHEMAS']._serialized_end=3634
  _globals['_SETVESSELINFOSTATUSSCHEMAS']._serialized_start=3636
  _globals['_SETVESSELINFOSTATUSSCHEMAS']._serialized_end=3709
  _globals['_STOPALARMMESSAGE']._serialized_start=3711
  _globals['_STOPALARMMESSAGE']._serialized_end=3785
  _globals['_UPDATEJOBDEST']._serialized_start=3787
  _globals['_UPDATEJOBDEST']._serialized_end=3873
  _globals['_UPDATEPLANCONTAINERS']._serialized_start=3876
  _globals['_UPDATEPLANCONTAINERS']._serialized_end=4125
  _globals['_UPDATEPLANCONTAINERS_PLANNEDCONTAINERDESTINATIONLISTENTRY']._serialized_start=4033
  _globals['_UPDATEPLANCONTAINERS_PLANNEDCONTAINERDESTINATIONLISTENTRY']._serialized_end=4125
  _globals['_VALIDATIONERROR']._serialized_start=4127
  _globals['_VALIDATIONERROR']._serialized_end=4184
  _globals['_VIRTUALPOINTSPOST']._serialized_start=4186
  _globals['_VIRTUALPOINTSPOST']._serialized_end=4247
  _globals['_TASK_INFO']._serialized_start=4250
  _globals['_TASK_INFO']._serialized_end=10426
# @@protoc_insertion_point(module_scope)
