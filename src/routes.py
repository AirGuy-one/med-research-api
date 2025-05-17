from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import schemas
from src.database import get_db
from src.repositories import (
    create_study,
    create_participant,
    create_measurement,
    get_measurements_by_participant,
    get_measurements_by_study,
)

router = APIRouter()


@router.post("/studies/", response_model=schemas.StudyOut)
def api_create_study(
    study: schemas.StudyCreate,
    db: Session = Depends(get_db),
):
    return create_study(db, study)


@router.post("/participants/", response_model=schemas.ParticipantOut)
def api_create_participant(
    participant: schemas.ParticipantCreate,
    db: Session = Depends(get_db),
):
    return create_participant(db, participant)


@router.post("/measurements/", response_model=schemas.MeasurementOut)
def api_create_measurement(
    measurement: schemas.MeasurementCreate,
    db: Session = Depends(get_db),
):
    return create_measurement(db, measurement)


@router.get(
    "/participants/{participant_id}/measurements",
    response_model=list[schemas.MeasurementOut],
)
def api_get_measurements_by_participant(
    participant_id: UUID,
    db: Session = Depends(get_db),
):
    return get_measurements_by_participant(db, participant_id)


@router.get(
    "/studies/{study_id}/measurements",
    response_model=list[schemas.MeasurementOut],
)
def api_get_measurements_by_study(
    study_id: UUID,
    db: Session = Depends(get_db),
):
    return get_measurements_by_study(db, study_id)
