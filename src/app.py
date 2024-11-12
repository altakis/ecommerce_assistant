# Based on https://github.com/pdichone/vincibits-news-summarizer/tree/5a2d14abf94ef8dba0e29d89c73bdfea545aff6d
import streamlit as st
from AssisstantManager import AssistantManager


def execute_streamlit_interface(manager: AssistantManager):
    # Streamlit interface
    st.title("Ecommerce ShopBot")

    with st.form(key="user_input_form"):
        instructions = st.text_input("Enter query:")
        submit_button = st.form_submit_button(label="Run Assistant")

        if submit_button:
            manager.create_thread()

            # Add the message and run the assistant
            manager.add_message_to_thread(role="user", content=f"{instructions}")
            manager.run_assistant(instructions=instructions)

            # Wait for completions and process messages
            manager.wait_for_completion()

            summary = manager.get_summary()

            st.write(summary)

            st.text("Run Steps:")
            st.code(manager.run_steps(), line_numbers=True)
