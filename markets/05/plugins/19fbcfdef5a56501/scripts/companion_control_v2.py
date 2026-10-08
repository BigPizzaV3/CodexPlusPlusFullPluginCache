# GENERATED FILE. DO NOT EDIT.
# Source: chatgpt-meetings-core/contracts/companion-control.v2.schema.json
# SHA-256: d6309d1d21648be83e96580befd92a276d925d355f0fc962c421b0156f58d0e1
# Regenerate: python3 chatgpt-meetings-core/scripts/generate_recording_control_stream_contract.py

# ruff: noqa: UP007 -- typing.Union preserves runtime Python 3.9 compatibility.

# Generated output must remain identical across repositories.
# fmt: off
from __future__ import annotations

import json
import re
from datetime import datetime
from typing import TYPE_CHECKING, Any, Final, Literal, TypedDict, Union

if TYPE_CHECKING:
    from typing import TypeGuard
else:
    try:
        from typing import TypeGuard
    except ImportError:
        class TypeGuard:
            @classmethod
            def __class_getitem__(cls, _value: object) -> type[bool]:
                return bool


PROTOCOL_VERSION: Final[int] = 2
FRAME_PREFIX_BYTES: Final[int] = 4
FRAME_PREFIX_BYTE_ORDER: Final[str] = 'little-endian'
MAX_FRAME_BYTES: Final[int] = 1048576
MAX_REQUEST_TTL_MILLIS: Final[int] = 5000
MAX_CLIENT_IDENTITIES: Final[int] = 64
MAX_CACHED_RESPONSES: Final[int] = 128
SCHEMA_SHA256: Final[str] = 'd6309d1d21648be83e96580befd92a276d925d355f0fc962c421b0156f58d0e1'
KNOWN_CAPABILITIES: Final[tuple[str, ...]] = ('recording.control.v2', 'client.context.v1', 'meetings.eligibility.v1', 'recording.calendar-context.v1', 'recording.audio-sources.v1', 'recording.recovery.v1', 'recording.encryption-errors.v1', 'recording.database-version-errors.v1', 'permissions.request.v1', 'settings.v2', 'settings.reminders.v1', 'settings.meeting-detection.v1', 'settings.sound-effects.v1', 'home.snapshot.v1', 'home.notes-source.v1', 'home.note-page-binding.v1', 'workspace.events.v1', 'lifecycle.update.v2', 'lifecycle.bootstrap-recovery.v1')
METHOD_CONTRACTS: Final[dict[str, dict[str, Any]]] = {'companion.initialize': {'requestSchemaRef': '#/$defs/InitializeRequest', 'resultSchemaRef': '#/$defs/InitializeResult', 'requiredCapabilities': []}, 'companion.getState': {'requestSchemaRef': '#/$defs/GetStateRequest', 'resultSchemaRef': '#/$defs/CompanionState', 'requiredCapabilities': ['recording.control.v2']}, 'client.setContext': {'requestSchemaRef': '#/$defs/SetClientContextRequest', 'resultSchemaRef': '#/$defs/RetryUploadResult', 'requiredCapabilities': ['client.context.v1']}, 'recording.start': {'requestSchemaRef': '#/$defs/StartRecordingRequest', 'resultSchemaRef': '#/$defs/CompanionState', 'requiredCapabilities': ['recording.control.v2'], 'fieldCapabilities': {'calendarContext': 'recording.calendar-context.v1'}}, 'recording.stop': {'requestSchemaRef': '#/$defs/StopRecordingRequest', 'resultSchemaRef': '#/$defs/StopRecordingResult', 'requiredCapabilities': ['recording.control.v2']}, 'recording.getUploads': {'requestSchemaRef': '#/$defs/GetUploadsRequest', 'resultSchemaRef': '#/$defs/UploadsResult', 'requiredCapabilities': ['recording.recovery.v1']}, 'recording.retry': {'requestSchemaRef': '#/$defs/RetryUploadRequest', 'resultSchemaRef': '#/$defs/RetryUploadResult', 'requiredCapabilities': ['recording.recovery.v1']}, 'permissions.recheck': {'requestSchemaRef': '#/$defs/RecheckPermissionsRequest', 'resultSchemaRef': '#/$defs/CompanionState', 'requiredCapabilities': ['recording.audio-sources.v1']}, 'permissions.request': {'requestSchemaRef': '#/$defs/RequestPermissionRequest', 'resultSchemaRef': '#/$defs/CompanionState', 'requiredCapabilities': ['permissions.request.v1']}, 'permissions.openSystemSettings': {'requestSchemaRef': '#/$defs/OpenSystemSettingsRequest', 'resultSchemaRef': '#/$defs/CompanionState', 'requiredCapabilities': ['permissions.request.v1']}, 'settings.get': {'requestSchemaRef': '#/$defs/GetSettingsRequest', 'resultSchemaRef': '#/$defs/SettingsState', 'requiredCapabilities': ['settings.v2'], 'fieldCapabilities': {'calendarRemindersEnabled': 'settings.reminders.v1', 'meetingDetectionEnabled': 'settings.meeting-detection.v1', 'soundEffectsEnabled': 'settings.sound-effects.v1'}}, 'settings.update': {'requestSchemaRef': '#/$defs/UpdateSettingsRequest', 'resultSchemaRef': '#/$defs/SettingsState', 'requiredCapabilities': ['settings.v2'], 'fieldCapabilities': {'calendarRemindersEnabled': 'settings.reminders.v1', 'meetingDetectionEnabled': 'settings.meeting-detection.v1', 'soundEffectsEnabled': 'settings.sound-effects.v1'}}, 'home.getSnapshot': {'requestSchemaRef': '#/$defs/GetHomeSnapshotRequest', 'resultSchemaRef': '#/$defs/HomeSnapshot', 'requiredCapabilities': ['home.snapshot.v1']}, 'lifecycle.quitForUpdate': {'requestSchemaRef': '#/$defs/QuitForUpdateRequest', 'resultSchemaRef': '#/$defs/QuitForUpdateResult', 'requiredCapabilities': ['lifecycle.update.v2']}}
NOTIFICATION_CONTRACTS: Final[dict[str, dict[str, Any]]] = {'companion.stateChanged': {'notificationSchemaRef': '#/$defs/StateChangedNotification', 'requiredCapabilities': ['recording.control.v2']}, 'recording.completed': {'notificationSchemaRef': '#/$defs/RecordingCompletedNotification', 'requiredCapabilities': ['recording.control.v2']}, 'workspace.changed': {'notificationSchemaRef': '#/$defs/WorkspaceChangedNotification', 'requiredCapabilities': ['workspace.events.v1']}}

_RESPONSE_SHAPES: Final[dict[str, Any]] = {'CompanionState': {'properties': {'accountScopeFingerprint': {}, 'lifecycle': {'properties': {'replacement': {'properties': {'allowed': {}, 'blockedReason': {}}}, 'bootstrapRecovery': {'properties': {'status': {}}}}}, 'recordingSummary': {'properties': {'capturing': {}, 'total': {}, 'stopped': {}, 'waitingForAuth': {}, 'creatingStream': {}, 'streaming': {}, 'finalizing': {}, 'delivered': {}, 'blocked': {}}}, 'recording': {'properties': {'phase': {}, 'session': {'properties': {'id': {}, 'startedAt': {}, 'meetingId': {}}}, 'controls': {'properties': {'start': {'properties': {'enabled': {}, 'disabledReason': {}}}, 'stop': {'properties': {'enabled': {}}}}}, 'audioSources': {'properties': {'microphone': {}, 'systemAudio': {}, 'warning': {}}}, 'permissions': {'properties': {'microphone': {'properties': {'canRequest': {}, 'status': {}}}, 'systemAudio': {'properties': {'canRequest': {}, 'status': {}}}}}, 'notice': {'properties': {'action': {'properties': {'kind': {}, 'permission': {}}}, 'kind': {}, 'message': {}}}}}, 'revision': {}, 'meetingsEligibility': {'properties': {'status': {}, 'decision': {'properties': {'canUseMeetings': {}, 'reason': {}, 'serviceCapacity': {}, 'pluginAvailability': {}, 'requiredUpdates': {'properties': {'app': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'plugin': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'codex': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}}}, 'platform': {}, 'client': {'properties': {'pluginVersion': {}, 'codexVersion': {}}}}}}}}}, 'HomeSnapshot': {'properties': {'accountScopeFingerprint': {}, 'calendar': {'properties': {'fetchedAt': {}, 'generatedAt': {}, 'truncated': {}, 'stale': {}, 'events': {'items': {'properties': {'id': {}, 'title': {}, 'startAtMillis': {}, 'endAtMillis': {}, 'meetingUrl': {}, 'responseStatus': {}}}}}}, 'notes': {'properties': {'source': {}, 'fetchedAt': {}, 'items': {'items': {'properties': {'id': {}, 'title': {}, 'startedAt': {}, 'endedAt': {}, 'status': {}, 'isEmpty': {}, 'numShareRecipients': {}, 'summaryPageId': {}, 'recordSource': {}, 'devicePlatform': {}}}}}}}}, 'InitializeResult': {'properties': {'protocolVersion': {}, 'ownerEpoch': {}, 'companionVersion': {}, 'capabilities': {'items': {}}, 'state': {'properties': {'accountScopeFingerprint': {}, 'lifecycle': {'properties': {'replacement': {'properties': {'allowed': {}, 'blockedReason': {}}}, 'bootstrapRecovery': {'properties': {'status': {}}}}}, 'recordingSummary': {'properties': {'capturing': {}, 'total': {}, 'stopped': {}, 'waitingForAuth': {}, 'creatingStream': {}, 'streaming': {}, 'finalizing': {}, 'delivered': {}, 'blocked': {}}}, 'recording': {'properties': {'phase': {}, 'session': {'properties': {'id': {}, 'startedAt': {}, 'meetingId': {}}}, 'controls': {'properties': {'start': {'properties': {'enabled': {}, 'disabledReason': {}}}, 'stop': {'properties': {'enabled': {}}}}}, 'audioSources': {'properties': {'microphone': {}, 'systemAudio': {}, 'warning': {}}}, 'permissions': {'properties': {'microphone': {'properties': {'canRequest': {}, 'status': {}}}, 'systemAudio': {'properties': {'canRequest': {}, 'status': {}}}}}, 'notice': {'properties': {'action': {'properties': {'kind': {}, 'permission': {}}}, 'kind': {}, 'message': {}}}}}, 'revision': {}, 'meetingsEligibility': {'properties': {'status': {}, 'decision': {'properties': {'canUseMeetings': {}, 'reason': {}, 'serviceCapacity': {}, 'pluginAvailability': {}, 'requiredUpdates': {'properties': {'app': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'plugin': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'codex': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}}}, 'platform': {}, 'client': {'properties': {'pluginVersion': {}, 'codexVersion': {}}}}}}}}}}}, 'JsonRpcError': {'properties': {'code': {}, 'message': {}, 'data': {'properties': {'kind': {}}}}}, 'QuitForUpdateResult': {'properties': {'disposition': {}, 'handoffId': {}, 'ownerEpoch': {}, 'captureAdmissionFenced': {}, 'reason': {}}}, 'RetryUploadResult': {'properties': {'accepted': {}}}, 'SettingsState': {'properties': {'canUpdate': {}, 'accountScopeFingerprint': {}, 'revision': {}, 'status': {}, 'values': {'properties': {'calendarRemindersEnabled': {}, 'meetingDetectionEnabled': {}, 'soundEffectsEnabled': {}}}, 'availability': {'properties': {'reminders': {}, 'meetingDetection': {}, 'soundEffects': {}}}}}, 'StopRecordingResult': {'properties': {'state': {'properties': {'accountScopeFingerprint': {}, 'lifecycle': {'properties': {'replacement': {'properties': {'allowed': {}, 'blockedReason': {}}}, 'bootstrapRecovery': {'properties': {'status': {}}}}}, 'recordingSummary': {'properties': {'capturing': {}, 'total': {}, 'stopped': {}, 'waitingForAuth': {}, 'creatingStream': {}, 'streaming': {}, 'finalizing': {}, 'delivered': {}, 'blocked': {}}}, 'recording': {'properties': {'phase': {}, 'session': {'properties': {'id': {}, 'startedAt': {}, 'meetingId': {}}}, 'controls': {'properties': {'start': {'properties': {'enabled': {}, 'disabledReason': {}}}, 'stop': {'properties': {'enabled': {}}}}}, 'audioSources': {'properties': {'microphone': {}, 'systemAudio': {}, 'warning': {}}}, 'permissions': {'properties': {'microphone': {'properties': {'canRequest': {}, 'status': {}}}, 'systemAudio': {'properties': {'canRequest': {}, 'status': {}}}}}, 'notice': {'properties': {'action': {'properties': {'kind': {}, 'permission': {}}}, 'kind': {}, 'message': {}}}}}, 'revision': {}, 'meetingsEligibility': {'properties': {'status': {}, 'decision': {'properties': {'canUseMeetings': {}, 'reason': {}, 'serviceCapacity': {}, 'pluginAvailability': {}, 'requiredUpdates': {'properties': {'app': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'plugin': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'codex': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}}}, 'platform': {}, 'client': {'properties': {'pluginVersion': {}, 'codexVersion': {}}}}}}}}}, 'completion': {'properties': {'sessionId': {}, 'outcome': {}}}}}, 'UploadsResult': {'properties': {'accountScopeFingerprint': {}, 'queue': {'properties': {'items': {'items': {'properties': {'recordingId': {}, 'phase': {}, 'createdAt': {}, 'audioDurationMs': {}, 'audioBytes': {}, 'canRetry': {}, 'failure': {'properties': {'stage': {}, 'category': {}, 'httpStatus': {}, 'attempt': {}, 'retryable': {}}}, 'memoryOnly': {}}}}, 'totalCount': {}, 'nextOffset': {}, 'revision': {}, 'historyFailure': {'properties': {'stage': {}, 'category': {}, 'httpStatus': {}, 'attempt': {}, 'retryable': {}}}, 'hasFailedUploads': {}, 'hasUploadsNeedingSignIn': {}}}}}, 'companion.stateChanged': {'properties': {'accountScopeFingerprint': {}, 'lifecycle': {'properties': {'replacement': {'properties': {'allowed': {}, 'blockedReason': {}}}, 'bootstrapRecovery': {'properties': {'status': {}}}}}, 'recordingSummary': {'properties': {'capturing': {}, 'total': {}, 'stopped': {}, 'waitingForAuth': {}, 'creatingStream': {}, 'streaming': {}, 'finalizing': {}, 'delivered': {}, 'blocked': {}}}, 'recording': {'properties': {'phase': {}, 'session': {'properties': {'id': {}, 'startedAt': {}, 'meetingId': {}}}, 'controls': {'properties': {'start': {'properties': {'enabled': {}, 'disabledReason': {}}}, 'stop': {'properties': {'enabled': {}}}}}, 'audioSources': {'properties': {'microphone': {}, 'systemAudio': {}, 'warning': {}}}, 'permissions': {'properties': {'microphone': {'properties': {'canRequest': {}, 'status': {}}}, 'systemAudio': {'properties': {'canRequest': {}, 'status': {}}}}}, 'notice': {'properties': {'action': {'properties': {'kind': {}, 'permission': {}}}, 'kind': {}, 'message': {}}}}}, 'revision': {}, 'meetingsEligibility': {'properties': {'status': {}, 'decision': {'properties': {'canUseMeetings': {}, 'reason': {}, 'serviceCapacity': {}, 'pluginAvailability': {}, 'requiredUpdates': {'properties': {'app': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'plugin': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}, 'codex': {'properties': {'status': {}, 'currentVersion': {}, 'minimumVersion': {}, 'warningVersion': {}}}}}, 'platform': {}, 'client': {'properties': {'pluginVersion': {}, 'codexVersion': {}}}}}}}}}, 'recording.completed': {'properties': {'sessionId': {}, 'outcome': {}}}, 'workspace.changed': {'properties': {'resource': {}, 'accountScopeFingerprint': {}}}}

