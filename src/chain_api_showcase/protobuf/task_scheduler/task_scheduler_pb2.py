# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_scheduler.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

TOSOrderUpdate = None
VehicleOrder = None
DependencyCheck = None
MovementInstructions = None
Request = None
MovementCancel = None
Response = None

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14task_scheduler.proto\x12\x0eTask_Scheduler\x1a\x19google/protobuf/any.proto\"-\n\x07Request\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"r\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\r\"\xba\x01\n\x12\x41\x63tionCodeResponse\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueId\x18\x02 \x01(\t\x12\x18\n\x10messageTimestamp\x18\x03 \x01(\t\x12\x0e\n\x06\x62uffer\x18\x04 \x01(\x08\x12\x16\n\x0e\x64\x65liveryStatus\x18\x05 \x01(\t\x12\x34\n\rlocationCheck\x18\x06 \x01(\x0b\x32\x1d.Task_Scheduler.LocationCheck\"\xf4\x02\n\x13\x43ontainerDefinition\x12\x16\n\x0euniqueObjectID\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\t\x12/\n\x0flogicalLocation\x18\x03 \x01(\x0b\x32\x16.Task_Scheduler.Origin\x12\x32\n\x0cportLocation\x18\x04 \x01(\x0b\x32\x1c.Task_Scheduler.PortLocation\x12\x0b\n\x03ISO\x18\x05 \x01(\t\x12\x0e\n\x06length\x18\x06 \x01(\x02\x12\r\n\x05width\x18\x07 \x01(\x02\x12\x0e\n\x06height\x18\x08 \x01(\x02\x12\x0e\n\x06weight\x18\t \x01(\x02\x12\x13\n\x0brelativePos\x18\n \x01(\t\x12\x13\n\x0btargetReady\x18\x0b \x01(\x08\x12\x14\n\x0creeferStatus\x18\x0c \x01(\t\x12!\n\x19\x61ssociatedTwinContainer_1\x18\r \x01(\t\x12!\n\x19\x61ssociatedTwinContainer_2\x18\x0e \x01(\t\"|\n\x0f\x44\x65pendencyCheck\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12;\n\x14movementInstructions\x18\x03 \x03(\x0b\x32\x1d.Task_Scheduler.WorkQueueInfo\"\xfc\x01\n\x17\x44\x65pendencyCheckResponse\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\t\x12S\n\x0e\x64\x65pendencyList\x18\x04 \x03(\x0b\x32;.Task_Scheduler.DependencyCheckResponse.DependencyListEntry\x1aK\n\x13\x44\x65pendencyListEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"c\n\x14\x44\x65pendencyDefinition\x12\x18\n\x10movementUniqueID\x18\x01 \x01(\t\x12\x19\n\x11processDependency\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x65pendencyType\x18\x03 \x01(\t\"\x9d\x01\n\x0e\x44\x65pendencyInfo\x12\x18\n\x10movementUniqueID\x18\x01 \x01(\t\x12&\n\x06origin\x18\x02 \x01(\x0b\x32\x16.Task_Scheduler.Origin\x12\x30\n\x0b\x64\x65stination\x18\x03 \x01(\x0b\x32\x1b.Task_Scheduler.Destination\x12\x17\n\x0f\x63ontainerNumber\x18\x04 \x01(\t\"D\n\x0e\x44\x65pendencyItem\x12\x18\n\x10pickupDependency\x18\x01 \x03(\t\x12\x18\n\x10groundDependency\x18\x02 \x03(\t\"j\n\x0b\x44\x65stination\x12\x0c\n\x04\x61rea\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x0c\n\x04lane\x18\x03 \x01(\x11\x12\r\n\x05stack\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\x11\x12\x13\n\x0borientation\x18\x06 \x01(\t\"\x93\x01\n\x13\x45xecutorDestination\x12@\n\x0flogicalLocation\x18\x01 \x01(\x0b\x32\'.Task_Scheduler.ExecutorLogicalLocation\x12:\n\x0cportLocation\x18\x02 \x01(\x0b\x32$.Task_Scheduler.ExecutorPortLocation\"v\n\x17\x45xecutorLogicalLocation\x12\x0c\n\x04\x61rea\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x0c\n\x04lane\x18\x03 \x01(\x11\x12\r\n\x05stack\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\x11\x12\x13\n\x0borientation\x18\x06 \x01(\t\"4\n\x14\x45xecutorPortLocation\x12\r\n\x05portX\x18\x01 \x01(\x02\x12\r\n\x05portY\x18\x02 \x01(\x02\"F\n\x13HTTPValidationError\x12/\n\x06\x64\x65tail\x18\x01 \x03(\x0b\x32\x1f.Task_Scheduler.ValidationError\"5\n\nJobContent\x12\x13\n\x0btosUniqueID\x18\x01 \x01(\t\x12\x12\n\ntwinMoveID\x18\x02 \x01(\t\"l\n\rLocationCheck\x12\x0c\n\x04\x61rea\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x0c\n\x04lane\x18\x03 \x01(\x11\x12\r\n\x05stack\x18\x04 \x01(\x11\x12\x0c\n\x04tier\x18\x05 \x01(\x11\x12\x13\n\x0borientation\x18\x06 \x01(\t\"{\n\x0eMovementCancel\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x15\n\requipmentName\x18\x04 \x01(\t\x12\x11\n\tequipType\x18\x05 \x01(\t\"o\n\x16MovementCancelResponse\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x14\n\x0c\x63\x61ncelResult\x18\x04 \x01(\x08\"\xbc\x01\n\x17MovementCreatedResponse\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\t\x12\x12\n\nstopStatus\x18\x04 \x01(\x08\x12L\n\x19movementInstructionStatus\x18\x05 \x03(\x0b\x32).Task_Scheduler.MovementInstructionStatus\"\x87\x04\n\x13MovementInstruction\x12\x18\n\x10movementUniqueID\x18\x01 \x01(\t\x12\x16\n\x0emovementStatus\x18\x02 \x01(\t\x12\x17\n\x0fmessageSequence\x18\x03 \x01(\x11\x12\x15\n\rworkQueueName\x18\x04 \x01(\t\x12\x14\n\x0cmovementType\x18\x05 \x01(\t\x12\x15\n\rtwinPickupGap\x18\x06 \x01(\x11\x12\x18\n\x10twinGroundingGap\x18\x07 \x01(\x11\x12\x15\n\requipmentName\x18\x08 \x01(\t\x12\x1e\n\x16teleoperatorAssistance\x18\t \x01(\t\x12&\n\x06origin\x18\n \x01(\x0b\x32\x16.Task_Scheduler.Origin\x12\x30\n\x0b\x64\x65stination\x18\x0b \x01(\x0b\x32\x1b.Task_Scheduler.Destination\x12\x17\n\x0foriginStartTime\x18\x0c \x01(\t\x12=\n\x10\x63ontainerDetails\x18\r \x01(\x0b\x32#.Task_Scheduler.ContainerDefinition\x12\x1a\n\x12\x61ssociatedTwinMove\x18\x0e \x01(\t\x12\x42\n\x14movementDependencies\x18\x0f \x03(\x0b\x32$.Task_Scheduler.DependencyDefinition\"\x86\x01\n\x19MovementInstructionStatus\x12\x18\n\x10movementUniqueID\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x15\n\requipmentName\x18\x03 \x01(\t\x12\x12\n\nrejectCode\x18\x04 \x03(\t\x12\x14\n\x0crejectReason\x18\x05 \x03(\t\"\xb1\x01\n\x14MovementInstructions\x12\x17\n\x0fmessageUniqueID\x18\x01 \x01(\t\x12\x13\n\x0bmessageName\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\t\x12\x15\n\rmessageSource\x18\x04 \x01(\t\x12\x41\n\x14movementInstructions\x18\x05 \x03(\x0b\x32#.Task_Scheduler.MovementInstruction\"o\n\x16MovementUpdateResponse\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\t\x12\x14\n\x0cupdateResult\x18\x04 \x01(\x08\"e\n\x06Origin\x12\x0c\n\x04\x61rea\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x0c\n\x04lane\x18\x03 \x01(\x11\x12\r\n\x05stack\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\x11\x12\x13\n\x0borientation\x18\x06 \x01(\t\"\x93\x03\n\x1fPlannedContainerDestinationDict\x12\x0c\n\x04\x61rea\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x0c\n\x04lane\x18\x03 \x01(\x11\x12\r\n\x05stack\x18\x04 \x01(\t\x12\x0c\n\x04tier\x18\x05 \x01(\x11\x12\x16\n\x0euniqueObjectID\x18\x06 \x01(\t\x12\x13\n\x0btargetReady\x18\x07 \x01(\x08\x12\x14\n\x0creeferStatus\x18\x08 \x01(\t\x12\x13\n\x0brelativePos\x18\t \x01(\t\x12\x19\n\x11\x64\x65stDoorDirection\x18\n \x01(\t\x12\x14\n\x0c\x63ontainerNum\x18\x0b \x01(\t\x12\x14\n\x0c\x63ontainerISO\x18\x0c \x01(\t\x12\x19\n\x11\x63ontainerLengthFT\x18\r \x01(\x02\x12\x17\n\x0f\x63ontainerHeight\x18\x0e \x01(\x02\x12\x19\n\x11\x63ontainerWeightKG\x18\x0f \x01(\x02\x12\x16\n\x0e\x63ontainerWidth\x18\x10 \x01(\x02\x12\"\n\x1a\x61ssociatedTwinContainer_id\x18\x11 \x01(\t\",\n\x0cPortLocation\x12\r\n\x05portX\x18\x01 \x01(\x02\x12\r\n\x05portY\x18\x02 \x01(\x02\"1\n\tStageData\x12\x12\n\njob_status\x18\x01 \x01(\t\x12\x10\n\x08job_lane\x18\x02 \x01(\t\"\xab\x01\n\x0eTOSOrderUpdate\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueID\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12 \n\x18updateOrderOperationType\x18\x04 \x01(\t\x12\x1b\n\x13updateOrderUniqueID\x18\x05 \x01(\t\x12\x19\n\x11updateOrderStatus\x18\x06 \x01(\x08\"9\n\x0fValidationError\x12\x0b\n\x03loc\x18\x01 \x03(\x11\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\xe5\x03\n\x0cVehicleOrder\x12\x13\n\x0bmessageName\x18\x01 \x01(\t\x12\x17\n\x0fmessageUniqueId\x18\x02 \x01(\t\x12\x18\n\x10messageTimestamp\x18\x03 \x01(\t\x12\x10\n\x08moveType\x18\x04 \x01(\t\x12\x15\n\runiqueOrderID\x18\x05 \x01(\t\x12\x0e\n\x06origin\x18\x06 \x01(\t\x12\x0f\n\x07jobType\x18\x07 \x01(\t\x12\x11\n\tvehicleID\x18\x08 \x01(\t\x12\x13\n\x0b\x62idirection\x18\t \x01(\x11\x12/\n\x0bjob_content\x18\n \x01(\x0b\x32\x1a.Task_Scheduler.JobContent\x12\x14\n\x0cmovementType\x18\x0b \x01(\t\x12\x38\n\x0b\x64\x65stination\x18\x0c \x01(\x0b\x32#.Task_Scheduler.ExecutorDestination\x12X\n\x1fplannedContainerDestinationList\x18\r \x03(\x0b\x32/.Task_Scheduler.PlannedContainerDestinationDict\x12\x12\n\nactionCode\x18\x0e \x01(\t\x12,\n\tstageData\x18\x0f \x01(\x0b\x32\x19.Task_Scheduler.StageData\"m\n\rWorkQueueInfo\x12\x12\n\nwork_queue\x18\x01 \x01(\t\x12H\n tos_to_scheduler_dependency_list\x18\x02 \x03(\x0b\x32\x1e.Task_Scheduler.DependencyInfo2\xab\x05\n\x0eTask_Scheduler\x12N\n\nreceive_mi\x12$.Task_Scheduler.MovementInstructions\x1a\x18.Task_Scheduler.Response\"\x00\x12=\n\x06remove\x12\x17.Task_Scheduler.Request\x1a\x18.Task_Scheduler.Response\"\x00\x12\x41\n\x02\x64\x63\x12\x1f.Task_Scheduler.DependencyCheck\x1a\x18.Task_Scheduler.Response\"\x00\x12\x44\n\x06\x63\x61ncel\x12\x1e.Task_Scheduler.MovementCancel\x1a\x18.Task_Scheduler.Response\"\x00\x12Z\n\x16receive_mi_update_post\x12$.Task_Scheduler.MovementInstructions\x1a\x18.Task_Scheduler.Response\"\x00\x12O\n\x13receive_action_code\x12\x1c.Task_Scheduler.VehicleOrder\x1a\x18.Task_Scheduler.Response\"\x00\x12J\n\x0corder_update\x12\x1e.Task_Scheduler.TOSOrderUpdate\x1a\x18.Task_Scheduler.Response\"\x00\x12?\n\x08\x63heck_sc\x12\x17.Task_Scheduler.Request\x1a\x18.Task_Scheduler.Response\"\x00\x12G\n\x10\x63heck_sc_details\x12\x17.Task_Scheduler.Request\x1a\x18.Task_Scheduler.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_scheduler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DEPENDENCYCHECKRESPONSE_DEPENDENCYLISTENTRY']._options = None
  _globals['_DEPENDENCYCHECKRESPONSE_DEPENDENCYLISTENTRY']._serialized_options = b'8\001'
  _globals['_REQUEST']._serialized_start=67
  _globals['_REQUEST']._serialized_end=112
  _globals['_RESPONSE']._serialized_start=114
  _globals['_RESPONSE']._serialized_end=228
  _globals['_ACTIONCODERESPONSE']._serialized_start=231
  _globals['_ACTIONCODERESPONSE']._serialized_end=417
  _globals['_CONTAINERDEFINITION']._serialized_start=420
  _globals['_CONTAINERDEFINITION']._serialized_end=792
  _globals['_DEPENDENCYCHECK']._serialized_start=794
  _globals['_DEPENDENCYCHECK']._serialized_end=918
  _globals['_DEPENDENCYCHECKRESPONSE']._serialized_start=921
  _globals['_DEPENDENCYCHECKRESPONSE']._serialized_end=1173
  _globals['_DEPENDENCYCHECKRESPONSE_DEPENDENCYLISTENTRY']._serialized_start=1098
  _globals['_DEPENDENCYCHECKRESPONSE_DEPENDENCYLISTENTRY']._serialized_end=1173
  _globals['_DEPENDENCYDEFINITION']._serialized_start=1175
  _globals['_DEPENDENCYDEFINITION']._serialized_end=1274
  _globals['_DEPENDENCYINFO']._serialized_start=1277
  _globals['_DEPENDENCYINFO']._serialized_end=1434
  _globals['_DEPENDENCYITEM']._serialized_start=1436
  _globals['_DEPENDENCYITEM']._serialized_end=1504
  _globals['_DESTINATION']._serialized_start=1506
  _globals['_DESTINATION']._serialized_end=1612
  _globals['_EXECUTORDESTINATION']._serialized_start=1615
  _globals['_EXECUTORDESTINATION']._serialized_end=1762
  _globals['_EXECUTORLOGICALLOCATION']._serialized_start=1764
  _globals['_EXECUTORLOGICALLOCATION']._serialized_end=1882
  _globals['_EXECUTORPORTLOCATION']._serialized_start=1884
  _globals['_EXECUTORPORTLOCATION']._serialized_end=1936
  _globals['_HTTPVALIDATIONERROR']._serialized_start=1938
  _globals['_HTTPVALIDATIONERROR']._serialized_end=2008
  _globals['_JOBCONTENT']._serialized_start=2010
  _globals['_JOBCONTENT']._serialized_end=2063
  _globals['_LOCATIONCHECK']._serialized_start=2065
  _globals['_LOCATIONCHECK']._serialized_end=2173
  _globals['_MOVEMENTCANCEL']._serialized_start=2175
  _globals['_MOVEMENTCANCEL']._serialized_end=2298
  _globals['_MOVEMENTCANCELRESPONSE']._serialized_start=2300
  _globals['_MOVEMENTCANCELRESPONSE']._serialized_end=2411
  _globals['_MOVEMENTCREATEDRESPONSE']._serialized_start=2414
  _globals['_MOVEMENTCREATEDRESPONSE']._serialized_end=2602
  _globals['_MOVEMENTINSTRUCTION']._serialized_start=2605
  _globals['_MOVEMENTINSTRUCTION']._serialized_end=3124
  _globals['_MOVEMENTINSTRUCTIONSTATUS']._serialized_start=3127
  _globals['_MOVEMENTINSTRUCTIONSTATUS']._serialized_end=3261
  _globals['_MOVEMENTINSTRUCTIONS']._serialized_start=3264
  _globals['_MOVEMENTINSTRUCTIONS']._serialized_end=3441
  _globals['_MOVEMENTUPDATERESPONSE']._serialized_start=3443
  _globals['_MOVEMENTUPDATERESPONSE']._serialized_end=3554
  _globals['_ORIGIN']._serialized_start=3556
  _globals['_ORIGIN']._serialized_end=3657
  _globals['_PLANNEDCONTAINERDESTINATIONDICT']._serialized_start=3660
  _globals['_PLANNEDCONTAINERDESTINATIONDICT']._serialized_end=4063
  _globals['_PORTLOCATION']._serialized_start=4065
  _globals['_PORTLOCATION']._serialized_end=4109
  _globals['_STAGEDATA']._serialized_start=4111
  _globals['_STAGEDATA']._serialized_end=4160
  _globals['_TOSORDERUPDATE']._serialized_start=4163
  _globals['_TOSORDERUPDATE']._serialized_end=4334
  _globals['_VALIDATIONERROR']._serialized_start=4336
  _globals['_VALIDATIONERROR']._serialized_end=4393
  _globals['_VEHICLEORDER']._serialized_start=4396
  _globals['_VEHICLEORDER']._serialized_end=4881
  _globals['_WORKQUEUEINFO']._serialized_start=4883
  _globals['_WORKQUEUEINFO']._serialized_end=4992
  _globals['_TASK_SCHEDULER']._serialized_start=4995
  _globals['_TASK_SCHEDULER']._serialized_end=5678
# @@protoc_insertion_point(module_scope)
