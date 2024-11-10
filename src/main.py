import openai

from dotenv import load_dotenv

from AssisstantManager import AssistantManager

load_dotenv()

client = openai.OpenAI()

from .app import execute_streamli_interface


def main():
    print("test")
    manager = AssistantManager(client=client)

    execute_streamli_interface(manager)


if __name__ == "__main__":
    main()
