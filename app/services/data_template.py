from datetime import datetime

from app import constants as const


def generate_json_spreadsheet_body():
    now_date_time = datetime.now().strftime(const.FORMAT)
    spreadsheet_body = {
        'properties': {
            'title': const.DOCUMENT_TITLE + now_date_time,
            'locale': const.DOCUMENT_LOCALE
        },
        'sheets': [{
            'properties': {
                'sheetType': const.SHEET_TYPE,
                'sheetId': const.SHEET_ID,
                'title': const.LIST_TITLE,
                'gridProperties': {
                    'rowCount': const.ROW_COUNT,
                    'columnCount': const.COLUMN_COUNT
                }
            }
        }]
    }
    return spreadsheet_body


def get_table_values_to_update():
    now_date_time = datetime.now().strftime(const.FORMAT)
    table_values = [
        [const.REPORT_DATE_TITLE, now_date_time],
        [const.SHEET_TITLE],
        [const.COLUMN_1, const.COLUMN_2, const.COLUMN_3]
    ]
    return table_values