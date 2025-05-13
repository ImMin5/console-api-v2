import logging

from fastapi import Depends, Request, APIRouter
from fastapi.concurrency import run_in_threadpool
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.fastapi.api import exception_handler

from cloudforet.console_api_v2.service.auth_service import AuthService

_LOGGER = logging.getLogger(__name__)
_AUTH_SCHEME = HTTPBasic()

router = APIRouter(include_in_schema=True)

SERVICE = "console-api"
RESOURCE = "Auth"

@router.get("/basic")
@exception_handler
async def basic(
    http_authorization: HTTPBasicCredentials = Depends(_AUTH_SCHEME)
) -> dict:
    if http_authorization is None:
        raise ERROR_REQUIRED_PARAMETER(message="empty token provided.")

    with AuthService() as auth_service:
        await run_in_threadpool(auth_service.basic, http_authorization.dict())
        return {"status_code": "200"}

@router.post("/saml/{domain_id}")
@exception_handler
async def saml(request: Request, domain_id: str) -> dict:
    with AuthService() as saml_service:
        form_data = await request.form()
        params = {"request": request, "form_data": form_data, "domain_id": domain_id}
        response = await run_in_threadpool(saml_service.saml, params)
        return response

@router.get("/saml/{domain_id}/metadata")
@exception_handler
async def saml_sp_metadata(domain_id: str) -> dict:
    with AuthService() as saml_service:
        response = await run_in_threadpool(saml_service.saml_sp_metadata, domain_id)
        return response
