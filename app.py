import streamlit as st
from finance_agent import agent

st.set_page_config(
    page_title= "Personal Finance Assistant"
)

st.title("Personal Finance Assistant")
st.caption("Ask questions about EMI, SIP return, and budgeting.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Get user input
user_input = st.chat_input("Ask a finance question...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Processing your request..."):
            try:
                response = agent.invoke({
                    "messages":[
                        {"role": "user", "content": user_input}
                    ]
                })
                #Find the latest AI message contaning text
                answer = None

                for message in reversed(response["messages"]):
                    if message.type == "ai" and message.content:
                        if isinstance(message.content, str):
                            answer = message.content
                            break

                        elif isinstance(message.content, list):
                            texts = [
                                block["text"]
                                for block in message.content
                                if  isinstance(block, dict)
                                and block.get("type") == "text"
                            ]

                            if texts:
                                answer =  "\n".join(texts)
                                break

                if answer:
                    st.markdown(answer)
                    st.session_state.messages.append({
                        "role" : "assitant",
                        "content" : "answer"
                    })
                else:
                    st.warning("The agent did not return a text response.")


            except Exception as e:
                st.error(f"Error: {e}")
