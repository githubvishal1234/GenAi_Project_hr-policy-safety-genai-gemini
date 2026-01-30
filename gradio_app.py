import gradio as gr
from app import hr_chatbot

gr.Interface(
    fn=hr_chatbot,
    inputs=gr.Textbox(lines=4, label="Ask HR Policy Question"),
    outputs=gr.Textbox(label="HR Assistant Response"),
    title="HR Policy Safety GenAI (Gemini)",
    description="Secure HR chatbot with prompt-injection protection"
).launch()
