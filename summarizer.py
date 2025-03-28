import openai
import os

def summarize_resume(resume_text):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
You are an AI assistant that summarizes professional resumes.

Here is a resume:
"""
{resume_text}

"""
Generate a concise summary highlighting the candidate's strengths, domain expertise, and job readiness.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert resume reviewer and summarizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=300
    )

    return response['choices'][0]['message']['content']
