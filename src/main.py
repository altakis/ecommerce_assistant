import openai
from dotenv import load_dotenv

from AssisstantManager import AssistantManager

load_dotenv()

client = openai.OpenAI()

from app import execute_streamlit_interface

from tools.available_tools import (
    _getProductInfoByCategory,
    _getProductInfoByName,
    _getProductStockById,
    get_tools,
)


def main():
    #print(_getProductInfoByName("tea"))
    print(_getProductInfoByCategory("Meat"))
    
    manager = AssistantManager(client=client)

    #execute_streamlit_interface(manager)
    
    instructions = """
    Do you have green tea?
    """
    
    manager.add_message_to_thread(role="user", content=f"{instructions}")
    
    manager.create_thread()    
    manager.run_assistant(instructions=instructions)
    # Wait for completions and process messages
    manager.wait_for_completion()
    summary = manager.get_summary()
    print(summary)
    """ print("Run Steps:")
    print(manager.run_steps()) """


if __name__ == "__main__":
    main()
