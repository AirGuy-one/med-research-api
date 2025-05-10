from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class StudyCreate(BaseModel):
    title: str
    description: str | None = None


class StudyOut(BaseModel):
    id: UUID
    title: str
    description: str | None
    created_at: datetime

    class Config:
        orm_mode = True


class ParticipantCreate(BaseModel):
    name: str
    birth_date: datetime | None = None


class ParticipantOut(BaseModel):
    id: UUID
    name: str
    birth_date: datetime | None

    class Config:
        orm_mode = True


class MeasurementCreate(BaseModel):
    study_participant_id: UUID
    type: str
    value: float


class MeasurementOut(BaseModel):
    id: UUID
    type: str
    value: float
    taken_at: datetime

    class Config:
        orm_mode = True