_SCHEMA: dict[str, Any] = json.loads(
    '{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"https://schemas.openai.com/chat'
    'gpt-meetings/companion-control.v2.schema.json","title":"ChatGPT Meetings companion control proto'
    'col v2","description":"Authenticated local companion discovery and transport. Recording, uploads'
    ', recovery, background synchronization, and cached-data production remain companion-owned.","x-c'
    'ompanion-protocol-version":2,"x-frame-prefix-byte-order":"little-endian","x-frame-prefix-bytes":'
    '4,"x-max-frame-bytes":1048576,"x-max-request-ttl-millis":5000,"x-max-client-identities":64,"x-ma'
    'x-cached-responses":128,"x-method-contracts":{"companion.initialize":{"requestSchemaRef":"#/$def'
    's/InitializeRequest","resultSchemaRef":"#/$defs/InitializeResult","requiredCapabilities":[]},"co'
    'mpanion.getState":{"requestSchemaRef":"#/$defs/GetStateRequest","resultSchemaRef":"#/$defs/Compa'
    'nionState","requiredCapabilities":["recording.control.v2"]},"client.setContext":{"requestSchemaR'
    'ef":"#/$defs/SetClientContextRequest","resultSchemaRef":"#/$defs/RetryUploadResult","requiredCap'
    'abilities":["client.context.v1"]},"recording.start":{"requestSchemaRef":"#/$defs/StartRecordingR'
    'equest","resultSchemaRef":"#/$defs/CompanionState","requiredCapabilities":["recording.control.v2'
    '"],"fieldCapabilities":{"calendarContext":"recording.calendar-context.v1"}},"recording.stop":{"r'
    'equestSchemaRef":"#/$defs/StopRecordingRequest","resultSchemaRef":"#/$defs/StopRecordingResult",'
    '"requiredCapabilities":["recording.control.v2"]},"recording.getUploads":{"requestSchemaRef":"#/$'
    'defs/GetUploadsRequest","resultSchemaRef":"#/$defs/UploadsResult","requiredCapabilities":["recor'
    'ding.recovery.v1"]},"recording.retry":{"requestSchemaRef":"#/$defs/RetryUploadRequest","resultSc'
    'hemaRef":"#/$defs/RetryUploadResult","requiredCapabilities":["recording.recovery.v1"]},"permissi'
    'ons.recheck":{"requestSchemaRef":"#/$defs/RecheckPermissionsRequest","resultSchemaRef":"#/$defs/'
    'CompanionState","requiredCapabilities":["recording.audio-sources.v1"]},"permissions.request":{"r'
    'equestSchemaRef":"#/$defs/RequestPermissionRequest","resultSchemaRef":"#/$defs/CompanionState","'
    'requiredCapabilities":["permissions.request.v1"]},"permissions.openSystemSettings":{"requestSche'
    'maRef":"#/$defs/OpenSystemSettingsRequest","resultSchemaRef":"#/$defs/CompanionState","requiredC'
    'apabilities":["permissions.request.v1"]},"settings.get":{"requestSchemaRef":"#/$defs/GetSettings'
    'Request","resultSchemaRef":"#/$defs/SettingsState","requiredCapabilities":["settings.v2"],"field'
    'Capabilities":{"calendarRemindersEnabled":"settings.reminders.v1","meetingDetectionEnabled":"set'
    'tings.meeting-detection.v1","soundEffectsEnabled":"settings.sound-effects.v1"}},"settings.update'
    '":{"requestSchemaRef":"#/$defs/UpdateSettingsRequest","resultSchemaRef":"#/$defs/SettingsState",'
    '"requiredCapabilities":["settings.v2"],"fieldCapabilities":{"calendarRemindersEnabled":"settings'
    '.reminders.v1","meetingDetectionEnabled":"settings.meeting-detection.v1","soundEffectsEnabled":"'
    'settings.sound-effects.v1"}},"home.getSnapshot":{"requestSchemaRef":"#/$defs/GetHomeSnapshotRequ'
    'est","resultSchemaRef":"#/$defs/HomeSnapshot","requiredCapabilities":["home.snapshot.v1"]},"life'
    'cycle.quitForUpdate":{"requestSchemaRef":"#/$defs/QuitForUpdateRequest","resultSchemaRef":"#/$de'
    'fs/QuitForUpdateResult","requiredCapabilities":["lifecycle.update.v2"]}},"x-notification-contrac'
    'ts":{"companion.stateChanged":{"notificationSchemaRef":"#/$defs/StateChangedNotification","requi'
    'redCapabilities":["recording.control.v2"]},"recording.completed":{"notificationSchemaRef":"#/$de'
    'fs/RecordingCompletedNotification","requiredCapabilities":["recording.control.v2"]},"workspace.c'
    'hanged":{"notificationSchemaRef":"#/$defs/WorkspaceChangedNotification","requiredCapabilities":['
    '"workspace.events.v1"]}},"oneOf":[{"$ref":"#/$defs/Descriptor"},{"$ref":"#/$defs/Request"},{"$re'
    'f":"#/$defs/Response"},{"$ref":"#/$defs/Notification"}],"$defs":{"PositiveSafeInteger":{"type":"'
    'integer","minimum":1,"maximum":9007199254740991},"ExecutableIdentity":{"type":"object","required'
    '":["path","sha256"],"additionalProperties":false,"dependentRequired":{"device":["inode"],"inode"'
    ':["device"]},"properties":{"path":{"type":"string","minLength":1,"maxLength":4096,"not":{"patter'
    'n":"[\\\\u0000\\\\r\\\\n]"}},"sha256":{"type":"string","pattern":"^[a-f0-9]{64}$"},"device":{"$ref":"#'
    '/$defs/PositiveSafeInteger"},"inode":{"$ref":"#/$defs/PositiveSafeInteger"},"processStartedAtMil'
    'lis":{"$ref":"#/$defs/PositiveSafeInteger"}}},"Descriptor":{"type":"object","required":["protoco'
    'lVersion","ownerEpoch","pid","platform","architecture","transport","endpoint","companionVersion"'
    ',"requestTTLMillis","maxFrameBytes","executableIdentity"],"additionalProperties":false,"properti'
    'es":{"protocolVersion":{"const":2},"ownerEpoch":{"$ref":"#/$defs/OpaqueIdentifier"},"pid":{"type'
    '":"integer","minimum":1,"maximum":2147483647},"platform":{"enum":["macos","windows"]},"architect'
    'ure":{"enum":["arm64","x64","universal"]},"transport":{"enum":["unix-domain-socket","windows-nam'
    'ed-pipe"]},"endpoint":{"type":"string","minLength":1,"maxLength":4096,"not":{"pattern":"[\\\\u0000'
    '\\\\r\\\\n]"}},"companionVersion":{"type":"string","minLength":1,"maxLength":64},"requestTTLMillis":'
    '{"type":"integer","minimum":1,"maximum":5000},"maxFrameBytes":{"const":1048576},"executableIdent'
    'ity":{"$ref":"#/$defs/ExecutableIdentity"}},"allOf":[{"if":{"properties":{"platform":{"const":"m'
    'acos"}}},"then":{"properties":{"transport":{"const":"unix-domain-socket"}}}},{"if":{"properties"'
    ':{"platform":{"const":"windows"}}},"then":{"properties":{"transport":{"const":"windows-named-pip'
    'e"},"architecture":{"enum":["arm64","x64"]}}}}]},"ReplayMetadata":{"type":"object","required":["'
    'clientId","ownerEpoch","sequence","issuedAtMillis"],"additionalProperties":false,"properties":{"'
    'clientId":{"$ref":"#/$defs/OpaqueIdentifier"},"ownerEpoch":{"$ref":"#/$defs/OpaqueIdentifier"},"'
    'sequence":{"$ref":"#/$defs/PositiveSafeInteger"},"issuedAtMillis":{"$ref":"#/$defs/PositiveSafeI'
    'nteger"}}},"OpaqueIdentifier":{"type":"string","minLength":8,"maxLength":128,"pattern":"^[A-Za-z'
    '0-9_-]+$"},"AccountScopeFingerprint":{"type":"string","pattern":"^[a-f0-9]{64}$"},"SafeInteger":'
    '{"type":"integer","minimum":0,"maximum":9007199254740991},"Timestamp":{"type":"string","format":'
    '"date-time","maxLength":64},"Capability":{"type":"string","minLength":3,"maxLength":96,"pattern"'
    ':"^[a-z][a-z0-9.-]*\\\\.v[1-9][0-9]*$"},"KnownCapability":{"enum":["recording.control.v2","client.'
    'context.v1","meetings.eligibility.v1","recording.calendar-context.v1","recording.audio-sources.v'
    '1","recording.recovery.v1","recording.encryption-errors.v1","recording.database-version-errors.v'
    '1","permissions.request.v1","settings.v2","settings.reminders.v1","settings.meeting-detection.v1'
    '","settings.sound-effects.v1","home.snapshot.v1","home.notes-source.v1","home.note-page-binding.'
    'v1","workspace.events.v1","lifecycle.update.v2","lifecycle.bootstrap-recovery.v1"]},"CapabilityL'
    'ist":{"type":"array","items":{"$ref":"#/$defs/Capability"},"maxItems":32,"uniqueItems":true},"Js'
    'onRpcRequest":{"type":"object","required":["jsonrpc","id","method","params"],"additionalProperti'
    'es":false,"properties":{"jsonrpc":{"const":"2.0"},"id":{"$ref":"#/$defs/OpaqueIdentifier"},"meth'
    'od":{"type":"string","maxLength":64},"params":{"type":"object"},"meta":{"$ref":"#/$defs/ReplayMe'
    'tadata"}}},"AuthenticatedRequest":{"allOf":[{"$ref":"#/$defs/JsonRpcRequest"},{"required":["meta'
    '"]}]},"EmptyParams":{"type":"object","maxProperties":0},"InitializeRequest":{"allOf":[{"$ref":"#'
    '/$defs/JsonRpcRequest"},{"not":{"required":["meta"]},"properties":{"method":{"const":"companion.'
    'initialize"},"params":{"type":"object","required":["protocolVersion","client","requestedCapabili'
    'ties"],"additionalProperties":false,"properties":{"protocolVersion":{"const":2},"client":{"type"'
    ':"object","required":["id","kind","version"],"additionalProperties":false,"properties":{"id":{"$'
    'ref":"#/$defs/OpaqueIdentifier"},"kind":{"const":"meetings-mcp"},"version":{"type":"string","min'
    'Length":1,"maxLength":64}}},"requestedCapabilities":{"$ref":"#/$defs/CapabilityList"}}}}}]},"Set'
    'ClientContextRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"method":'
    '{"const":"client.setContext"},"params":{"type":"object","required":["codexAppVersion"],"addition'
    'alProperties":false,"properties":{"codexAppVersion":{"description":"Observed Codex desktop appli'
    'cation version, never the CLI or Meetings plugin version. Missing or unknown observations must n'
    'ot be sent or clear a prior observation.","type":"string","maxLength":128,"pattern":"^(0|[1-9][0'
    '-9]*)\\\\.(0|[1-9][0-9]*)\\\\.(0|[1-9][0-9]*)(-((0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)(\\\\.(0|['
    '1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?(\\\\+[0-9A-Za-z-]+(\\\\.[0-9A-Za-z-]+)*)?$(?![\\\\s\\\\S])'
    '"}}}}}]},"GetStateRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"met'
    'hod":{"const":"companion.getState"},"params":{"$ref":"#/$defs/EmptyParams"}}}]},"CalendarRecordi'
    'ngContext":{"type":"object","additionalProperties":false,"required":["accountScopeFingerprint","'
    'source","eventId","occurrenceStart","title"],"properties":{"accountScopeFingerprint":{"$ref":"#/'
    '$defs/AccountScopeFingerprint"},"source":{"const":"google_calendar"},"eventId":{"type":"string",'
    '"minLength":1,"maxLength":512},"occurrenceStart":{"$ref":"#/$defs/Timestamp"},"title":{"type":"s'
    'tring","maxLength":512}}},"StartRecordingRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedReques'
    't"},{"properties":{"method":{"const":"recording.start"},"params":{"type":"object","additionalPro'
    'perties":false,"properties":{"calendarContext":{"$ref":"#/$defs/CalendarRecordingContext"}}}}}]}'
    ',"StopRecordingRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"method'
    '":{"const":"recording.stop"},"params":{"type":"object","required":["expectedSessionId"],"additio'
    'nalProperties":false,"properties":{"expectedSessionId":{"$ref":"#/$defs/OpaqueIdentifier"}}}}}]}'
    ',"RecheckPermissionsRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"m'
    'ethod":{"const":"permissions.recheck"},"params":{"$ref":"#/$defs/EmptyParams"}}}]},"RequestPermi'
    'ssionRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"method":{"const"'
    ':"permissions.request"},"params":{"type":"object","required":["kind"],"additionalProperties":fal'
    'se,"properties":{"kind":{"enum":["microphone","systemAudio"]}}}}}]},"OpenSystemSettingsRequest":'
    '{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"method":{"const":"permissions.'
    'openSystemSettings"},"params":{"type":"object","required":["kind"],"additionalProperties":false,'
    '"properties":{"kind":{"enum":["microphone","systemAudio"]}}}}}]},"AccountScopeParams":{"type":"o'
    'bject","required":["accountScopeFingerprint"],"additionalProperties":false,"properties":{"accoun'
    'tScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerprint"}}},"UploadRecordingId":{"type":"str'
    'ing","pattern":"^recording-[a-f0-9]{64}$"},"GetUploadsParams":{"type":"object","required":["acco'
    'untScopeFingerprint"],"additionalProperties":false,"properties":{"accountScopeFingerprint":{"$re'
    'f":"#/$defs/AccountScopeFingerprint"},"offset":{"$ref":"#/$defs/SafeInteger","default":0}}},"Get'
    'UploadsRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"method":{"cons'
    't":"recording.getUploads"},"params":{"$ref":"#/$defs/GetUploadsParams"}}}]},"RetryUploadParams":'
    '{"type":"object","required":["accountScopeFingerprint","recordingId"],"additionalProperties":fal'
    'se,"properties":{"accountScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerprint"},"recording'
    'Id":{"$ref":"#/$defs/UploadRecordingId"}}},"RetryUploadRequest":{"allOf":[{"$ref":"#/$defs/Authe'
    'nticatedRequest"},{"properties":{"method":{"const":"recording.retry"},"params":{"$ref":"#/$defs/'
    'RetryUploadParams"}}}]},"GetSettingsRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{'
    '"properties":{"method":{"const":"settings.get"},"params":{"$ref":"#/$defs/AccountScopeParams"}}}'
    ']},"SettingsChanges":{"type":"object","minProperties":1,"additionalProperties":false,"properties'
    '":{"calendarRemindersEnabled":{"type":"boolean"},"meetingDetectionEnabled":{"type":"boolean"},"s'
    'oundEffectsEnabled":{"type":"boolean"}}},"UpdateSettingsRequest":{"allOf":[{"$ref":"#/$defs/Auth'
    'enticatedRequest"},{"properties":{"method":{"const":"settings.update"},"params":{"type":"object"'
    ',"required":["accountScopeFingerprint","changes"],"additionalProperties":false,"properties":{"ac'
    'countScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerprint"},"changes":{"$ref":"#/$defs/Set'
    'tingsChanges"}}}}}]},"GetHomeSnapshotRequest":{"allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},'
    '{"properties":{"method":{"const":"home.getSnapshot"},"params":{"type":"object","required":["acco'
    'untScopeFingerprint"],"additionalProperties":false,"properties":{"accountScopeFingerprint":{"$re'
    'f":"#/$defs/AccountScopeFingerprint"},"notesSource":{"enum":["meetings","private-notes"]},"inclu'
    'dePageBindings":{"type":"boolean"}}}}}]},"BootstrapRecoveryStatus":{"type":"string","enum":["res'
    'tartable","restarting","exhausted"]},"BootstrapRecovery":{"type":"object","required":["status"],'
    '"additionalProperties":false,"properties":{"status":{"$ref":"#/$defs/BootstrapRecoveryStatus"}}}'
    ',"QuitForUpdateReason":{"type":"string","enum":["bootstrap-recovery"]},"QuitForUpdateRequest":{"'
    'allOf":[{"$ref":"#/$defs/AuthenticatedRequest"},{"properties":{"method":{"const":"lifecycle.quit'
    'ForUpdate"},"params":{"type":"object","required":["expectedOwnerEpoch"],"additionalProperties":f'
    'alse,"properties":{"expectedOwnerEpoch":{"$ref":"#/$defs/OpaqueIdentifier"},"reason":{"$ref":"#/'
    '$defs/QuitForUpdateReason"}}}}}]},"Request":{"oneOf":[{"$ref":"#/$defs/InitializeRequest"},{"$re'
    'f":"#/$defs/SetClientContextRequest"},{"$ref":"#/$defs/GetStateRequest"},{"$ref":"#/$defs/StartR'
    'ecordingRequest"},{"$ref":"#/$defs/StopRecordingRequest"},{"$ref":"#/$defs/GetUploadsRequest"},{'
    '"$ref":"#/$defs/RetryUploadRequest"},{"$ref":"#/$defs/RecheckPermissionsRequest"},{"$ref":"#/$de'
    'fs/RequestPermissionRequest"},{"$ref":"#/$defs/OpenSystemSettingsRequest"},{"$ref":"#/$defs/GetS'
    'ettingsRequest"},{"$ref":"#/$defs/UpdateSettingsRequest"},{"$ref":"#/$defs/GetHomeSnapshotReques'
    't"},{"$ref":"#/$defs/QuitForUpdateRequest"}]},"Permission":{"type":"object","required":["status"'
    ',"canRequest"],"additionalProperties":false,"properties":{"status":{"enum":["granted","promptabl'
    'e","denied","unsupported","unknown"]},"canRequest":{"type":"boolean"}},"if":{"properties":{"stat'
    'us":{"const":"promptable"}}},"then":{"properties":{"canRequest":{"const":true}}},"else":{"proper'
    'ties":{"canRequest":{"const":false}}}},"StartControl":{"oneOf":[{"type":"object","required":["en'
    'abled","disabledReason"],"additionalProperties":false,"properties":{"enabled":{"const":true},"di'
    'sabledReason":{"type":"null"}}},{"type":"object","required":["enabled","disabledReason"],"additi'
    'onalProperties":false,"properties":{"enabled":{"const":false},"disabledReason":{"enum":["recordi'
    'ng-active","permission-required","permission-denied","companion-unavailable","recording-unavaila'
    'ble","update-in-progress"]}}}]},"StopControl":{"type":"object","required":["enabled"],"additiona'
    'lProperties":false,"properties":{"enabled":{"type":"boolean"}}},"RecordingSession":{"type":"obje'
    'ct","required":["id","startedAt"],"additionalProperties":false,"properties":{"id":{"$ref":"#/$de'
    'fs/OpaqueIdentifier"},"startedAt":{"$ref":"#/$defs/Timestamp"},"meetingId":{"$ref":"#/$defs/Opaq'
    'ueIdentifier"}}},"RecordingNoticeAction":{"oneOf":[{"type":"object","required":["kind","permissi'
    'on"],"additionalProperties":false,"properties":{"kind":{"const":"request-permission"},"permissio'
    'n":{"enum":["microphone","systemAudio"]}}},{"type":"object","required":["kind","permission"],"ad'
    'ditionalProperties":false,"properties":{"kind":{"const":"open-system-settings"},"permission":{"e'
    'num":["microphone","systemAudio"]}}},{"type":"object","required":["kind"],"additionalProperties"'
    ':false,"properties":{"kind":{"const":"retry-stop"}}},{"type":"object","required":["kind"],"addit'
    'ionalProperties":false,"properties":{"kind":{"const":"recheck-audio"}}}]},"RecordingNotice":{"ty'
    'pe":"object","required":["kind","message","action"],"additionalProperties":false,"properties":{"'
    'kind":{"enum":["permission-required","permission-denied","recording-unavailable","finalization-f'
    'ailed","companion-unavailable"]},"message":{"type":"string","minLength":1,"maxLength":256},"acti'
    'on":{"anyOf":[{"$ref":"#/$defs/RecordingNoticeAction"},{"type":"null"}]}},"allOf":[{"if":{"prope'
    'rties":{"kind":{"const":"permission-required"}}},"then":{"properties":{"action":{"type":"object"'
    ',"properties":{"kind":{"const":"request-permission"}}}}}},{"if":{"properties":{"kind":{"const":"'
    'permission-denied"}}},"then":{"properties":{"action":{"type":"object","properties":{"kind":{"con'
    'st":"open-system-settings"}}}}}},{"if":{"properties":{"kind":{"const":"finalization-failed"}}},"'
    'then":{"properties":{"action":{"type":"object","properties":{"kind":{"const":"retry-stop"}}}}}},'
    '{"if":{"properties":{"kind":{"const":"recording-unavailable"}}},"then":{"properties":{"action":{'
    '"anyOf":[{"type":"null"},{"type":"object","properties":{"kind":{"const":"recheck-audio"}}}]}}}},'
    '{"if":{"properties":{"kind":{"const":"companion-unavailable"}}},"then":{"properties":{"action":{'
    '"type":"null"}}}}]},"AudioSourceStatus":{"type":"string","enum":["ready","device-absent","permis'
    'sion-denied","permission-required","unavailable"]},"AudioSources":{"type":"object","required":["'
    'microphone","systemAudio","warning"],"additionalProperties":false,"properties":{"microphone":{"$'
    'ref":"#/$defs/AudioSourceStatus"},"systemAudio":{"$ref":"#/$defs/AudioSourceStatus"},"warning":{'
    '"anyOf":[{"type":"string","minLength":1,"maxLength":256},{"type":"null"}]}}},"RecordingPresentat'
    'ion":{"type":"object","required":["phase","session","controls","permissions","notice"],"addition'
    'alProperties":false,"properties":{"phase":{"enum":["idle","starting","recording","stopping","una'
    'vailable"]},"session":{"anyOf":[{"$ref":"#/$defs/RecordingSession"},{"type":"null"}]},"controls"'
    ':{"type":"object","required":["start","stop"],"additionalProperties":false,"properties":{"start"'
    ':{"$ref":"#/$defs/StartControl"},"stop":{"$ref":"#/$defs/StopControl"}}},"permissions":{"type":"'
    'object","required":["microphone","systemAudio"],"additionalProperties":false,"properties":{"micr'
    'ophone":{"$ref":"#/$defs/Permission"},"systemAudio":{"$ref":"#/$defs/Permission"}}},"notice":{"a'
    'nyOf":[{"$ref":"#/$defs/RecordingNotice"},{"type":"null"}]},"audioSources":{"$ref":"#/$defs/Audi'
    'oSources"}},"allOf":[{"if":{"required":["audioSources"],"properties":{"controls":{"properties":{'
    '"start":{"properties":{"enabled":{"const":true}}}}}}},"then":{"properties":{"audioSources":{"one'
    'Of":[{"properties":{"microphone":{"const":"ready"},"systemAudio":{"const":"ready"}}},{"propertie'
    's":{"microphone":{"const":"ready"},"systemAudio":{"const":"device-absent"}}},{"properties":{"mic'
    'rophone":{"const":"device-absent"},"systemAudio":{"const":"ready"}}}]}}}},{"if":{"properties":{"'
    'controls":{"properties":{"stop":{"properties":{"enabled":{"const":true}}}}}}},"then":{"propertie'
    's":{"session":{"$ref":"#/$defs/RecordingSession"}}}},{"if":{"properties":{"phase":{"const":"idle'
    '"}}},"then":{"properties":{"session":{"type":"null"},"controls":{"properties":{"stop":{"properti'
    'es":{"enabled":{"const":false}}}}}}}},{"if":{"properties":{"phase":{"const":"starting"}}},"then"'
    ':{"properties":{"controls":{"properties":{"start":{"properties":{"enabled":{"const":false}}},"st'
    'op":{"properties":{"enabled":{"const":false}}}}}}}},{"if":{"properties":{"phase":{"const":"recor'
    'ding"}}},"then":{"properties":{"session":{"$ref":"#/$defs/RecordingSession"},"controls":{"proper'
    'ties":{"start":{"properties":{"enabled":{"const":false},"disabledReason":{"const":"recording-act'
    'ive"}}},"stop":{"properties":{"enabled":{"const":true}}}}}}}},{"if":{"properties":{"phase":{"con'
    'st":"stopping"}}},"then":{"properties":{"session":{"$ref":"#/$defs/RecordingSession"},"controls"'
    ':{"properties":{"start":{"properties":{"enabled":{"const":false},"disabledReason":{"const":"reco'
    'rding-active"}}}}}}}},{"if":{"properties":{"phase":{"const":"unavailable"}}},"then":{"properties'
    '":{"session":{"type":"null"},"controls":{"properties":{"start":{"properties":{"enabled":{"const"'
    ':false}}},"stop":{"properties":{"enabled":{"const":false}}}}}}}},{"if":{"properties":{"controls"'
    ':{"properties":{"start":{"properties":{"enabled":{"const":true}}}}}}},"then":{"properties":{"pha'
    'se":{"const":"idle"}}}},{"if":{"properties":{"notice":{"type":"object","properties":{"kind":{"co'
    'nst":"finalization-failed"}}}}},"then":{"properties":{"phase":{"const":"stopping"},"session":{"$'
    'ref":"#/$defs/RecordingSession"},"controls":{"properties":{"stop":{"properties":{"enabled":{"con'
    'st":true}}}}}}}}]},"ReplacementAvailability":{"oneOf":[{"type":"object","required":["allowed","b'
    'lockedReason"],"additionalProperties":false,"properties":{"allowed":{"const":true},"blockedReaso'
    'n":{"type":"null"}}},{"type":"object","required":["allowed","blockedReason"],"additionalProperti'
    'es":false,"properties":{"allowed":{"const":false},"blockedReason":{"enum":["recording-active","r'
    'ecording-starting","recording-stopping","owner-unavailable"]}}}]},"RecordingSummary":{"type":"ob'
    'ject","required":["total","capturing","stopped","waitingForAuth","creatingStream","streaming","f'
    'inalizing","delivered","blocked"],"additionalProperties":false,"properties":{"total":{"$ref":"#/'
    '$defs/SafeInteger"},"capturing":{"$ref":"#/$defs/SafeInteger"},"stopped":{"$ref":"#/$defs/SafeIn'
    'teger"},"waitingForAuth":{"$ref":"#/$defs/SafeInteger"},"creatingStream":{"$ref":"#/$defs/SafeIn'
    'teger"},"streaming":{"$ref":"#/$defs/SafeInteger"},"finalizing":{"$ref":"#/$defs/SafeInteger"},"'
    'delivered":{"$ref":"#/$defs/SafeInteger"},"blocked":{"$ref":"#/$defs/SafeInteger"}}},"UploadPhas'
    'e":{"enum":["idle","uploading","uploaded","needs-sign-in","failed"]},"UploadFailureStage":{"enum'
    '":["session-create","stream-resume","audio-delivery","finalization","full-audio-upload","receipt'
    '-validation","local-recovery"]},"UploadFailureCategory":{"enum":["invalid-request","invalid-cred'
    'ential","authorization-changed","buffer-full","session-closed","offline","timeout","tls","http-r'
    'ejected","invalid-response","protocol-violation","cancelled","internal","encryption-key-missing"'
    ',"decryption-failed","database-too-new","missing-audio","corrupt-audio","unsafe-audio","invalid-'
    'receipt","invalid-acknowledgment","unknown"]},"UploadFailure":{"type":"object","required":["stag'
    'e","category","attempt","retryable"],"additionalProperties":false,"properties":{"stage":{"$ref":'
    '"#/$defs/UploadFailureStage"},"category":{"$ref":"#/$defs/UploadFailureCategory"},"httpStatus":{'
    '"type":"integer","minimum":100,"maximum":599},"attempt":{"type":"integer","minimum":0,"maximum":'
    '9999},"retryable":{"type":"boolean"}}},"UploadItem":{"type":"object","required":["recordingId","'
    'phase","createdAt","audioDurationMs","audioBytes","canRetry"],"additionalProperties":false,"prop'
    'erties":{"recordingId":{"$ref":"#/$defs/UploadRecordingId"},"phase":{"$ref":"#/$defs/UploadPhase'
    '"},"createdAt":{"$ref":"#/$defs/Timestamp"},"audioDurationMs":{"$ref":"#/$defs/SafeInteger"},"au'
    'dioBytes":{"$ref":"#/$defs/SafeInteger"},"canRetry":{"type":"boolean"},"failure":{"$ref":"#/$def'
    's/UploadFailure"},"memoryOnly":{"type":"boolean"}}},"UploadQueue":{"type":"object","required":["'
    'items","totalCount","nextOffset","revision","hasFailedUploads","hasUploadsNeedingSignIn"],"addit'
    'ionalProperties":false,"properties":{"items":{"type":"array","maxItems":24,"items":{"$ref":"#/$d'
    'efs/UploadItem"}},"totalCount":{"$ref":"#/$defs/SafeInteger"},"nextOffset":{"anyOf":[{"$ref":"#/'
    '$defs/SafeInteger"},{"type":"null"}]},"revision":{"type":"string","minLength":64,"maxLength":64,'
    '"pattern":"^[a-f0-9]{64}$"},"historyFailure":{"$ref":"#/$defs/UploadFailure"},"hasFailedUploads"'
    ':{"type":"boolean"},"hasUploadsNeedingSignIn":{"type":"boolean"}}},"UploadsResult":{"type":"obje'
    'ct","required":["accountScopeFingerprint","queue"],"additionalProperties":false,"properties":{"a'
    'ccountScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerprint"},"queue":{"$ref":"#/$defs/Uplo'
    'adQueue"}}},"RetryUploadResult":{"type":"object","required":["accepted"],"additionalProperties":'
    'false,"properties":{"accepted":{"const":true}}},"EligibilityUpdateStatus":{"enum":["none","warni'
    'ng","required"]},"EligibilityUpdate":{"type":"object","required":["status","currentVersion","min'
    'imumVersion","warningVersion"],"additionalProperties":false,"properties":{"status":{"$ref":"#/$d'
    'efs/EligibilityUpdateStatus"},"currentVersion":{"type":"string","maxLength":128},"minimumVersion'
    '":{"type":"string","maxLength":128},"warningVersion":{"type":"string","maxLength":128}}},"Eligib'
    'ilityUpdates":{"type":"object","required":["app","plugin","codex"],"additionalProperties":false,'
    '"properties":{"app":{"$ref":"#/$defs/EligibilityUpdate"},"plugin":{"$ref":"#/$defs/EligibilityUp'
    'date"},"codex":{"$ref":"#/$defs/EligibilityUpdate"}}},"EligibilityCapacity":{"enum":["off","warn'
    'ing","blocked"]},"EligibilityAvailability":{"enum":["available","coming_soon"]},"EligibilityReas'
    'on":{"enum":["capacity","availability","app_update","codex_update","plugin_update","context_unav'
    'ailable"]},"EligibilityClient":{"type":"object","required":["pluginVersion"],"additionalProperti'
    'es":false,"properties":{"pluginVersion":{"type":"string","maxLength":128},"codexVersion":{"type"'
    ':"string","maxLength":128}}},"MeetingsEligibilityDecision":{"type":"object","required":["canUseM'
    'eetings","serviceCapacity","pluginAvailability","requiredUpdates","platform","client"],"addition'
    'alProperties":false,"properties":{"canUseMeetings":{"type":"boolean"},"reason":{"$ref":"#/$defs/'
    'EligibilityReason"},"serviceCapacity":{"$ref":"#/$defs/EligibilityCapacity"},"pluginAvailability'
    '":{"$ref":"#/$defs/EligibilityAvailability"},"requiredUpdates":{"$ref":"#/$defs/EligibilityUpdat'
    'es"},"platform":{"enum":["macos","windows"]},"client":{"$ref":"#/$defs/EligibilityClient"}},"all'
    'Of":[{"if":{"properties":{"canUseMeetings":{"const":true}}},"then":{"not":{"required":["reason"]'
    '}},"else":{"required":["reason"]}}]},"EligibilityStatus":{"enum":["unresolved","resolved","error'
    '"]},"MeetingsEligibility":{"type":"object","required":["status"],"additionalProperties":false,"p'
    'roperties":{"status":{"$ref":"#/$defs/EligibilityStatus"},"decision":{"$ref":"#/$defs/MeetingsEl'
    'igibilityDecision"}},"description":"Native accepted policy only, independent of audio and record'
    'ing state. Error may retain a last accepted decision for the same authenticated account. Never p'
    'erforms network I/O when read.","allOf":[{"if":{"properties":{"status":{"const":"resolved"}}},"t'
    'hen":{"required":["decision"]}},{"if":{"properties":{"status":{"const":"unresolved"}}},"then":{"'
    'not":{"required":["decision"]}}}]},"CompanionState":{"type":"object","required":["revision","acc'
    'ountScopeFingerprint","recording","lifecycle"],"additionalProperties":false,"properties":{"revis'
    'ion":{"$ref":"#/$defs/SafeInteger"},"accountScopeFingerprint":{"anyOf":[{"$ref":"#/$defs/Account'
    'ScopeFingerprint"},{"type":"null"}]},"recording":{"$ref":"#/$defs/RecordingPresentation"},"recor'
    'dingSummary":{"$ref":"#/$defs/RecordingSummary"},"meetingsEligibility":{"$ref":"#/$defs/Meetings'
    'Eligibility"},"lifecycle":{"type":"object","required":["replacement"],"additionalProperties":fal'
    'se,"properties":{"replacement":{"$ref":"#/$defs/ReplacementAvailability"},"bootstrapRecovery":{"'
    '$ref":"#/$defs/BootstrapRecovery"}}}},"allOf":[{"if":{"required":["meetingsEligibility"],"proper'
    'ties":{"meetingsEligibility":{"required":["decision"]}}},"then":{"properties":{"accountScopeFing'
    'erprint":{"$ref":"#/$defs/AccountScopeFingerprint"}}}},{"if":{"properties":{"recording":{"proper'
    'ties":{"phase":{"const":"starting"}}}}},"then":{"properties":{"lifecycle":{"properties":{"replac'
    'ement":{"properties":{"allowed":{"const":false},"blockedReason":{"const":"recording-starting"}}}'
    '}}}}},{"if":{"properties":{"recording":{"properties":{"phase":{"const":"recording"}}}}},"then":{'
    '"properties":{"lifecycle":{"properties":{"replacement":{"properties":{"allowed":{"const":false},'
    '"blockedReason":{"const":"recording-active"}}}}}}}},{"if":{"properties":{"recording":{"propertie'
    's":{"phase":{"const":"stopping"}}}}},"then":{"properties":{"lifecycle":{"properties":{"replaceme'
    'nt":{"properties":{"allowed":{"const":false},"blockedReason":{"const":"recording-stopping"}}}}}}'
    '}},{"if":{"properties":{"recording":{"properties":{"phase":{"const":"unavailable"}}}}},"then":{"'
    'properties":{"lifecycle":{"properties":{"replacement":{"properties":{"allowed":{"const":false},"'
    'blockedReason":{"const":"owner-unavailable"}}}}}}}},{"if":{"properties":{"lifecycle":{"required"'
    ':["bootstrapRecovery"]}}},"then":{"properties":{"recordingSummary":{"properties":{"capturing":{"'
    'const":0}}},"recording":{"properties":{"phase":{"const":"unavailable"},"session":{"type":"null"}'
    ',"controls":{"properties":{"start":{"properties":{"enabled":{"const":false}}},"stop":{"propertie'
    's":{"enabled":{"const":false}}}}}}},"lifecycle":{"properties":{"replacement":{"properties":{"all'
    'owed":{"const":false}}}}}}}}]},"InitializeResult":{"type":"object","required":["protocolVersion"'
    ',"ownerEpoch","companionVersion","capabilities","state"],"additionalProperties":false,"propertie'
    's":{"protocolVersion":{"const":2},"ownerEpoch":{"$ref":"#/$defs/OpaqueIdentifier"},"companionVer'
    'sion":{"type":"string","minLength":1,"maxLength":64},"capabilities":{"$ref":"#/$defs/CapabilityL'
    'ist"},"state":{"$ref":"#/$defs/CompanionState"}}},"SettingsState":{"type":"object","required":["'
    'accountScopeFingerprint","revision","status","canUpdate","values","availability"],"additionalPro'
    'perties":false,"properties":{"accountScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerprint"'
    '},"revision":{"$ref":"#/$defs/SafeInteger"},"status":{"enum":["ready","saving","unavailable"]},"'
    'canUpdate":{"type":"boolean"},"values":{"type":"object","additionalProperties":false,"properties'
    '":{"calendarRemindersEnabled":{"type":"boolean"},"meetingDetectionEnabled":{"type":"boolean"},"s'
    'oundEffectsEnabled":{"type":"boolean"}}},"availability":{"type":"object","additionalProperties":'
    'false,"properties":{"reminders":{"type":"boolean"},"meetingDetection":{"type":"boolean"},"soundE'
    'ffects":{"type":"boolean"}}}},"if":{"properties":{"status":{"enum":["saving","unavailable"]}}},"'
    'then":{"properties":{"canUpdate":{"const":false}}}},"MeetingUrl":{"type":"string","minLength":9,'
    '"maxLength":2048,"pattern":"^https://"},"CalendarEvent":{"type":"object","required":["id","title'
    '","startAtMillis","endAtMillis","meetingUrl","responseStatus"],"additionalProperties":false,"pro'
    'perties":{"id":{"type":"string","minLength":1,"maxLength":512,"description":"Exact upstream host'
    'ed Calendar event identifier; never replace it with a synthetic or hashed ID."},"title":{"type":'
    '"string","maxLength":512},"startAtMillis":{"$ref":"#/$defs/SafeInteger"},"endAtMillis":{"$ref":"'
    '#/$defs/SafeInteger"},"meetingUrl":{"anyOf":[{"$ref":"#/$defs/MeetingUrl"},{"type":"null"}]},"re'
    'sponseStatus":{"enum":["accepted","tentative","declined","unknown"]}}},"CalendarSnapshot":{"type'
    '":"object","required":["fetchedAt","generatedAt","truncated","stale","events"],"additionalProper'
    'ties":false,"properties":{"fetchedAt":{"$ref":"#/$defs/Timestamp"},"generatedAt":{"$ref":"#/$def'
    's/Timestamp"},"truncated":{"type":"boolean"},"stale":{"type":"boolean"},"events":{"type":"array"'
    ',"maxItems":100,"items":{"$ref":"#/$defs/CalendarEvent"}}}},"MeetingNote":{"type":"object","requ'
    'ired":["id","title","startedAt","endedAt","status","isEmpty","numShareRecipients"],"additionalPr'
    'operties":false,"properties":{"id":{"type":"string","minLength":1,"maxLength":512},"title":{"typ'
    'e":"string","maxLength":512},"startedAt":{"$ref":"#/$defs/Timestamp"},"endedAt":{"anyOf":[{"$ref'
    '":"#/$defs/Timestamp"},{"type":"null"}]},"status":{"enum":["ready","joining","waiting","recordin'
    'g","uploading","processing","failed"]},"isEmpty":{"type":"boolean"},"numShareRecipients":{"$ref"'
    ':"#/$defs/SafeInteger"},"summaryPageId":{"type":"string","pattern":"^page_[0-9a-f]{32}$"},"recor'
    'dSource":{"type":"string","minLength":1,"maxLength":256},"devicePlatform":{"enum":["ios","androi'
    'd"]}}},"NotesSnapshot":{"type":"object","required":["fetchedAt","items"],"additionalProperties":'
    'false,"properties":{"source":{"enum":["meetings","private-notes"]},"fetchedAt":{"$ref":"#/$defs/'
    'Timestamp"},"items":{"type":"array","maxItems":20,"items":{"$ref":"#/$defs/MeetingNote"}}}},"Hom'
    'eSnapshot":{"type":"object","required":["accountScopeFingerprint","calendar","notes"],"additiona'
    'lProperties":false,"properties":{"accountScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerpr'
    'int"},"calendar":{"anyOf":[{"$ref":"#/$defs/CalendarSnapshot"},{"type":"null"}]},"notes":{"anyOf'
    '":[{"$ref":"#/$defs/NotesSnapshot"},{"type":"null"}]}}},"RecordingCompletion":{"type":"object","'
    'required":["sessionId","outcome"],"additionalProperties":false,"properties":{"sessionId":{"$ref"'
    ':"#/$defs/OpaqueIdentifier"},"outcome":{"const":"saved"}}},"StopRecordingResult":{"type":"object'
    '","required":["state"],"additionalProperties":false,"properties":{"state":{"$ref":"#/$defs/Compa'
    'nionState"},"completion":{"$ref":"#/$defs/RecordingCompletion"}}},"QuitForUpdateResult":{"oneOf"'
    ':[{"type":"object","required":["disposition","handoffId","ownerEpoch","captureAdmissionFenced"],'
    '"additionalProperties":false,"properties":{"disposition":{"const":"accepted"},"handoffId":{"$ref'
    '":"#/$defs/OpaqueIdentifier"},"ownerEpoch":{"$ref":"#/$defs/OpaqueIdentifier"},"captureAdmission'
    'Fenced":{"const":true}}},{"type":"object","required":["disposition","reason"],"additionalPropert'
    'ies":false,"properties":{"disposition":{"const":"blocked"},"reason":{"enum":["recording-active",'
    '"recording-starting","recording-stopping","owner-unavailable"]}}}]},"SuccessResult":{"oneOf":[{"'
    '$ref":"#/$defs/InitializeResult"},{"$ref":"#/$defs/CompanionState"},{"$ref":"#/$defs/SettingsSta'
    'te"},{"$ref":"#/$defs/HomeSnapshot"},{"$ref":"#/$defs/StopRecordingResult"},{"$ref":"#/$defs/Upl'
    'oadsResult"},{"$ref":"#/$defs/RetryUploadResult"},{"$ref":"#/$defs/QuitForUpdateResult"}]},"Erro'
    'rKind":{"enum":["unsupported-protocol","unsupported-capability","invalid-arguments","owner-chang'
    'ed","account-changed","session-mismatch","recording-active","recording-unavailable","permission-'
    'required","permission-denied","settings-unavailable","update-blocked","operation-cancelled","ope'
    'ration-ambiguous"]},"JsonRpcError":{"type":"object","required":["code","message","data"],"additi'
    'onalProperties":false,"properties":{"code":{"type":"integer","minimum":-32768,"maximum":-32000},'
    '"message":{"type":"string","minLength":1,"maxLength":256},"data":{"type":"object","required":["k'
    'ind"],"additionalProperties":false,"properties":{"kind":{"$ref":"#/$defs/ErrorKind"}}}}},"Respon'
    'se":{"oneOf":[{"type":"object","required":["jsonrpc","id","result"],"additionalProperties":false'
    ',"properties":{"jsonrpc":{"const":"2.0"},"id":{"$ref":"#/$defs/OpaqueIdentifier"},"result":{"$re'
    'f":"#/$defs/SuccessResult"}}},{"type":"object","required":["jsonrpc","id","error"],"additionalPr'
    'operties":false,"properties":{"jsonrpc":{"const":"2.0"},"id":{"$ref":"#/$defs/OpaqueIdentifier"}'
    ',"error":{"$ref":"#/$defs/JsonRpcError"}}}]},"StateChangedNotification":{"type":"object","requir'
    'ed":["jsonrpc","method","params"],"additionalProperties":false,"properties":{"jsonrpc":{"const":'
    '"2.0"},"method":{"const":"companion.stateChanged"},"params":{"$ref":"#/$defs/CompanionState"}}},'
    '"RecordingCompletedNotification":{"type":"object","required":["jsonrpc","method","params"],"addi'
    'tionalProperties":false,"properties":{"jsonrpc":{"const":"2.0"},"method":{"const":"recording.com'
    'pleted"},"params":{"$ref":"#/$defs/RecordingCompletion"}}},"WorkspaceChangedNotification":{"type'
    '":"object","required":["jsonrpc","method","params"],"additionalProperties":false,"properties":{"'
    'jsonrpc":{"const":"2.0"},"method":{"const":"workspace.changed"},"params":{"type":"object","requi'
    'red":["resource","accountScopeFingerprint"],"additionalProperties":false,"properties":{"resource'
    '":{"enum":["calendar","notes"]},"accountScopeFingerprint":{"$ref":"#/$defs/AccountScopeFingerpri'
    'nt"}}}}},"Notification":{"oneOf":[{"$ref":"#/$defs/StateChangedNotification"},{"$ref":"#/$defs/R'
    'ecordingCompletedNotification"},{"$ref":"#/$defs/WorkspaceChangedNotification"}]}}}'
)


