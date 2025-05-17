# src/repositories.py

from uuid import UUID

from sqlalchemy.orm import Session

from src import models, schemas


def create_study(db: Session, study_in: schemas.StudyCreate) -> models.Study:
    db_obj = models.Study(**study_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_participant(db: Session, participant_in: schemas.ParticipantCreate) -> models.Participant:
    db_obj = models.Participant(**participant_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_measurement(db: Session, measurement_in: schemas.MeasurementCreate) -> models.Measurement:
    db_obj = models.Measurement(**measurement_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_measurements_by_participant(db: Session, participant_id: UUID) -> list[models.Measurement]:
    study_participants = (
        db.query(models.StudyParticipant)
        .filter_by(participant_id=participant_id)
        .all()
    )
    measurements: list[models.Measurement] = []
    for sp in study_participants:
        measurements.extend(
            db.query(models.Measurement)
            .filter_by(study_participant_id=sp.id)
            .all()
        )
    return measurements


def get_measurements_by_study(db: Session, study_id: UUID) -> list[models.Measurement]:
    study_participants = (
        db.query(models.StudyParticipant)
        .filter_by(study_id=study_id)
        .all()
    )
    measurements: list[models.Measurement] = []
    for sp in study_participants:
        measurements.extend(
            db.query(models.Measurement)
            .filter_by(study_participant_id=sp.id)
            .all()
        )
    return measurements
