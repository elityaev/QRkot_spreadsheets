from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    @staticmethod
    async def get_project_by_name(
            project_name: str,
            session: AsyncSession,
    ) -> CharityProject:
        """Получение проекта по имени."""
        project = await session.execute(
            select(CharityProject).where(
                CharityProject.name == project_name
            )
        )
        return project.scalars().first()

    @staticmethod
    async def get_projects_by_completion_rate(session: AsyncSession):
        closed_objs = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == 1
            )
        )
        closed_objs = closed_objs.scalars().all()
        data = []
        for obj in closed_objs:
            new_list = [obj.name,
                        str(obj.close_date - obj.create_date),
                        obj.description]
            data.append(new_list)
        sorted_projects = sorted(data, key=lambda x: x[1])
        return sorted_projects


project_crud = CRUDCharityProject(CharityProject)
