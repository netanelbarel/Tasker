import openai
import os

openai.api_key = os.environ.get("API_KEY")

def generate_text(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded, sleeping for {e.time_until_rate_limit_reset} seconds")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    return response.choices[0].text.strip()
