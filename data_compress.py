import os
import zipfile as zip
from datetime import datetime
from os.path import join, relpath


def data_compress(data: list) -> None:
    filename_compress = f'zip_files_{datetime.now().date()}.7z'
    with zip.ZipFile(filename_compress, 'w') as file_zip:
        for item in data:
            file_zip.write(item)


def get_folder_files(abspath: str) -> list:
    if not os.path.exists(abspath):
        raise FileNotFoundError('Path not found!')
    data = list()
    for root, subfolder, files in os.walk(abspath):
        data.extend(join(root, file) for file in files)
    if not data:
        raise ValueError('No files!')
    return [relpath(file) for file in data]


if __name__ == '__main__':
    abspath = rf'C:\Users\shadmin.LAN\Desktop\clean-logs-txt\files'
    data = get_folder_files(abspath)
    data_compress(data)
