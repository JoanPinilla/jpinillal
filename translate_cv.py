# translate_cv.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("cv_es.html", "r", encoding="utf-8") as f:
    html_text = f.read()

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a professional translator. Translate the HTML content from Spanish to English, keeping all tags and structure unchanged."
        },
        {
            "role": "user",
            "content": html_text
        }
    ],
    temperature=0.3
)

translated = response.choices[0].message.content.strip()

with open("cv_en.html", "w", encoding="utf-8") as f:
    f.write(translated)
