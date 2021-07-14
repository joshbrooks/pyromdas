# pyromdas
Convert romdas (mdb) format to Python formats


## Requirements

apt install mdbtools (NOT pip install mdbtoools)


## Extracting Table Data

import subprocess
file="/home/josh/Downloads/ROMDAS - test_1-survey.mdb"
table="Profiler_Raw_Elev_LWP-test_1-survey"
table_info = subprocess.run(['mdb-export', file, table], capture_output=True)

echo ${FILE} ${TABLE}
mdb-export "${FILE}" ${TABLE}
