from typing import List

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import project_crud
from app.services.google_api import spreadsheets_create, set_user_permissions, spreadsheets_update_value

router = APIRouter()


@router.post(
    '/',
    response_model=List[List[str]],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_service: Aiogoogle = Depends(get_service),
) -> List:
    """
    Получение отсортированного по сроку закрытия списка проектов
    и обновление Google-таблицы - только для суперюзеров.
    """
    sorted_projects = await project_crud.get_projects_by_completion_rate(
        session
    )
    spreadsheet_id = await spreadsheets_create(wrapper_service)
    await set_user_permissions(spreadsheet_id, wrapper_service)
    await spreadsheets_update_value(spreadsheet_id,
                                    sorted_projects,
                                    wrapper_service)
    return sorted_projects
