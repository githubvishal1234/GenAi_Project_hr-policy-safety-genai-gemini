from gemini_llm import call_gemini

while True:
    user_input = input("User: ")
    print("Bot:", call_gemini(user_input))
