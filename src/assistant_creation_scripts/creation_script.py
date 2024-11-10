import openai
from dotenv import load_dotenv
from .config import assistant_configuration
from .tools import packaged_tools

load_dotenv()
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

client = openai.OpenAI()

packaged_tools.append({"type": "code_interpreter"})

# ==  Create our Assistant (Uncomment this to create your assistant) ==
assistant_bot = client.beta.assistants.create(
    name=assistant_configuration['name'],
    instructions=assistant_configuration['instruction_prompt'],
    model=assistant_configuration['model'],
    tools=packaged_tools,
)
asistant_id = assistant_bot.id
print(asistant_id)

# === Thread (uncomment this to create your Thread) ===
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "What can of service do you provide?",
        },
        {
            "role": "user",
            "content": "Tell me about the 'EcoFriendly Water Bottle'.",
        },
        {
            "role": "user",
            "content": "Do you have any tea products?",
        },
    ]
)
thread_id = thread.id
print(thread_id)
