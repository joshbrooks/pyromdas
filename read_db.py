import subprocess
from typing import Type, Dict
from pydantic import BaseModel
from models import (
    ProcessLog,
    ProfilerHeader,
    ProfilerIri,
    RawAccel,
    RawElev,
    RomdasExtract,
    RoughnessProcessed,
    RoughnessRaw,
    SurveyHeader,
)
import io
import csv
from datetime import datetime


def read_table(file: str, table_name: str):
    table_info = subprocess.run(["mdb-export", file, table_name], capture_output=True)
    tabular_data = io.StringIO(table_info.stdout.decode())
    return enumerate(csv.reader(tabular_data))


if __name__ == "__main__":

    survey_suffix = "test_1-survey"
    file: str = "/home/josh/Downloads/ROMDAS - test_1-survey.mdb"
    process_log_table_name: str = f"Process_Log_{survey_suffix}"

    rd = RomdasExtract()

    for num, line in read_table(file, process_log_table_name):
        if num == 0:
            headers = [l.lower() for l in line]
            continue
        data = dict(zip(headers, line))
        data["when"] = datetime.strptime(data["when"], "%m/%d/%y %H:%M:%S")
        rd.processlog.append(ProcessLog(**data))

    rough_table = f"Roughness_Processed_{survey_suffix}"
    for num, line in read_table(file, rough_table):
        if num == 0:
            headers = [l.lower() for l in line]
            continue
        rd.roughnessprocessed.append(RoughnessProcessed(**dict(zip(headers, line))))

    for num, line in read_table(file, f"Roughness_Raw_{survey_suffix}"):
        if num == 0:
            headers = [l.lower() for l in line]
            continue
        rd.roughnessraw.append(RoughnessRaw(**dict(zip(headers, line))))

    for num, line in read_table(file, "Survey_Header"):
        if num == 0:
            headers = [l.lower() for l in line]
            continue
        data = dict(zip(headers, line))
        data["survey_date"] = datetime.strptime(
            data["survey_date"], "%m/%d/%y %H:%M:%S"
        )
        rd.surveyheader.append(SurveyHeader(**data))

    for num, line in read_table(file, f"Profiler_IRI_{survey_suffix}"):
        if num == 0:
            headers = [l.lower() for l in line]
            continue

        rd.profileriri.append(ProfilerIri(**dict(zip(headers, line))))

    for num, line in read_table(file, f"Profiler_Header_{survey_suffix}"):
        if num == 0:
            headers = [l.lower() for l in line]
            continue

        rd.profilerheader.append(ProfilerHeader(**dict(zip(headers, line))))

    for num, line in read_table(file, f"Profiler_Raw_Accel_LWP-{survey_suffix}"):
        if num == 0:
            headers = [l.lower() for l in line]
            continue

        rd.rawaccel.append(RawAccel(**dict(zip(headers, line))))

    for num, line in read_table(file, f"Profiler_Raw_Elev_LWP-{survey_suffix}"):
        if num == 0:
            headers = [l.lower() for l in line]
            continue
        rd.rawelev.append(RawElev(**dict(zip(headers, line))))
