from http import HTTPStatus

from fastapi import HTTPException

from app import constants as const


def validate_len_data_to_update(table_length):
    if table_length > const.ROW_COUNT:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail='Объем данных превышает допустимый'
        )