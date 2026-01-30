from google import genai

# TEMPORARY: hard-code API key (to avoid Windows env issues)
API_KEY = "AIzaSyBQBvcUTAh1u86F0Qr0M6bC7q6YdXaQdeg"

client = genai.Client(api_key=API_KEY)

def call_gemini(user_input: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=user_input
    )
    return response.text
