#import streamlit as st
import ollama

stream = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': 'Is the sky blue?'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)

# Set your OpenAI API key here
'''
openai.api_key = 'YOUR_OPENAI_API_KEY'
def main():
    st.title("Document Processing and QA Chatbot")
    # File uploader
    uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf"])
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        # Display file content
        st.subheader("Uploaded Document Content:")
        file_contents = uploaded_file.read()
        st.write(file_contents.decode("utf-8"))
        # Chatbot interface
        st.subheader("Ask a question about the document:")
        question = st.text_input("Your Question:")
        if st.button("Ask"):
            if question.strip() == "":
                st.warning("Please enter a question.")
            else:
                answer_question(file_contents, question)
def answer_question(document, question):
    # Use OpenAI's GPT-3 to answer the question
    response = openai.Completion.create(
        engine="davinci",  # You can specify any other variant like "curie" or "babbage"
        prompt=question + "\nAnswer:",
        max_tokens=50,
        context=document,
        stop="\n"
    )
    # Extract the answer from the response
    answer = response.choices[0].text.strip()
    # Display the answer
    st.write(f"**Question:** {question}")
    st.write(f"**Answer:** {answer}")
    if __name__ == "__main__":
    main()
'''