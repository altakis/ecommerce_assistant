import openai

from dotenv import load_dotenv

from AssisstantManager import AssistantManager

load_dotenv()

client = openai.OpenAI()

from app import execute_streamlit_interface


def main():
    """ manager = AssistantManager(client=client)

    execute_streamlit_interface(manager) """
    from assistant_creation_scripts import packaged_tools_funcs
    
    print(packaged_tools_funcs[0]("tea"))


if __name__ == "__main__":
    main()
