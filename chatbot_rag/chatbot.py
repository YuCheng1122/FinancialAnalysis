import cohere
from dotenv import load_dotenv
import os
import requests

# Load the .env file
load_dotenv()

# Retrieve the API key from the .env file
cohere_api_key = os.getenv('COHERE_API_KEY')

# Initialize the Cohere client
co = cohere.Client(cohere_api_key)

# Function to retrieve documents from all text files in a given directory
def retrieve_documents_from_directory(directory_path):
    documents = []
    # Walk through the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            # Construct full file path
            file_path = os.path.join(directory_path, filename)
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                documents.append({"id": filename, "text": content})
    return documents

# Example usage: 相對路徑一直抓不到所以先暫時用絕對路徑
directory_path = r'D:\3952\AI\rag_raw_data\台積電2023~2002'


documents = retrieve_documents_from_directory(directory_path)

# Function to generate a response based on the retrieved documents and the query
def generate_response(query, documents):
    # 只使用最近的一部分文檔
    recent_documents = documents[-10:]  # 假設每年一個文檔，只取最近五年的數據

    response = co.chat(
        chat_history=[
            {"role": "USER", "message": query}
        ],
        message=query,
        documents=recent_documents,  # 使用較少的文檔
        prompt_truncation='AUTO'  # 自動截斷過長的輸入
    )
    return response


# Main chatbot function
def chatbot(query):
    # Retrieve related documents from the text file
    documents = retrieve_documents_from_directory(directory_path)
    
    # Generate a response based on the documents
    response = generate_response(query, documents)
    
    return response

# Example usage
user_query = "Near-term demand and inventory situation: Inquire about recent changes and expectations for fabless semiconductor inventory?"
bot_response = chatbot(user_query)
print(bot_response)