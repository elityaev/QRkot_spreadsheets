from app.models import CharityProject, Donation

INV_DICT = {
    CharityProject: Donation,
    Donation: CharityProject
}
FORMAT = "%Y/%m/%d %H:%M:%S"
# константы шаблона для создания документа - таблицы
DOCUMENT_TITLE = 'Отчет на '
DOCUMENT_LOCALE = 'ru_RU'
SHEET_TYPE = 'GRID'
SHEET_ID = 0
LIST_TITLE = 'Лист1'
ROW_COUNT = 100
COLUMN_COUNT = 3
# константы для шапки таблицы с обновляемыми данными
REPORT_DATE_TITLE = 'Отчет от'
SHEET_TITLE = 'Топ проектов по скорости закрытия'
COLUMN_1 = 'Название проекта'
COLUMN_2 = 'Время сбора'
COLUMN_3 = 'Описание'
UPDATE_RANGE = 'A1:C'