PositiveSafeInteger = int


class _ExecutableIdentityRequired(TypedDict):
    path: str
    sha256: str


class ExecutableIdentity(_ExecutableIdentityRequired, total=False):
    device: PositiveSafeInteger
    inode: PositiveSafeInteger
    processStartedAtMillis: PositiveSafeInteger


class Descriptor(TypedDict):
    protocolVersion: Literal[2]
    ownerEpoch: OpaqueIdentifier
    pid: int
    platform: Literal['macos', 'windows']
    architecture: Literal['arm64', 'x64', 'universal']
    transport: Literal['unix-domain-socket', 'windows-named-pipe']
    endpoint: str
    companionVersion: str
    requestTTLMillis: int
    maxFrameBytes: Literal[1048576]
    executableIdentity: ExecutableIdentity


class ReplayMetadata(TypedDict):
    clientId: OpaqueIdentifier
    ownerEpoch: OpaqueIdentifier
    sequence: PositiveSafeInteger
    issuedAtMillis: PositiveSafeInteger


OpaqueIdentifier = str


AccountScopeFingerprint = str


SafeInteger = int


Timestamp = str


Capability = str


KnownCapability = Literal['recording.control.v2', 'client.context.v1', 'meetings.eligibility.v1', 'recording.calendar-context.v1', 'recording.audio-sources.v1', 'recording.recovery.v1', 'recording.encryption-errors.v1', 'recording.database-version-errors.v1', 'permissions.request.v1', 'settings.v2', 'settings.reminders.v1', 'settings.meeting-detection.v1', 'settings.sound-effects.v1', 'home.snapshot.v1', 'home.notes-source.v1', 'home.note-page-binding.v1', 'workspace.events.v1', 'lifecycle.update.v2', 'lifecycle.bootstrap-recovery.v1']


