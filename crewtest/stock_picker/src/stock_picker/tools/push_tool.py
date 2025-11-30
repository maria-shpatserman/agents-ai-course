from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class PushNotificationInput(BaseModel):
    """A message to be sent to user"""
    message: str = Field(..., description="A message to be snt to user")

class PushNotificationTool(BaseTool):
    name: str = "Send a push notification"
    description: str = (
        "This tool is used to push notification to user"
    )
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, message: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")
        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Push: {message}")
        payload = {"user": pushover_user, "token": pushover_token, "message": message}
        requests.post(pushover_url, data=payload)
        return '{"notification": "ok"}'
