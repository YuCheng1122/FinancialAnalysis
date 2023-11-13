import openai
import os
import json
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve the API key from the .env file
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set up the OpenAI client with your API key
openai.api_key = openai_api_key

# Function to read the content of a text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Function to analyze sentiment using OpenAI's GPT-3 model
def analyze_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another engine you prefer
        prompt=f"The following text is analyzed to determine its sentiment:\n\n{text}\n\nThe sentiment of the above text is:",
        max_tokens=60,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Main function to handle the sentiment analysis logic
def sentiment_analysis(file_path):
    # Read the content of the text file
    text_content = read_text_file(file_path)
    
    # Analyze the sentiment of the text content
    sentiment_result = analyze_sentiment(text_content)
    
    # Return the sentiment result
    return sentiment_result

# Set the file path variable 相對路徑一直抓不到所以先暫時用絕對路徑
user_file_path =r'D:\3952\AI\rag_raw_data\台積電2023~2002\2330台積電_2023Q1法人說明會(英)_20230420.txt'

# Call the sentiment analysis function with the file path
sentiment_result = sentiment_analysis(user_file_path)

# Print the sentiment result
print(f"Sentiment Analysis Result: {sentiment_result}")