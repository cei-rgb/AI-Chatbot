import streamlit as st
import requests

st.title("AI Chatbot")

st.write("Simple AI chatbot powered by LLM and FastAPI")

user_input = st.text_input("Enter your message:")

if st.button("Send"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": user_input}
            )

            if response.status_code == 200:
                data = response.json()

                if "response" in data:
                    st.success("AI Response:")
                    st.write(data["response"])
                else:
                    st.error("Error from backend: " + str(data))

            else:
                st.error("Backend error: " + str(response.status_code))

        except Exception as e:
            st.error("Could not connect to backend: " + str(e))
