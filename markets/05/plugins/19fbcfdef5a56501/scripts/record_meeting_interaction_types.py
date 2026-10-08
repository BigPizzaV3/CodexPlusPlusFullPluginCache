"""App-facing wire contracts for direct Record meeting interactions."""

from __future__ import annotations

from typing import Literal, TypeAlias, TypedDict

RecordMeetingTranscriptStatus = Literal["pending", "preliminary", "final", "unavailable"]
RecordMeetingProcessingStage = Literal["transcribing", "preparing-notes"]
RecordMeetingNoteStatus = Literal[
    "ready",
    "cca_complete",
    "joining",
    "waiting",
    "recording",
    "uploading",
    "processing",
    "failed",
]


class MeetingsActivityWire(TypedDict):
    """Workspace-scoped unread activity without note content or identifiers."""

    hasUnreadActivity: bool


class RecordMeetingPersonWire(TypedDict):
    """One attendee projected into selected-note detail."""

    name: str | None
    email: str | None


class RecordMeetingShareRecipientWire(TypedDict):
    """One selected-note share recipient with a validated email."""

    name: str | None
    email: str


class RecordMeetingTranscriptEntryWire(TypedDict):
    """One source transcript or meeting-chat entry."""

    speaker: str | None
    message: str
    timestamp: str | None
    offsetSeconds: float | None


class RecordMeetingRenderedTranscriptRowWire(TypedDict):
    """One rendered transcript row with its display timestamp."""

    speaker: str | None
    timestampLabel: str | None
    message: str
    offsetSeconds: float | None


class RecordMeetingRenderedTranscriptWire(TypedDict):
    """Rendered transcript rows returned when the backend provides them."""

    rows: list[RecordMeetingRenderedTranscriptRowWire]


class RecordMeetingTranscriptWire(TypedDict):
    """Bounded transcript content projected into selected-note detail."""

    status: RecordMeetingTranscriptStatus
    entries: list[RecordMeetingTranscriptEntryWire]
    renderedTranscript: RecordMeetingRenderedTranscriptWire | None


class _OptionalRecordMeetingNoteWire(TypedDict, total=False):
    personalNoteTakingComingSoon: bool
    processingStage: RecordMeetingProcessingStage
    summaryPageUrl: str
    summaryPageStatus: Literal["ready", "unavailable"]
    meetingChat: RecordMeetingTranscriptWire
    recordSource: str
    devicePlatform: Literal["ios", "android"]
    processingState: str
    canShareMeeting: bool


class RecordMeetingNoteWire(_OptionalRecordMeetingNoteWire):
    """Complete private selected-note detail returned to the app."""

    id: str
    title: str
    recordingStartTime: str | None
    recordingEndTime: str | None
    calendarStartTime: str | None
    calendarEndTime: str | None
    attendees: list[RecordMeetingPersonWire]
    shareRecipients: list[RecordMeetingShareRecipientWire]
    status: str | None
    processingStatus: str | None
    displayStatus: RecordMeetingNoteStatus
    permalink: None
    summary: str | None
    transcript: RecordMeetingTranscriptWire


class RecordMeetingShareWire(TypedDict):
    """Validated sharing acknowledgement returned to the app."""

    meeting_id: str
    recipient_email: str
    recipient_name: str | None
    access_edge_created: bool


class RecordMeetingShareEligibilityMemberWire(TypedDict):
    """One exact eligible workspace recipient without backend identifiers."""

    email: str
    name: str | None


class RecordMeetingPersonalShareEligibilityWire(TypedDict):
    """Verified personal-account sharing scope."""

    scope: Literal["personal"]
    workspaceName: None
    member: None


class RecordMeetingWorkspaceShareEligibilityWire(TypedDict):
    """Verified workspace scope and, when requested, one eligible member."""

    scope: Literal["workspace"]
    workspaceName: str | None
    member: RecordMeetingShareEligibilityMemberWire | None


RecordMeetingShareEligibilityWire: TypeAlias = (
    RecordMeetingPersonalShareEligibilityWire | RecordMeetingWorkspaceShareEligibilityWire
)


class RecordMeetingDeleteWire(TypedDict):
    """Private acknowledgement for one explicitly deleted meeting."""

    meeting_id: str
    deleted: Literal[True]


class RecordMeetingReprocessWire(TypedDict):
    """Private acknowledgement for the selected note's existing processing job."""

    meetingId: str
    status: Literal["processing"]


class _OptionalRecordMeetingFeedbackWire(TypedDict, total=False):
    feedbackContinuationToken: str
    diagnosticsUploaded: bool


class RecordMeetingFeedbackWire(_OptionalRecordMeetingFeedbackWire):
    """Validated feedback acknowledgement returned to the app."""

    meetingId: str
    feedbackId: str | None
