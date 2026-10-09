"""Structured record extracted from one alarm or test log line (Phase 1)."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class AlarmRecord(BaseModel):
    occurred_at: datetime = Field(description="When the alarm occurred")
    equipment: str = Field(description="Rig or equipment name, e.g. 'Durability Rig 2'")
    alarm_code: str = Field(description="Alarm code as written in the log, e.g. 'E-203'")
    severity: Severity
    probable_cause: str | None = Field(
        default=None, description="Likely cause if the log suggests one, otherwise None"
    )
