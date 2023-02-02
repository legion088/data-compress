import os
import zipfile as zip
from datetime import datetime


def data_compress(abspath: str, data: list):
    filename_compress = f'zip_files_{datetime.now().date()}.zip'
    abspath_file_compress = os.path.join(abspath, filename_compress)
    with zip.ZipFile(abspath_file_compress, 'w') as file_zip:
        for item in data:
            file_zip.write(item)


def get_folder_files(abspath: str) -> list:
    if not os.path.exists(abspath):
        raise FileNotFoundError('Path not found!')
    data = list()
    for root, subfolder, files in os.walk(abspath):
        data.extend(os.path.join(root, file) for file in files)
    return data


if __name__ == '__main__':
    abspath = fr'C:\Users\petrov_pp\Desktop\files'
    data = get_folder_files(abspath)
    data_compress(abspath, data)
