from app.agents import BaseAgentFactory
from openai import OpenAI
import time
import re


class OpenAIAssistant(BaseAgentFactory):
    def __init__(self):
        self.client = OpenAI()
        self.assistant = None
        self.thread = None
        self.file = None

    def name(self) -> str:
        return "OpenAIAssistant"

    def build(self, file: str):
        self.file = self.client.files.create(
            file=open(file, "rb"),
            purpose='assistants'
        )
        self.assistant = self.client.beta.assistants.create(
            model="gpt-4-1106-preview",
            tools=[{"type": "retrieval"}]
        )
        self.thread = self.client.beta.threads.create()

    def chat(self, query: str):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=query,
            file_ids=[self.file.id]
        )
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
        )
        while True:
            time.sleep(0.5)
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
            )
            if run.status == "completed":
                break
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )
        text_value = messages.data[0].content[0].text.value
        print(text_value)
        # 出力からソースを削除
        pattern = r"【.*】"
        text_value = re.sub(pattern, "", text_value)
        return text_value
