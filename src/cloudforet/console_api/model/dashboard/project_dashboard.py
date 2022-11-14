from pydantic import BaseModel, Field
from typing import List, Dict, Union, Any
from datetime import datetime
from enum import Enum


class Scope(str, Enum):
    domain = 'DOMAIN'
    user = 'USER'

# Base Model


class ProjectDashboard(BaseModel):
    project_dashboard_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    scope: Union[Scope, None] = Field(None)
    version: Union[int, None] = Field(None)
    layouts: Union[List[Dict], None] = Field(None)
    dashboard_options_schema: Union[dict, None] = Field(None)
    settings: Union[dict, None] = Field(None)
    labels: Union[List[str], None] = Field(None)
    tags: Union[dict, None] = Field(None)
    user_id: Union[str, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)
    updated_at: Union[datetime, None] = Field(None)


class ProjectDashboardVersion(BaseModel):
    project_dashboard_id: Union[str, None] = Field(None)
    version: Union[int, None] = Field(None)
    layouts: Union[List[dict], None] = Field(None)
    dashboard_options: Union[dict, None] = Field(None)
    settings: Union[dict, None] = Field(None)
    dashboard_options_schema: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    create_at: Union[datetime, None] = Field(None)


class StatInfo(BaseModel):
    results: Union[List[Any], None] = Field(None)
    total_count: Union[List[int], None] = Field(None)


# Project Dashboard Info model

class ProjectDashboardInfo(ProjectDashboard):
    class Create(BaseModel):
        project_id: str = Field(...)
        name: str = Field(...)
        layout: Union[List[dict], None] = Field(None)
        dashboard_options: Union[dict, None] = Field(None)
        settings: Union[dict, None] = Field(None)
        dashboard_options_schema: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        userid: Union[str, None] = Field(None)
        domain_id: str = Field(...)

    class Update(BaseModel):
        project_dashboard_id: str = Field(...)
        name: Union[str, None] = Field(...)
        layout: Union[List[dict], None] = Field(None)
        dashboard_options: Union[dict, None] = Field(None)
        settings: Union[dict, None] = Field(None)
        dashboard_options_schema: Union[dict, None] = Field(None)
        labels: Union[List[str], None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: str = Field(...)

    class Delete(BaseModel):
        project_dashboard_id: str = Field(...)
        domain_id: str = Field(...)

    class Get(BaseModel):
        project_dashboard_id: str = Field(...)
        only: Union[List[str], None] = Field(None)
        domain_id: str = Field(...)

    class List(BaseModel):
        project_dashboard_id: Union[str, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        scope: Union[Scope, None] = Field(None)
        user_id: Union[str, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(...)


class ProjectDashboardVersionInfo(ProjectDashboardVersion):
    class DeleteVersion(BaseModel):
        project_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(...)

    class RevertVersion(BaseModel):
        project_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(...)

    class GetVersion(BaseModel):
        project_dashboard_id: str = Field(...)
        version: int = Field(...)
        domain_id: str = Field(...)

    class ListVersions(BaseModel):
        project_dashboard_id: str = Field(...)
        version: Union[int, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: str = Field(...)


class Stat(BaseModel):
    query: dict = Field(...)
    domain_id: str = Field(...)

    @staticmethod
    def description():
        desc = """
# Request Body
## query
- required

## domain_id
- required
                                        """
        return desc

    @staticmethod
    def response():
        response_example = {
            "200": {
                "model": StatInfo
            }
        }
        return response_example