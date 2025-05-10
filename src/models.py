import datetime
import uuid

from sqlalchemy import (
    Column, String, DateTime, ForeignKey, Float
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Study(Base):
    __tablename__ = "studies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    participants = relationship("StudyParticipant", back_populates="study")


class Participant(Base):
    __tablename__ = "participants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=True)

    studies = relationship("StudyParticipant", back_populates="participant")


class StudyParticipant(Base):
    __tablename__ = "study_participants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    study_id = Column(UUID(as_uuid=True), ForeignKey("studies.id"), nullable=False)
    participant_id = Column(UUID(as_uuid=True), ForeignKey("participants.id"), nullable=False)

    study = relationship("Study", back_populates="participants")
    participant = relationship("Participant", back_populates="studies")
    measurements = relationship("Measurement", back_populates="study_participant")


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    study_participant_id = Column(UUID(as_uuid=True), ForeignKey("study_participants.id"), nullable=False)

    type = Column(String, nullable=False)  # e.g. "temperature", "blood_pressure"
    value = Column(Float, nullable=False)
    taken_at = Column(DateTime, default=datetime.datetime.utcnow)

    study_participant = relationship("StudyParticipant", back_populates="measurements")
