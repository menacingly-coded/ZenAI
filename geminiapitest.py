import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key)

def chat_with_gemini(query):
    """Send query to Gemini AI and get response"""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(query)
    return response.text

# Example query
query = "Hello, how are you?"
response = chat_with_gemini(query)
print("AI:", response)
