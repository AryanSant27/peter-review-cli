from google import genai
import os
from dotenv import load_dotenv

load_dotenv()


# You'll need to set your API key as an environment variable or pass it directly
# export GOOGLE_API_KEY="your-api-key-here"

system_prompt = (
    "You are Peter Griffin from Family Guy. Review the following code in Peter's humorous style, "
    "making sarcastic, funny, and over-the-top comments as Peter would. Keep the review short and avoid the technical jargon which can be hard to pronounce"
    "Avoid using terms that may-be hard to pronounce for a TTS system"
    "Occasionally Make references to Family Guy characters"
    "If there is some error in the code, address it but even in that maintain the gimmick"
    "Here's the code:"

)


def review(text):
    try:
        # Initialize the client
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))  # or use environment variable

        # Combine system prompt with the text
        full_prompt = f"{system_prompt}\n\n{text}"

        # Generate content using the correct method and model name
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",  # Use the experimental version
            contents=full_prompt  # Fixed: use 'contents' instead of 'content'
        )

        # Extract the text from response
        return response.text

    except Exception as e:
        print(f"Error generating review: {e}")
        return None

# Example usage (for testing)
if __name__ == "__main__":
    sample_text = "This is a sample text for review."
    result = review(sample_text)
    if result:
        print(result)
    else:
        print("Failed to generate review.")