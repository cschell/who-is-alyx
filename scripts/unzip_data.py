"""
Zip the csvs in players/
"""

import pathlib
import zipfile

FORCE = False

for entry in pathlib.Path("players/").glob("*.zip"):
    if FORCE or not entry.with_suffix("").exists():
        print(f"unzipping new archive {entry}")
        zf = zipfile.ZipFile(entry, "r")
        zf.extractall()
        zf.close()
    else:
        print(f"skipping {entry.with_suffix('')}, folder already exists (to enforce overwriting edit this script and set `FORCE = True`)")
