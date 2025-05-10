from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import models, schemas
from src.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/studies/", response_model=schemas.StudyOut)
def create_study(study: schemas.StudyCreate, db: Session = Depends(get_db)):
    db_study = models.Study(**study.dict())
    db.add(db_study)
    db.commit()
    db.refresh(db_study)
    return db_study


@router.post("/participants/", response_model=schemas.ParticipantOut)
def create_participant(p: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    db_p = models.Participant(**p.dict())
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p


@router.post("/measurements/", response_model=schemas.MeasurementOut)
def create_measurement(m: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    db_m = models.Measurement(**m.dict())
    db.add(db_m)
    db.commit()
    db.refresh(db_m)
    return db_m


@router.get("/participants/{participant_id}/measurements", response_model=list[schemas.MeasurementOut])
def get_measurements_by_participant(participant_id: UUID, db: Session = Depends(get_db)):
    study_participants = db.query(models.StudyParticipant).filter_by(participant_id=participant_id).all()
    measurements = []
    for sp in study_participants:
        measurements += db.query(models.Measurement).filter_by(study_participant_id=sp.id).all()
    return measurements


@router.get("/studies/{study_id}/measurements", response_model=list[schemas.MeasurementOut])
def get_measurements_by_study(study_id: UUID, db: Session = Depends(get_db)):
    study_participants = db.query(models.StudyParticipant).filter_by(study_id=study_id).all()
    measurements = []
    for sp in study_participants:
        measurements += db.query(models.Measurement).filter_by(study_participant_id=sp.id).all()
    return measurements
