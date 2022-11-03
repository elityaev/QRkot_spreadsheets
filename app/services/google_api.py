from aiogoogle import Aiogoogle

from app import constants as const
from app.core.config import settings
from app.services.data_template import generate_json_spreadsheet_body, get_table_values_to_update
from app.services.validators import validate_len_data_to_update


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    """Функция создания таблицы."""
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = generate_json_spreadsheet_body()
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    """Функция предоставления доступа личному аккаунту к таблице."""
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        )
    )


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle,
) -> None:
    """Функция, записывающая информацию из БД в таблицу."""
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = get_table_values_to_update()
    for project in projects:
        new_row = [str(project[0]), str(project[1]), str(project[2])]
        table_values.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    table_length = len(table_values)
    validate_len_data_to_update(table_length)
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=const.UPDATE_RANGE + str(table_length),
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
