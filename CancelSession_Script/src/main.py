
#!/usr/bin/env python3
import argparse
import os
import sys
import re
from datetime import datetime
from typing import Optional, Set, Dict, List

import pandas as pd
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent

# --- Defaults (can be overridden via CLI) ---
CSV_FILE = BASE_DIR / ".." / "sample" / "data.csv"
LOG_FILE= (BASE_DIR / ".." / "sample" / "pyslac.log").resolve()
CSV_FILE=CSV_FILE.resolve()
LOG_FILE=LOG_FILE.resolve()


if not CSV_FILE.exists():
    raise FileNotFoundError(f"CSV file not found: {CSV_FILE}")

df=pd.read_csv(CSV_FILE,encoding="utf-16",sep="\t",engine="python")
# print("shape",df.shape)


dur = df["Duration"].astype(str).str.strip().str.lower()

sec=pd.to_numeric(
    dur.str.extract(r"(\d+)\s*s")[0],
    errors="coerce"
)
df["Duration_seconds"] = sec
filtered = df[(sec > 40) & (sec < 60)]
# print(filtered)
chargeEndTime=filtered["chargingEndTime"]
# print("chargeEndTime",chargeEndTime)




logwithErrorlist = []   

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for i, line in enumerate(f, start=1):
        if "ERROR - PEV-EVSE MATCHED Failed" in line:
            logwithErrorlist.append(f"{i:05d}: {line.rstrip()}")
            # print(f"{i:05d}: {line.rstrip()}")

logfile_time_stamp = []
for item in logwithErrorlist:
    m = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2})", item)
    if m:
        logfile_time_stamp.append(m.group(1))

# print("logfile_time_stamp",logfile_time_stamp)

csvFile_timeStamp=[]
for item in chargeEndTime:
    m = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2})", item)
    if m:
        csvFile_timeStamp.append(m.group(1))

# print("csvFile_timeStamp",csvFile_timeStamp)




matches = sorted(set(logfile_time_stamp) & set(csvFile_timeStamp))
print("Matches:", matches)
print("Count:", len(matches))
if matches:
    print("Slack error")