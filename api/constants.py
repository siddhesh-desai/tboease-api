from google.ai.generativelanguage_v1beta.types import content

# Requirement Extractor Constants

REQUIREMENT_EXTRACTOR_SYSTEM_PROMPT = """You are an intelligent feature extractor. Your task is to extract requirements from natural language text 
and convert them into a structured JSON format. Follow these steps:
1. Carefully read the input text provided.
2. Identify and extract the following fields if mentioned: company_name, event_title, event_mood, number_of_days, date_range, number_of_people, age_group_of_people, country, state, city, budget, hotel_quality, is_accomodation_required, is_food_required, is_wifi_required, is_auditorium_required, auditorium_capacity, hotel_characteristics, dietary_restrictions, itinerary_requirements.
3. Ensure that only the fields mentioned in the input text are included in the output.
4. Return the extracted requirements in the specified JSON format.
5. If city is provided, you have to fill the country and state fields as well by your knowledge.
6. If any of the fields are not mentioned in the input text, return 'None' for those fields."""

REQUIREMENT_EXTRACTOR_MODEL = "gemini-1.5-flash-latest"

REQUIREMENT_EXTRACTOR_SCHEMA = content.Schema(
    type=content.Type.OBJECT,
    enum=[],
    required=["requirement_set"],
    properties={
        "requirement_set": content.Schema(
            type=content.Type.OBJECT,
            required=[
                "company_name",
                "event_title",
                "event_mood",
                "number_of_days",
                "date_range",
                "number_of_people",
                "age_group_of_people",
                "country",
                "state",
                "city",
                "budget",
                "hotel_quality",
                "is_accomodation_required",
                "is_food_required",
                "is_wifi_required",
                "is_auditorium_required",
                "auditorium_capacity",
                "hotel_characteristics",
                "dietary_restrictions",
                "itinerary_requirements",
            ],
            properties={
                "company_name": content.Schema(
                    type=content.Type.STRING,
                ),
                "event_title": content.Schema(
                    type=content.Type.STRING,
                ),
                "event_mood": content.Schema(
                    type=content.Type.STRING,
                ),
                "number_of_days": content.Schema(
                    type=content.Type.STRING,
                ),
                "date_range": content.Schema(
                    type=content.Type.STRING,
                ),
                "number_of_people": content.Schema(
                    type=content.Type.STRING,
                ),
                "age_group_of_people": content.Schema(
                    type=content.Type.STRING,
                ),
                "country": content.Schema(
                    type=content.Type.STRING,
                ),
                "state": content.Schema(
                    type=content.Type.STRING,
                ),
                "city": content.Schema(
                    type=content.Type.STRING,
                ),
                "budget": content.Schema(
                    type=content.Type.STRING,
                    enum=["Low", "Medium", "High", "None"],
                ),
                "hotel_quality": content.Schema(
                    type=content.Type.STRING,
                    enum=[
                        "1 Star",
                        "2 Star",
                        "3 Star",
                        "4 Star",
                        "5 Star",
                        "None",
                    ],
                ),
                "is_accomodation_required": content.Schema(
                    type=content.Type.STRING,
                    enum=["Yes", "No", "None"],
                ),
                "is_food_required": content.Schema(
                    type=content.Type.STRING,
                    enum=["Yes", "No", "None"],
                ),
                "is_wifi_required": content.Schema(
                    type=content.Type.STRING,
                    enum=["Yes", "No", "None"],
                ),
                "is_auditorium_required": content.Schema(
                    type=content.Type.STRING,
                    enum=["Yes", "No", "None"],
                ),
                "auditorium_capacity": content.Schema(
                    type=content.Type.STRING,
                ),
                "hotel_characteristics": content.Schema(
                    type=content.Type.ARRAY,
                    items=content.Schema(
                        type=content.Type.STRING,
                    ),
                ),
                "dietary_restrictions": content.Schema(
                    type=content.Type.STRING,
                ),
                "itinerary_requirements": content.Schema(
                    type=content.Type.ARRAY,
                    items=content.Schema(
                        type=content.Type.STRING,
                    ),
                ),
            },
        ),
    },
)


# Location Suggester Constants

LOCATION_SUGGESTER_SYSTEM_PROMPT = """You are a location suggester for events. Your task is to suggest 5 locations based on the provided requirements. Follow these steps:
1. Read the input requirements provided.
2. Suggest suitable locations which would be a country, state and city that matches the requirements.
3. If the country and state is already provided, suggest a city that matches the requirements.
4. If the country is already provided, suggest a state and city that matches the requirements.
5. If a city is already provided, add the country, state and explanation of the provided city and do not suggest any other location.
6. Try to cover variety of countries, states and cities in the suggestions.
7. Ensure that the suggestions are relevant and feasible.
8. Also for each location, provide a short explanation about why this location.
9. Return the suggested locations in a structured JSON format.
"""

LOCATION_SUGGESTER_MODEL = "gemini-1.5-flash-latest"

LOCATION_SUGGESTER_SCHEMA = content.Schema(
    type=content.Type.OBJECT,
    enum=[],
    required=["locations"],
    properties={
        "locations": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.OBJECT,
                enum=[],
                required=["country", "state", "city", "explanation"],
                properties={
                    "country": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "state": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "city": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "explanation": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
        ),
    },
)
