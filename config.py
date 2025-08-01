import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Example: Access API key or other secrets
OPENAI_API_KEY = os.getenv('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')
HUGGINGFACE_API_KEY = os.getenv('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')