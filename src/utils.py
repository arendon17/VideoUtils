import json
import datetime
import logging
from pathlib import Path

logging.basicConfig(format='%(levelname)s %(asctime)s : %(message)s', level=logging.INFO)


class Utils:
    @staticmethod
    def _get_file_path(file_path):
        base_path = Path(__file__).parent
        return (base_path / file_path).resolve()

    @staticmethod
    def get_json_file(filepath):
        try:
            json_url = Utils._get_file_path(filepath)
            json_file = json.load(open(json_url, 'r', encoding='utf8'))
        except Exception as err:
            raise

        return json_file

    @staticmethod
    def write_json_file(json_data, filepath):
        try:
            json_url = Utils._get_file_path(filepath)
            with open(json_url, "w") as json_file:
                json.dump(json_data, json_file)
        except Exception as err:
            logging.error(f'Error with write_json_file - {err}')
            raise

    @staticmethod
    def get_text_file(filepath):
        url = Utils._get_file_path(filepath)
        text_file = open(url, 'r', encoding='utf8')

        return text_file.read()

    @staticmethod
    def write_text_file(filepath, text):
        url = Utils._get_file_path(filepath)
        with open(url, 'w') as out:
            out.write(text + '\n')

    @staticmethod
    def is_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError as err:
            return False

    @staticmethod
    def rename_file(filename, new_name=None, new_text_to_append=None):
        name_split = filename.split('.')
        current_name = name_split[:-1]  # all but last item
        file_extension = name_split[-1]  # last item -> file extension
        renamed_file = filename
        if new_name is not None:
            renamed_file = f'{new_name}.{file_extension}'
        if new_text_to_append is not None:
            renamed_file = f'{current_name}{new_text_to_append}.{file_extension}'
        return renamed_file
