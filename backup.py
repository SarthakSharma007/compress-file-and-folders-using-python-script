import shutil
import os
import datetime


def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name, 'zip', source)


source = ""  # enter your file path which you have to compress
destination = ""  # enter your file path where you want to save the compressed file

backup_files(source, destination)
