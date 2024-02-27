# Streamlit app layout
st.title('My Chatbot')

# User input
user_input = st.text_input("Talk to the chatbot:")

# Send message to OpenAI API
if user_input:
    response = client.create_completion(
        model="text-davinci-003",  # or any other model
        prompt=user_input,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    # Display the response
    st.write(response.choices[0].text.strip())
