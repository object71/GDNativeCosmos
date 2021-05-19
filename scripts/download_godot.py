import platform
import requests
import zipfile
import io
import logging
import pathlib
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

download_dir = pathlib.Path("./godot")
download_dir.mkdir(parents=True, exist_ok=True)
if any(download_dir.iterdir()):
    logger.info("Godot already present")
    sys.exit(0)

godot_version = "3.3.1"
godot_downloads_url_base = "https://downloads.tuxfamily.org/godotengine"

def download_and_unzip(url):
    logger.info(f"Downloading: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        return

    with zipfile.ZipFile(io.BytesIO(response.content)) as the_zip:
        for contained_file_info in the_zip.infolist():
            with open(f"./godot/{contained_file_info.filename}", "wb") as new_file:
                with the_zip.open(contained_file_info) as contained_file:
                    new_file.write(contained_file.read())


if platform.system() == "Windows":
    download_and_unzip(f"{godot_downloads_url_base}/{godot_version}/Godot_v{godot_version}-stable_win32.exe.zip")
    download_and_unzip(f"{godot_downloads_url_base}/{godot_version}/Godot_v{godot_version}-stable_win64.exe.zip")
elif platform.system() == "Linux":
    download_and_unzip(f"{godot_downloads_url_base}/{godot_version}/Godot_v{godot_version}-stable_x11.32.zip")
    download_and_unzip(f"{godot_downloads_url_base}/{godot_version}/Godot_v{godot_version}-stable_x11.64.zip")
