import logging
from fastapi import Request, Depends, Response, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from spaceone.core.fastapi.api import BaseAPI, exception_handler

from cloudforet.console_api_v2.service.agent_service import AgentService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBearer()

router = APIRouter(include_in_schema=True)

SERVICE = "console-api"
RESOURCE = "Agent"

@router.get("/kubernetes")
@exception_handler
async def kubernetes(self, request: Request, service_account_id: str, token: HTTPAuthorizationCredentials = Depends(_AUTH_SCHEME)):
    params = {"service_account_id": service_account_id, "token": token.credentials}

    with AgentService() as agent_service:
        spaceone_agent = agent_service.kubernetes(params)
        return Response(content=spaceone_agent, media_type="application/x-yaml")
