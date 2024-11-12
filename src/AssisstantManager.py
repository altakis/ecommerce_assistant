# Based on https://github.com/pdichone/vincibits-news-summarizer/tree/5a2d14abf94ef8dba0e29d89c73bdfea545aff6d

import json
import time

from assistant_creation_scripts.config import assistant_configuration
from tools.available_tools import (
    _getProductInfoByCategory,
    _getProductInfoByName,
    _getProductStockById,
    get_tools,
)


class AssistantManager:
    assistant_id = "asst_CLK8ocJG1D4lGYQ6EQp52BTj"
    thread_id = None
    model = assistant_configuration["model"]

    def __init__(self, client):
        self.client = client
        self.assistant = None
        self.thread = None
        self.run = None
        self.summary = None

        # Retrieve existing assistant and thread if IDs are already set
        if AssistantManager.assistant_id:
            self.assistant = self.client.beta.assistants.retrieve(
                assistant_id=AssistantManager.assistant_id
            )
        if AssistantManager.thread_id:
            self.thread = self.client.beta.threads.retrieve(
                thread_id=AssistantManager.thread_id
            )

    def create_assistant(self, name):
        if not self.assistant:
            assistant_obj = self.client.beta.assistants.create(
                name=assistant_configuration["name"],
                instructions=assistant_configuration["instruction_prompt"],
                tools=get_tools(),
                model=self.model,
            )
            AssistantManager.assistant_id = assistant_obj.id
            self.assistant = assistant_obj
            print(f"AssisID:::: {self.assistant.id}")

    def create_thread(self):
        if not self.thread:
            thread_obj = self.client.beta.threads.create()
            AssistantManager.thread_id = thread_obj.id
            self.thread = thread_obj
            print(f"ThreadID::: {self.thread.id}")

    def add_message_to_thread(self, role, content):
        if self.thread:
            self.client.beta.threads.messages.create(
                thread_id=self.thread.id, role=role, content=content
            )

    def run_assistant(self, instructions):
        if self.thread and self.assistant:
            self.run = self.client.beta.threads.runs.create(
                thread_id=self.thread.id,
                assistant_id=self.assistant.id,
                instructions=instructions,
            )

    def process_message(self):
        if self.thread:
            messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
            last_message = messages.data[0]
            role = last_message.role
            response = last_message.content[0].text.value
            summary = [response]
            self.summary = "\n".join(summary)
            print(f"SUMMARY-----> {role.capitalize()}: ==> {response}")

            # for msg in messages:
            #     role = msg.role
            #     content = msg.content[0].text.value
            #     print(f"SUMMARY-----> {role.capitalize()}: ==> {content}")

    def get_all_messages_in_thread(self, thread_id):
        if thread_id:
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)
            all_thread_data = [
                [message.role, message.content] for message in messages.data
            ]
            print(all_thread_data)

    def call_required_functions(self, required_actions: dict):
        if not self.run:
            return
        tool_outputs = []

        for tool in required_actions.tool_calls:
            if tool.function.name == "_getProductInfoByName":
                args = json.loads(tool.function.arguments)
                output = _getProductInfoByName(**args)
                print(f"STUFFFFF;;;;{output}")
                final_str = "".join("".join(item) for item in output)
                tool_outputs.append({"tool_call_id": tool["id"], "output": final_str})
            elif tool.function.name == "_getProductStockById":
                args = json.loads(tool.function.arguments)
                output = _getProductStockById(**args)
                print(f"STUFFFFF;;;;{output}")
                final_str = "".join("".join(item) for item in output)
                tool_outputs.append({"tool_call_id": tool["id"], "output": final_str})
            elif tool.function.name == "_getProductInfoByCategory":
                args = json.loads(tool.function.arguments)
                output = _getProductInfoByCategory(**args)
                print(f"STUFFFFF;;;;{output}")
                final_str = "".join("".join(item) for item in output)
                tool_outputs.append({"tool_call_id": tool["id"], "output": final_str})

        # Submit all tool outputs at once after collecting them in a list
        if tool_outputs:
            print("Submitting outputs back to the Assistant...")
            try:
                self.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=self.thread.id,
                    run_id=self.run.id,
                    tool_outputs=tool_outputs,
                )
                print("Tool outputs submitted successfully.")
            except Exception as e:
                print("Failed to submit tool outputs:", e)
        else:
            print("No tool outputs to submit.")

    # for streamlit
    def get_summary(self):
        return self.summary

    def wait_for_completion(self):
        if self.thread and self.run:
            while True:
                time.sleep(5)
                run_status = self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread.id, run_id=self.run.id
                )
                print(f"RUN STATUS:: {run_status.model_dump_json(indent=4)}")

                if run_status.status == "completed":
                    self.process_message()
                    break
                elif run_status.status == "requires_action":
                    print("FUNCTION CALLING NOW...")
                    self.call_required_functions(
                        required_actions=run_status.required_action.submit_tool_outputs
                    )

    # Run the steps
    def run_steps(self):
        run_steps = self.client.beta.threads.runs.steps.list(
            thread_id=self.thread.id, run_id=self.run.id
        )
        print(f"Run-Steps::: {run_steps}")
        return run_steps.data
