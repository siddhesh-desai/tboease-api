import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import api.constants as constants


class LocationSuggestingAgent:
    """Location Suggesting Agent"""

    def __init__(self):
        """Initialise karega"""

        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        self.chat_history = []

        self.model = genai.GenerativeModel(
            model_name=constants.LOCATION_SUGGESTER_MODEL,
            system_instruction=constants.LOCATION_SUGGESTER_SYSTEM_PROMPT,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=constants.LOCATION_SUGGESTER_SCHEMA,
            ),
        )

    def generate_llm_response(self, user_prompt):
        """LLM Response dega"""

        history = "Chat History:\n"

        if self.chat_history != []:
            history = "\n".join([f"{role}: {text}" for role, text in self.chat_history])

        result = self.model.generate_content(f"{user_prompt}\n---\n{history}")
        return result.text

    def generate_user_prompt(self, requirement_dict, is_regeneration=False):
        """User prompt generate hoga for both first time and regeneration"""

        user_prompt = (
            ("Suggest suitable locations based on the following requirements:\n")
            if not is_regeneration
            else "Regenerate the suitable locations based on the following requirements, make sure previous locations are not repeated:\n"
        )

        for key, label in [
            ("country", "Country"),
            ("state", "State"),
            ("city", "City"),
            ("event_title", "Event Name"),
            ("event_mood", "Event Mood"),
            ("number_of_days", "Number of Days"),
            ("date_range", "Date Range"),
            ("number_of_people", "Number of People"),
            ("age_group_of_people", "Age Group of People"),
            ("budget", "Budget"),
            ("hotel_quality", "Hotel Quality"),
            ("is_accomodation_required", "Is Accomodation Required"),
            ("is_food_required", "Food Provided"),
            ("is_wifi_required", "Is WiFi Required"),
            ("is_auditorium_required", "Is Auditorium Required"),
            ("auditorium_capacity", "Auditorium Capacity"),
            ("dietary_restrictions", "Dietary Restrictions"),
            ("hotel_characteristics", "Hotel Characteristics"),
            ("itinerary_requirements", "Itinerary Requirements"),
        ]:
            if (
                key in requirement_dict
                and requirement_dict[key]
                and requirement_dict[key] != "None"
            ):
                user_prompt += f"({label}: {requirement_dict[key]})\n"

        if (
            requirement_dict["country"]
            and requirement_dict["country"] != "None"
            and requirement_dict["state"]
            and requirement_dict["state"] != "None"
        ):
            user_prompt += f"\nMake sure the suggested locations are from {requirement_dict['state']}, {requirement_dict['country']}.\n"
        elif requirement_dict["country"] and requirement_dict["country"] != "None":
            user_prompt += f"\nMake sure the suggested locations are from {requirement_dict['country']}.\n"

        return user_prompt

    def suggest_locations(self, requirements: dict, is_regeneration=False):
        """Locations suggest karega based on requirements"""

        user_prompt = self.generate_user_prompt(requirements, is_regeneration)

        response = self.generate_llm_response(user_prompt)

        self.chat_history.append({"USER", user_prompt})
        self.chat_history.append({"LLM", response})

        suggested_locations = json.loads(response)["locations"]
        return suggested_locations


if __name__ == "__main__":
    agent = LocationSuggestingAgent()
    requirements = {
        "company_name": "Tech Corp",
        "event_title": "Annual Meetup",
        "event_mood": "Professional",
        "number_of_days": "3",
        "date_range": "2023-11-01 to 2023-11-03",
        "number_of_people": "100",
        "age_group_of_people": "25-45",
        "country": "USA",
        "state": "New York",
        "city": "New York City",
        "budget": "Medium",
        "hotel_quality": "4 Star",
        "is_accomodation_required": "Yes",
        "is_food_required": "Yes",
        "is_wifi_required": "Yes",
        "is_auditorium_required": "Yes",
        "auditorium_capacity": "150",
        "hotel_characteristics": ["Modern", "Business-friendly"],
        "dietary_restrictions": "Vegetarian",
        "itinerary_requirements": ["Workshops", "Networking Sessions"],
    }
    suggestions = agent.suggest_locations(requirements)
    print("-------------------\n")
    print(agent.chat_history)
    print("-------------------\n")
    print(suggestions)
