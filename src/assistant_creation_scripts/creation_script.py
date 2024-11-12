import openai
from dotenv import load_dotenv

from .config import assistant_configuration
from .tools import (
    get_product_info_by_category,
    get_product_info_by_name,
    get_product_stock_by_id,
)

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
    name=assistant_configuration["name"],
    instructions=assistant_configuration["instruction_prompt"],
    model=assistant_configuration["model"],
    tools=[
        get_product_info_by_name.__getProductInfoByName_tool_definition,
        get_product_info_by_category.__getProductInfoByCategory_tool_definition,
        get_product_stock_by_id.__getProductStockById_tool_definition,
    ],
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
