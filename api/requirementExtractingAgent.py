import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import api.constants as constants


class RequirementExtractingAgent:
    """Requirement Extracting Agent"""

    def __init__(self):
        """Initialise karega"""

        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        self.model = genai.GenerativeModel(
            model_name=constants.REQUIREMENT_EXTRACTOR_MODEL,
            system_instruction=constants.REQUIREMENT_EXTRACTOR_SYSTEM_PROMPT,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=constants.REQUIREMENT_EXTRACTOR_SCHEMA,
            ),
        )

    def generate_llm_response(self, user_prompt):
        """LLM Response dega"""

        result = self.model.generate_content(user_prompt)
        return result.text

    def generate_user_prompt(self, user_natural_language_text):
        """User prompt generate hoga"""

        user_prompt = f"Extract the requirements from the following text:\n\n{user_natural_language_text}"

        return user_prompt

    def extract_requirements(self, user_natural_language_text):
        """Natural language text se requirements extract karega"""

        user_prompt = self.generate_user_prompt(user_natural_language_text)

        response = self.generate_llm_response(user_prompt)

        extracted_requirements = json.loads(response)["requirement_set"]
        return extracted_requirements


if __name__ == "__main__":
    requirement_extracting_agent = RequirementExtractingAgent()
    user_natural_language_text = "We are planning a 3-day event in New York City. We need a hotel with 4-star quality, accommodation, and food provided. We require WiFi and an auditorium with a capacity of 100 people. The event is for a company of 50 people in the age group of 25-40. The budget is $5000. The event title is 'Annual Conference'."
    extracted_requirements = requirement_extracting_agent.extract_requirements(
        user_natural_language_text
    )
    print(extracted_requirements)
