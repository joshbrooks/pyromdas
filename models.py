from typing import List
from pydantic import BaseModel
from datetime import datetime


class ProcessLog(BaseModel):
    level: str
    when: datetime
    type: str
    source: str
    description: str


class RoughnessProcessed(BaseModel):
    chainage: float
    lrp_offset_start: float
    lrp_offset_end: float
    lrp_distance: float
    lrp_number_start: int
    lrp_number_end: int
    speed: float
    raw_c_1: int
    raw_c_2: int
    raw_c_1_km: float
    raw_c_2_km: float
    c_rough_1: float
    c_rough_2: float
    calib_rgh: float
    quality: float
    c_1_a1: float
    c_1_a2: float
    c_1_a3: float
    c_1_a4: float
    c_1_a5: float
    c_1_a6: float
    c_1_a7: float
    c_2_a1: float
    c_2_a2: float
    c_2_a3: float
    c_2_a4: float
    c_2_a5: float
    c_2_a6: float
    c_2_a7: float


class RoughnessRaw(BaseModel):
    chainage: float
    speed: float
    lrp_number: int
    rough_1: int
    rough_2: int
    time: float
    exclusion: str


class SurveyHeader(BaseModel):

    survey_id: str
    survey_file: str
    survey_desc: str
    survey_date: datetime
    vehicle: str
    operator: str
    user_1_name: str
    user_1: str
    user_2_name: str
    user_2: str
    user_3_name: str
    user_3: str
    lrp_file: str
    lrp_reset: str
    lrp_start: int
    chain_init: float
    chain_start: float
    chain_end: float
    sect_len: float
    dir: str
    lane: int
    devices: str
    otherside: bool
    version: str
    memo: str
    length: float


class ProfilerIri(BaseModel):

    chainage: float
    lrp_offset_start: float
    lrp_offset_end: float
    lrp_number_start: int
    lrp_number_end: int
    speed: float
    lwp_iri: float
    lwp_quality: float
    rwp_iri: float
    rwp_quality: float
    lane_iri: float


class ProfilerHeader(BaseModel):

    sampling_interval: float
    processing_interval: float
    lwp_id: str
    rwp_id: str


class RawAccel(BaseModel):

    chainage: float
    time: float
    lrp_chainage: float
    lrp_number: int
    elevation: float
    acceleration: float
    profile: float
    count: int
    timestamp: int
    status: str


class RawElev(BaseModel):

    chainage: float
    time: float
    lrp_chainage: float
    lrp_number: int
    elevation: float
    acceleration: float
    profile: float
    count: int
    timestamp: int
    status: str


class RomdasExtract(BaseModel):
    processlog: List[ProcessLog] = []
    profilerheader: List[ProfilerHeader] = []
    profileriri: List[ProfilerIri] = []
    rawaccel: List[RawAccel] = []
    rawelev: List[RawElev] = []
    roughnessprocessed: List[RoughnessProcessed] = []
    roughnessraw: List[RoughnessRaw] = []
    surveyheader: List[SurveyHeader] = []