CapabilityList = list[Capability]


class _JsonRpcRequestRequired(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: str
    params: dict[str, object]


class JsonRpcRequest(_JsonRpcRequestRequired, total=False):
    meta: ReplayMetadata


class AuthenticatedRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: str
    params: dict[str, object]
    meta: ReplayMetadata


class EmptyParams(TypedDict):
    pass


class InitializeRequestParamsClient(TypedDict):
    id: OpaqueIdentifier
    kind: Literal['meetings-mcp']
    version: str


class InitializeRequestParams(TypedDict):
    protocolVersion: Literal[2]
    client: InitializeRequestParamsClient
    requestedCapabilities: CapabilityList


class _InitializeRequestRequired(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['companion.initialize']
    params: InitializeRequestParams


class InitializeRequest(_InitializeRequestRequired, total=False):
    meta: ReplayMetadata


class SetClientContextRequestParams(TypedDict):
    codexAppVersion: str


class SetClientContextRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['client.setContext']
    params: SetClientContextRequestParams
    meta: ReplayMetadata


class GetStateRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['companion.getState']
    params: EmptyParams
    meta: ReplayMetadata


class CalendarRecordingContext(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint
    source: Literal['google_calendar']
    eventId: str
    occurrenceStart: Timestamp
    title: str


class _StartRecordingRequestParamsRequired(TypedDict):
    pass


class StartRecordingRequestParams(_StartRecordingRequestParamsRequired, total=False):
    calendarContext: CalendarRecordingContext


class StartRecordingRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['recording.start']
    params: StartRecordingRequestParams
    meta: ReplayMetadata


class StopRecordingRequestParams(TypedDict):
    expectedSessionId: OpaqueIdentifier


class StopRecordingRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['recording.stop']
    params: StopRecordingRequestParams
    meta: ReplayMetadata


class RecheckPermissionsRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['permissions.recheck']
    params: EmptyParams
    meta: ReplayMetadata


class RequestPermissionRequestParams(TypedDict):
    kind: Literal['microphone', 'systemAudio']


class RequestPermissionRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['permissions.request']
    params: RequestPermissionRequestParams
    meta: ReplayMetadata


class OpenSystemSettingsRequestParams(TypedDict):
    kind: Literal['microphone', 'systemAudio']


class OpenSystemSettingsRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['permissions.openSystemSettings']
    params: OpenSystemSettingsRequestParams
    meta: ReplayMetadata


class AccountScopeParams(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint


UploadRecordingId = str


class _GetUploadsParamsRequired(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint


class GetUploadsParams(_GetUploadsParamsRequired, total=False):
    offset: SafeInteger


class GetUploadsRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['recording.getUploads']
    params: GetUploadsParams
    meta: ReplayMetadata


class RetryUploadParams(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint
    recordingId: UploadRecordingId


class RetryUploadRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['recording.retry']
    params: RetryUploadParams
    meta: ReplayMetadata


class GetSettingsRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['settings.get']
    params: AccountScopeParams
    meta: ReplayMetadata


class _SettingsChangesRequired(TypedDict):
    pass


class SettingsChanges(_SettingsChangesRequired, total=False):
    calendarRemindersEnabled: bool
    meetingDetectionEnabled: bool
    soundEffectsEnabled: bool


class UpdateSettingsRequestParams(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint
    changes: SettingsChanges


class UpdateSettingsRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['settings.update']
    params: UpdateSettingsRequestParams
    meta: ReplayMetadata


class _GetHomeSnapshotRequestParamsRequired(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint


class GetHomeSnapshotRequestParams(_GetHomeSnapshotRequestParamsRequired, total=False):
    notesSource: Literal['meetings', 'private-notes']
    includePageBindings: bool


class GetHomeSnapshotRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['home.getSnapshot']
    params: GetHomeSnapshotRequestParams
    meta: ReplayMetadata


BootstrapRecoveryStatus = Literal['restartable', 'restarting', 'exhausted']


class BootstrapRecovery(TypedDict):
    status: BootstrapRecoveryStatus


QuitForUpdateReason = Literal['bootstrap-recovery']


class _QuitForUpdateRequestParamsRequired(TypedDict):
    expectedOwnerEpoch: OpaqueIdentifier


class QuitForUpdateRequestParams(_QuitForUpdateRequestParamsRequired, total=False):
    reason: QuitForUpdateReason


class QuitForUpdateRequest(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    method: Literal['lifecycle.quitForUpdate']
    params: QuitForUpdateRequestParams
    meta: ReplayMetadata


Request = Union[InitializeRequest, SetClientContextRequest, GetStateRequest, StartRecordingRequest, StopRecordingRequest, GetUploadsRequest, RetryUploadRequest, RecheckPermissionsRequest, RequestPermissionRequest, OpenSystemSettingsRequest, GetSettingsRequest, UpdateSettingsRequest, GetHomeSnapshotRequest, QuitForUpdateRequest]


class Permission(TypedDict):
    status: Literal['granted', 'promptable', 'denied', 'unsupported', 'unknown']
    canRequest: bool


class StartControlEnabled(TypedDict):
    enabled: Literal[True]
    disabledReason: None


class StartControlDisabled(TypedDict):
    enabled: Literal[False]
    disabledReason: Literal['recording-active', 'permission-required', 'permission-denied', 'companion-unavailable', 'recording-unavailable', 'update-in-progress']


StartControl = Union[StartControlEnabled, StartControlDisabled]


class StopControl(TypedDict):
    enabled: bool


class _RecordingSessionRequired(TypedDict):
    id: OpaqueIdentifier
    startedAt: Timestamp


class RecordingSession(_RecordingSessionRequired, total=False):
    meetingId: OpaqueIdentifier


class RecordingNoticeActionRequestPermission(TypedDict):
    kind: Literal['request-permission']
    permission: Literal['microphone', 'systemAudio']


class RecordingNoticeActionOpenSystemSettings(TypedDict):
    kind: Literal['open-system-settings']
    permission: Literal['microphone', 'systemAudio']


class RecordingNoticeActionRetryStop(TypedDict):
    kind: Literal['retry-stop']


class RecordingNoticeActionRecheckAudio(TypedDict):
    kind: Literal['recheck-audio']


RecordingNoticeAction = Union[RecordingNoticeActionRequestPermission, RecordingNoticeActionOpenSystemSettings, RecordingNoticeActionRetryStop, RecordingNoticeActionRecheckAudio]


class RecordingNotice(TypedDict):
    kind: Literal['permission-required', 'permission-denied', 'recording-unavailable', 'finalization-failed', 'companion-unavailable']
    message: str
    action: Union[RecordingNoticeAction, None]


AudioSourceStatus = Literal['ready', 'device-absent', 'permission-denied', 'permission-required', 'unavailable']


class AudioSources(TypedDict):
    microphone: AudioSourceStatus
    systemAudio: AudioSourceStatus
    warning: Union[str, None]


class RecordingPresentationControls(TypedDict):
    start: StartControl
    stop: StopControl


class RecordingPresentationPermissions(TypedDict):
    microphone: Permission
    systemAudio: Permission


class _RecordingPresentationRequired(TypedDict):
    phase: Literal['idle', 'starting', 'recording', 'stopping', 'unavailable']
    session: Union[RecordingSession, None]
    controls: RecordingPresentationControls
    permissions: RecordingPresentationPermissions
    notice: Union[RecordingNotice, None]


class RecordingPresentation(_RecordingPresentationRequired, total=False):
    audioSources: AudioSources


class ReplacementAvailabilityAllowed(TypedDict):
    allowed: Literal[True]
    blockedReason: None


class ReplacementAvailabilityBlocked(TypedDict):
    allowed: Literal[False]
    blockedReason: Literal['recording-active', 'recording-starting', 'recording-stopping', 'owner-unavailable']


ReplacementAvailability = Union[ReplacementAvailabilityAllowed, ReplacementAvailabilityBlocked]


class RecordingSummary(TypedDict):
    total: SafeInteger
    capturing: SafeInteger
    stopped: SafeInteger
    waitingForAuth: SafeInteger
    creatingStream: SafeInteger
    streaming: SafeInteger
    finalizing: SafeInteger
    delivered: SafeInteger
    blocked: SafeInteger


UploadPhase = Literal['idle', 'uploading', 'uploaded', 'needs-sign-in', 'failed']


UploadFailureStage = Literal['session-create', 'stream-resume', 'audio-delivery', 'finalization', 'full-audio-upload', 'receipt-validation', 'local-recovery']


UploadFailureCategory = Literal['invalid-request', 'invalid-credential', 'authorization-changed', 'buffer-full', 'session-closed', 'offline', 'timeout', 'tls', 'http-rejected', 'invalid-response', 'protocol-violation', 'cancelled', 'internal', 'encryption-key-missing', 'decryption-failed', 'database-too-new', 'missing-audio', 'corrupt-audio', 'unsafe-audio', 'invalid-receipt', 'invalid-acknowledgment', 'unknown']


class _UploadFailureRequired(TypedDict):
    stage: UploadFailureStage
    category: UploadFailureCategory
    attempt: int
    retryable: bool


class UploadFailure(_UploadFailureRequired, total=False):
    httpStatus: int


class _UploadItemRequired(TypedDict):
    recordingId: UploadRecordingId
    phase: UploadPhase
    createdAt: Timestamp
    audioDurationMs: SafeInteger
    audioBytes: SafeInteger
    canRetry: bool


class UploadItem(_UploadItemRequired, total=False):
    failure: UploadFailure
    memoryOnly: bool


class _UploadQueueRequired(TypedDict):
    items: list[UploadItem]
    totalCount: SafeInteger
    nextOffset: Union[SafeInteger, None]
    revision: str
    hasFailedUploads: bool
    hasUploadsNeedingSignIn: bool


class UploadQueue(_UploadQueueRequired, total=False):
    historyFailure: UploadFailure


class UploadsResult(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint
    queue: UploadQueue


class RetryUploadResult(TypedDict):
    accepted: Literal[True]


EligibilityUpdateStatus = Literal['none', 'warning', 'required']


class EligibilityUpdate(TypedDict):
    status: EligibilityUpdateStatus
    currentVersion: str
    minimumVersion: str
    warningVersion: str


class EligibilityUpdates(TypedDict):
    app: EligibilityUpdate
    plugin: EligibilityUpdate
    codex: EligibilityUpdate


EligibilityCapacity = Literal['off', 'warning', 'blocked']


EligibilityAvailability = Literal['available', 'coming_soon']


EligibilityReason = Literal['capacity', 'availability', 'app_update', 'codex_update', 'plugin_update', 'context_unavailable']


class _EligibilityClientRequired(TypedDict):
    pluginVersion: str


class EligibilityClient(_EligibilityClientRequired, total=False):
    codexVersion: str


class _MeetingsEligibilityDecisionRequired(TypedDict):
    canUseMeetings: bool
    serviceCapacity: EligibilityCapacity
    pluginAvailability: EligibilityAvailability
    requiredUpdates: EligibilityUpdates
    platform: Literal['macos', 'windows']
    client: EligibilityClient


class MeetingsEligibilityDecision(_MeetingsEligibilityDecisionRequired, total=False):
    reason: EligibilityReason


EligibilityStatus = Literal['unresolved', 'resolved', 'error']


class _MeetingsEligibilityRequired(TypedDict):
    status: EligibilityStatus


class MeetingsEligibility(_MeetingsEligibilityRequired, total=False):
    decision: MeetingsEligibilityDecision


class _CompanionStateLifecycleRequired(TypedDict):
    replacement: ReplacementAvailability


class CompanionStateLifecycle(_CompanionStateLifecycleRequired, total=False):
    bootstrapRecovery: BootstrapRecovery


class _CompanionStateRequired(TypedDict):
    revision: SafeInteger
    accountScopeFingerprint: Union[AccountScopeFingerprint, None]
    recording: RecordingPresentation
    lifecycle: CompanionStateLifecycle


class CompanionState(_CompanionStateRequired, total=False):
    recordingSummary: RecordingSummary
    meetingsEligibility: MeetingsEligibility


class InitializeResult(TypedDict):
    protocolVersion: Literal[2]
    ownerEpoch: OpaqueIdentifier
    companionVersion: str
    capabilities: CapabilityList
    state: CompanionState


class _SettingsStateValuesRequired(TypedDict):
    pass


class SettingsStateValues(_SettingsStateValuesRequired, total=False):
    calendarRemindersEnabled: bool
    meetingDetectionEnabled: bool
    soundEffectsEnabled: bool


class _SettingsStateAvailabilityRequired(TypedDict):
    pass


class SettingsStateAvailability(_SettingsStateAvailabilityRequired, total=False):
    reminders: bool
    meetingDetection: bool
    soundEffects: bool


class SettingsState(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint
    revision: SafeInteger
    status: Literal['ready', 'saving', 'unavailable']
    canUpdate: bool
    values: SettingsStateValues
    availability: SettingsStateAvailability


MeetingUrl = str


class CalendarEvent(TypedDict):
    id: str
    title: str
    startAtMillis: SafeInteger
    endAtMillis: SafeInteger
    meetingUrl: Union[MeetingUrl, None]
    responseStatus: Literal['accepted', 'tentative', 'declined', 'unknown']


class CalendarSnapshot(TypedDict):
    fetchedAt: Timestamp
    generatedAt: Timestamp
    truncated: bool
    stale: bool
    events: list[CalendarEvent]


class _MeetingNoteRequired(TypedDict):
    id: str
    title: str
    startedAt: Timestamp
    endedAt: Union[Timestamp, None]
    status: Literal['ready', 'joining', 'waiting', 'recording', 'uploading', 'processing', 'failed']
    isEmpty: bool
    numShareRecipients: SafeInteger


class MeetingNote(_MeetingNoteRequired, total=False):
    summaryPageId: str
    recordSource: str
    devicePlatform: Literal['ios', 'android']


class _NotesSnapshotRequired(TypedDict):
    fetchedAt: Timestamp
    items: list[MeetingNote]


class NotesSnapshot(_NotesSnapshotRequired, total=False):
    source: Literal['meetings', 'private-notes']


class HomeSnapshot(TypedDict):
    accountScopeFingerprint: AccountScopeFingerprint
    calendar: Union[CalendarSnapshot, None]
    notes: Union[NotesSnapshot, None]


class RecordingCompletion(TypedDict):
    sessionId: OpaqueIdentifier
    outcome: Literal['saved']


class _StopRecordingResultRequired(TypedDict):
    state: CompanionState


class StopRecordingResult(_StopRecordingResultRequired, total=False):
    completion: RecordingCompletion


class QuitForUpdateResultAccepted(TypedDict):
    disposition: Literal['accepted']
    handoffId: OpaqueIdentifier
    ownerEpoch: OpaqueIdentifier
    captureAdmissionFenced: Literal[True]


class QuitForUpdateResultBlocked(TypedDict):
    disposition: Literal['blocked']
    reason: Literal['recording-active', 'recording-starting', 'recording-stopping', 'owner-unavailable']


QuitForUpdateResult = Union[QuitForUpdateResultAccepted, QuitForUpdateResultBlocked]


SuccessResult = Union[InitializeResult, CompanionState, SettingsState, HomeSnapshot, StopRecordingResult, UploadsResult, RetryUploadResult, QuitForUpdateResult]


ErrorKind = Literal['unsupported-protocol', 'unsupported-capability', 'invalid-arguments', 'owner-changed', 'account-changed', 'session-mismatch', 'recording-active', 'recording-unavailable', 'permission-required', 'permission-denied', 'settings-unavailable', 'update-blocked', 'operation-cancelled', 'operation-ambiguous']


class JsonRpcErrorData(TypedDict):
    kind: ErrorKind


class JsonRpcError(TypedDict):
    code: int
    message: str
    data: JsonRpcErrorData


class ResponseSuccess(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    result: SuccessResult


class ResponseError(TypedDict):
    jsonrpc: Literal['2.0']
    id: OpaqueIdentifier
    error: JsonRpcError


Response = Union[ResponseSuccess, ResponseError]


class StateChangedNotification(TypedDict):
    jsonrpc: Literal['2.0']
    method: Literal['companion.stateChanged']
    params: CompanionState


class RecordingCompletedNotification(TypedDict):
    jsonrpc: Literal['2.0']
    method: Literal['recording.completed']
    params: RecordingCompletion


class WorkspaceChangedNotificationParams(TypedDict):
    resource: Literal['calendar', 'notes']
    accountScopeFingerprint: AccountScopeFingerprint


class WorkspaceChangedNotification(TypedDict):
    jsonrpc: Literal['2.0']
    method: Literal['workspace.changed']
    params: WorkspaceChangedNotificationParams


Notification = Union[StateChangedNotification, RecordingCompletedNotification, WorkspaceChangedNotification]


def _same_json(left: object, right: object) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return isinstance(left, bool) and isinstance(right, bool) and left is right
    return left == right


def _valid_type(kind: str, value: object) -> bool:
    if kind == "object":
        return isinstance(value, dict)
    if kind == "array":
        return isinstance(value, list)
    if kind == "string":
        return isinstance(value, str)
    if kind == "boolean":
        return isinstance(value, bool)
    if kind == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if kind == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return value is None if kind == "null" else False


def _valid(schema: dict[str, object], value: object) -> bool:
    reference = schema.get("$ref")
    if isinstance(reference, str):
        definition = reference.removeprefix("#/$defs/")
        return _valid(_SCHEMA["$defs"][definition], value)
    for key, requirement in (("allOf", all), ("anyOf", any)):
        branches = schema.get(key)
        if isinstance(branches, list) and not requirement(_valid(branch, value) for branch in branches):
            return False
    branches = schema.get("oneOf")
    if isinstance(branches, list) and sum(_valid(branch, value) for branch in branches) != 1:
        return False
    forbidden = schema.get("not")
    if isinstance(forbidden, dict) and _valid(forbidden, value):
        return False
    conditional = schema.get("if")
    if isinstance(conditional, dict):
        branch = schema.get("then" if _valid(conditional, value) else "else")
        if isinstance(branch, dict) and not _valid(branch, value):
            return False
    kind = schema.get("type")
    if isinstance(kind, str) and not _valid_type(kind, value):
        return False
    if "const" in schema and not _same_json(value, schema["const"]):
        return False
    enumeration = schema.get("enum")
    if isinstance(enumeration, list) and not any(_same_json(value, item) for item in enumeration):
        return False
    if isinstance(value, dict):
        required = schema.get("required", [])
        if not isinstance(required, list):
            return False
        if any(key not in value for key in required):
            return False
        minimum = schema.get("minProperties")
        maximum = schema.get("maxProperties")
        if isinstance(minimum, int) and len(value) < minimum:
            return False
        if isinstance(maximum, int) and len(value) > maximum:
            return False
        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            return False
        if schema.get("additionalProperties") is False and not set(value).issubset(properties):
            return False
        for key, child in properties.items():
            if key in value and not _valid(child, value[key]):
                return False
        dependent_required = schema.get("dependentRequired", {})
        if not isinstance(dependent_required, dict):
            return False
        for key, dependencies in dependent_required.items():
            if not isinstance(dependencies, list):
                return False
            if key in value and any(dependency not in value for dependency in dependencies):
                return False
    if isinstance(value, list):
        minimum = schema.get("minItems")
        maximum = schema.get("maxItems")
        if isinstance(minimum, int) and len(value) < minimum:
            return False
        if isinstance(maximum, int) and len(value) > maximum:
            return False
        items = schema.get("items")
        if isinstance(items, dict) and not all(_valid(items, item) for item in value):
            return False
        if schema.get("uniqueItems"):
            identities = [json.dumps(item, sort_keys=True, separators=(",", ":")) for item in value]
            if len(identities) != len(set(identities)):
                return False
    if isinstance(value, str):
        minimum = schema.get("minLength")
        maximum = schema.get("maxLength")
        if isinstance(minimum, int) and len(value) < minimum:
            return False
        if isinstance(maximum, int) and len(value) > maximum:
            return False
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, value) is None:
            return False
        if schema.get("format") == "date-time":
            try:
                parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                return False
            if parsed.tzinfo is None:
                return False
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        maximum = schema.get("maximum")
        if isinstance(minimum, (int, float)) and value < minimum:
            return False
        if isinstance(maximum, (int, float)) and value > maximum:
            return False
    return True


def validate_definition(name: str, value: object) -> bool:
    definition = _SCHEMA["$defs"].get(name)
    return isinstance(definition, dict) and _valid(definition, value)


def is_descriptor(value: object) -> TypeGuard[Descriptor]:
    return validate_definition("Descriptor", value)


def is_request(value: object) -> TypeGuard[Request]:
    return validate_definition("Request", value)


def is_response(value: object) -> TypeGuard[Response]:
    return validate_definition("Response", value)


def is_notification(value: object) -> TypeGuard[Notification]:
    return validate_definition("Notification", value)


def is_initialize_result(value: object) -> TypeGuard[InitializeResult]:
    return validate_definition("InitializeResult", value)


def is_companion_state(value: object) -> TypeGuard[CompanionState]:
    return validate_definition("CompanionState", value)


def is_recording_completion(value: object) -> TypeGuard[RecordingCompletion]:
    return validate_definition("RecordingCompletion", value)


def is_stop_recording_result(value: object) -> TypeGuard[StopRecordingResult]:
    return validate_definition("StopRecordingResult", value)


def is_quit_for_update_result(value: object) -> TypeGuard[QuitForUpdateResult]:
    return validate_definition("QuitForUpdateResult", value)


def is_settings_state(value: object) -> TypeGuard[SettingsState]:
    return validate_definition("SettingsState", value)


def is_uploads_result(value: object) -> TypeGuard[UploadsResult]:
    return validate_definition("UploadsResult", value)


def is_retry_upload_result(value: object) -> TypeGuard[RetryUploadResult]:
    return validate_definition("RetryUploadResult", value)


def is_home_snapshot(value: object) -> TypeGuard[HomeSnapshot]:
    if not isinstance(value, dict) or not validate_definition("HomeSnapshot", value):
        return False
    calendar = value.get("calendar")
    return calendar is None or all(
        event["endAtMillis"] >= event["startAtMillis"] for event in calendar["events"]
    )


def _project_known(shape: dict[str, Any], value: object) -> object:
    properties = shape.get("properties")
    if isinstance(value, dict) and isinstance(properties, dict):
        return {key: _project_known(child, value[key]) for key, child in properties.items() if key in value}
    items = shape.get("items")
    if isinstance(value, list) and isinstance(items, dict):
        return [_project_known(items, item) for item in value]
    return value


def parse_initialize_result(value: object) -> InitializeResult | None:
    # Discard additive response fields before validating or caching native state.
    projected = _project_known(_RESPONSE_SHAPES["InitializeResult"], value)
    return projected if is_initialize_result(projected) else None


def parse_response(response: object, request: object, negotiated_capabilities: object = ()) -> Response | None:
    # Project payload metadata, retaining strict envelope and authority checks.
    if not isinstance(response, dict) or not is_request(request):
        return None
    projected = dict(response)
    if "result" in projected:
        name = METHOD_CONTRACTS[request["method"]]["resultSchemaRef"].removeprefix("#/$defs/")
        projected["result"] = _project_known(_RESPONSE_SHAPES[name], projected["result"])
    if "error" in projected:
        projected["error"] = _project_known(_RESPONSE_SHAPES["JsonRpcError"], projected["error"])
    if response_matches_request(projected, request, negotiated_capabilities):
        return projected
    return None


def parse_notification(value: object, negotiated_capabilities: object) -> Notification | None:
    # Discard unknown payload fields without accepting new notification methods.
    if not isinstance(value, dict) or not isinstance(value.get("method"), str):
        return None
    contract = NOTIFICATION_CONTRACTS.get(value["method"])
    if contract is None:
        return None
    projected = dict(value)
    if "params" in projected:
        projected["params"] = _project_known(_RESPONSE_SHAPES[value["method"]], projected["params"])
    if notification_is_authorized(projected, negotiated_capabilities):
        return projected
    return None


def _eligibility_field_is_authorized(state: object, capabilities: object) -> bool:
    return (isinstance(state, dict) and "meetingsEligibility" not in state) or (
        isinstance(capabilities, (list, tuple, set, frozenset))
        and "meetings.eligibility.v1" in capabilities
    )


def _settings_fields_are_authorized(
    values: object, availability: object, field_capabilities: dict[str, str], negotiated: set[str]
) -> bool:
    if not isinstance(values, dict) or not isinstance(availability, dict):
        return False
    availability_fields = {"reminders": "calendarRemindersEnabled", "meetingDetection": "meetingDetectionEnabled", "soundEffects": "soundEffectsEnabled"}
    for field in values:
        if field_capabilities.get(field) not in negotiated:
            return False
    for field in availability:
        if field_capabilities.get(availability_fields.get(field, "")) not in negotiated:
            return False
    return True


def request_is_authorized(value: object, negotiated_capabilities: object) -> bool:
    if not is_request(value) or not isinstance(negotiated_capabilities, (list, tuple, set, frozenset)):
        return False
    method = value["method"]
    contract = METHOD_CONTRACTS.get(method)
    if contract is None:
        return False
    negotiated = set(negotiated_capabilities).intersection(KNOWN_CAPABILITIES)
    if not set(contract["requiredCapabilities"]).issubset(negotiated):
        return False
    if method == "lifecycle.quitForUpdate" and "reason" in value["params"]:
        return "lifecycle.bootstrap-recovery.v1" in negotiated
    if method == "recording.start" and "calendarContext" in value["params"]:
        return "recording.calendar-context.v1" in negotiated
    if method == "settings.update":
        params = value["params"]
        changes = params.get("changes")
        if not isinstance(changes, dict):
            return False
        return all(
            contract.get("fieldCapabilities", {}).get(field) in negotiated for field in changes
        )
    return True


def response_matches_request(
    response: object,
    request: object,
    negotiated_capabilities: object = (),
) -> TypeGuard[Response]:
    if not is_response(response) or not is_request(request):
        return False
    if response["id"] != request["id"]:
        return False
    if "error" in response:
        return True
    contract = METHOD_CONTRACTS.get(request["method"])
    if contract is None:
        return False
    result = response["result"]
    if not validate_definition(contract["resultSchemaRef"].removeprefix("#/$defs/"), result):
        return False
    if request["method"] == "companion.initialize":
        if not _eligibility_field_is_authorized(result.get("state"), result.get("capabilities")):
            return False
    elif request["method"] == "recording.stop":
        if not _eligibility_field_is_authorized(result.get("state"), negotiated_capabilities):
            return False
    elif contract["resultSchemaRef"] == "#/$defs/CompanionState":
        if not _eligibility_field_is_authorized(result, negotiated_capabilities):
            return False
    if request["method"] == "home.getSnapshot" and not is_home_snapshot(result):
        return False
    if request["method"] in ("settings.get", "settings.update"):
        if not isinstance(result, dict) or not isinstance(
            negotiated_capabilities, (list, tuple, set, frozenset)
        ):
            return False
        return _settings_fields_are_authorized(
            result.get("values"),
            result.get("availability"),
            contract["fieldCapabilities"],
            set(negotiated_capabilities).intersection(KNOWN_CAPABILITIES),
        )
    return True


def notification_is_authorized(value: object, negotiated_capabilities: object) -> TypeGuard[Notification]:
    if not is_notification(value) or not isinstance(negotiated_capabilities, (list, tuple, set, frozenset)):
        return False
    contract = NOTIFICATION_CONTRACTS.get(value["method"])
    if contract is None:
        return False
    if value["method"] == "companion.stateChanged" and not _eligibility_field_is_authorized(
        value["params"], negotiated_capabilities
    ):
        return False
    return set(contract["requiredCapabilities"]).issubset(
        set(negotiated_capabilities).intersection(KNOWN_CAPABILITIES)
    )
# fmt: on
