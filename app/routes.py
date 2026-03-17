from fastapi import APIRouter
from app.dal import *

router = APIRouter()


@router.get("/health")
def health_chck():
    return {"status": "ok"}


@router.get("/traffic_alert")
def _traffic_alert():
    result = traffic_alert()
    return result


@router.get("/analysis_of_collection_sources")
def _analysis_of_collection_sources():
    result = analysis_of_collection_sources()
    return result


@router.get("/finding_new_targets")
def _finding_new_targets():
    result = finding_new_targets()
    return result


@router.get("/identifying_awakened_sleeping_cells")
def _identifying_awakened_sleeping_cells():
    result = identifying_awakened_sleeping_cells()
    return result


@router.get("/visualization_of_a_target_trajectory:")
def _visualization_of_a_target_trajectory():
    result = visualization_of_a_target_trajectory()
    return result
