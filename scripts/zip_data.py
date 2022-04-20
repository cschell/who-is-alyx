"""
Zip the csvs in players/
"""

import pathlib
import zipfile

for entry in pathlib.Path("players/").glob("*"):
    if entry.is_dir():
        zip_path = entry.with_suffix(".zip")

        print(f"creating new archive {zip_path}")
        zf = zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9)

        for csv in entry.glob("**/*.csv"):
            zf.write(csv)
            print(f"  adding {csv}")

        zf.close()