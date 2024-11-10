import openai
from dotenv import load_dotenv
import config
from tools import packaged_tools

load_dotenv()
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

client = openai.OpenAI()

# ==  Create our Assistant (Uncomment this to create your assistant) ==
assistant_bot = client.beta.assistants.create(
    name=config.assistant_name,
    instructions=config.base_instruction_prompt,
    model=config.assistant_model,
    tools = packaged_tools
)
asistant_id = assistant_bot.id
print(asistant_id)

# === Thread (uncomment this to create your Thread) ===
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "What can of service do you provide?",
        }
    ]
)
thread_id = thread.id
print(thread_id)
