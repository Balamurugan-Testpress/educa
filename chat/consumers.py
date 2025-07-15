import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.id = self.scope["url_route"]["kwargs"]["course_id"]
        self.room_group_name = f"chat_{self.id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "").strip()
        if not message:
            return  # skip empty messages

        # Safely get username
        user = self.user.username if self.user.is_authenticated else "Anonymous"

        # Format datetime: e.g., "15 Jul 2025, 12:34 PM"
        now = timezone.localtime().strftime("%d %b %Y, %I:%M %p")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": user,
                "datetime": now,
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "user": event["user"],
                    "datetime": event["datetime"],
                }
            )
        )
