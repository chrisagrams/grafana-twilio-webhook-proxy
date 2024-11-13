import os
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Dict, Optional
from dotenv import load_dotenv

from twilio_api import make_call, make_text


load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
from_number = os.getenv("FROM_NUMBER")

app = FastAPI()


class Alert(BaseModel):
    status: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    startsAt: str
    endsAt: str
    generatorURL: Optional[str]
    fingerprint: Optional[str]
    silenceURL: Optional[str]
    dashboardURL: Optional[str]
    panelURL: Optional[str]
    values: Optional[str]
    valueString: Optional[str]


class AlertBody(BaseModel):
    receiver: str
    status: str
    alerts: List[Alert]
    groupLabels: Dict[str, str]
    commonLabels: Dict[str, str]
    commonAnnotations: Dict[str, str]
    externalURL: str
    version: str
    groupKey: str
    truncatedAlerts: int
    orgId: int
    title: str
    state: str
    message: str


@app.post("/sms")
def send_text(
    alert_data: AlertBody,
    to_number: str = Query(..., description="The phone number to text"),
):
    description = alert_data.commonAnnotations.get("description")
    summary = alert_data.commonAnnotations.get("summary")

    text = make_text(
        account_sid=account_sid,
        account_token=auth_token,
        from_number=from_number,
        to_number=to_number,
        message=description + " " + summary,
    )

    return text.sid


@app.post("/call")
def send_call(
    alert_data: AlertBody,
    to_number: str = Query(..., description="The phone number to call"),
):
    description = alert_data.commonAnnotations.get("description")
    summary = alert_data.commonAnnotations.get("summary")

    call = make_call(
        account_sid=account_sid,
        account_token=auth_token,
        from_number=from_number,
        to_number=to_number,
        message=description + " " + summary,
    )
    return call.sid
