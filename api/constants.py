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


# Itinerary Generator

# To be improved

ITINERARY_GENERATOR_SYSTEM_PROMPT = """You are an itinerary generator for events. Your task is to generate an itinerary based on the provided requirements. Follow these steps:
1. Read the input requirements provided.
2. Generate a detailed itinerary for the event based on the requirements.
3. Ensure that the itinerary is well-structured and covers all the necessary aspects.
4. Include details such as event schedule, activities, locations, accommodations, etc.
"""

ITINERARY_GENERATOR_MODEL = "gemini-1.5-flash-latest"

ITINERARY_GENERATOR_SCHEMA = content.Schema(
    type=content.Type.OBJECT,
    enum=[],
    required=["itinerary"],
    properties={
        "itinerary": content.Schema(
            type=content.Type.OBJECT,
            enum=[],
            required=[
                "company_name",
                "event_title",
                "number_of_days",
                "date_range",
                "location",
                "budget",
                "hotel_details",
                "food_arrangements",
                "schedule",
                "miscellaneous",
                "weather",
            ],
            properties={
                "company_name": content.Schema(
                    type=content.Type.STRING,
                ),
                "event_title": content.Schema(
                    type=content.Type.STRING,
                ),
                "number_of_days": content.Schema(
                    type=content.Type.INTEGER,
                ),
                "date_range": content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=["start_date", "end_date"],
                    properties={
                        "start_date": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "end_date": content.Schema(
                            type=content.Type.STRING,
                        ),
                    },
                ),
                "location": content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=["country", "state", "city"],
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
                    },
                ),
                "budget": content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=["currency", "total_amount", "breakdown"],
                    properties={
                        "currency": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "total_amount": content.Schema(
                            type=content.Type.NUMBER,
                        ),
                        "breakdown": content.Schema(
                            type=content.Type.OBJECT,
                            properties={
                                "accommodation": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                                "food": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                                "venue": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                                "miscellaneous": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                            },
                        ),
                    },
                ),
                "hotel_details": content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=[
                        "is_accommodation_required",
                        "hotel_quality",
                        "hotel_name",
                        "hotel_characteristics",
                        "hotel_id",
                        "check_in_time",
                        "check_out_time",
                        "is_auditorium_required",
                        "is_wifi_required",
                        "price",
                    ],
                    properties={
                        "is_accommodation_required": content.Schema(
                            type=content.Type.BOOLEAN,
                        ),
                        "hotel_quality": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "hotel_name": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "hotel_characteristics": content.Schema(
                            type=content.Type.ARRAY,
                            items=content.Schema(
                                type=content.Type.STRING,
                            ),
                        ),
                        "hotel_id": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "check_in_time": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "check_out_time": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "is_auditorium_required": content.Schema(
                            type=content.Type.BOOLEAN,
                        ),
                        "auditorium_capacity": content.Schema(
                            type=content.Type.INTEGER,
                        ),
                        "is_wifi_required": content.Schema(
                            type=content.Type.BOOLEAN,
                        ),
                        "price": content.Schema(
                            type=content.Type.OBJECT,
                            enum=[],
                            required=["currency", "amount"],
                            properties={
                                "currency": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "amount": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                            },
                        ),
                    },
                ),
                "food_arrangements": content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=["is_food_required"],
                    properties={
                        "is_food_required": content.Schema(
                            type=content.Type.BOOLEAN,
                        ),
                        "dietary_restrictions": content.Schema(
                            type=content.Type.ARRAY,
                            items=content.Schema(
                                type=content.Type.STRING,
                            ),
                        ),
                        "meal_schedule": content.Schema(
                            type=content.Type.OBJECT,
                            properties={
                                "breakfast": content.Schema(
                                    type=content.Type.OBJECT,
                                    properties={
                                        "start_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "end_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                    },
                                ),
                                "lunch": content.Schema(
                                    type=content.Type.OBJECT,
                                    properties={
                                        "start_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "end_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                    },
                                ),
                                "dinner": content.Schema(
                                    type=content.Type.OBJECT,
                                    properties={
                                        "start_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "end_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                    },
                                ),
                            },
                        ),
                    },
                ),
                "schedule": content.Schema(
                    type=content.Type.ARRAY,
                    items=content.Schema(
                        type=content.Type.OBJECT,
                        enum=[],
                        required=["day_number", "date", "time_table"],
                        properties={
                            "day_number": content.Schema(
                                type=content.Type.NUMBER,
                            ),
                            "date": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "time_table": content.Schema(
                                type=content.Type.ARRAY,
                                items=content.Schema(
                                    type=content.Type.OBJECT,
                                    enum=[],
                                    required=[
                                        "start_time",
                                        "end_time",
                                        "activity",
                                        "location",
                                        "details",
                                    ],
                                    properties={
                                        "start_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "end_time": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "activity": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "location": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                        "details": content.Schema(
                                            type=content.Type.STRING,
                                        ),
                                    },
                                ),
                            ),
                        },
                    ),
                ),
                "nearby_tourist_spots": content.Schema(
                    type=content.Type.ARRAY,
                    items=content.Schema(
                        type=content.Type.OBJECT,
                        properties={
                            "venue_name": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "venue_distance_from_location": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "details": content.Schema(
                                type=content.Type.STRING,
                            ),
                        },
                    ),
                ),
                "ongoing_festivals": content.Schema(
                    type=content.Type.ARRAY,
                    items=content.Schema(
                        type=content.Type.OBJECT,
                        properties={
                            "festival_name": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "venue_name": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "venue_distance_from_location": content.Schema(
                                type=content.Type.STRING,
                            ),
                            "details": content.Schema(
                                type=content.Type.STRING,
                            ),
                        },
                    ),
                ),
                "miscellaneous": content.Schema(
                    type=content.Type.OBJECT,
                    properties={
                        "dress_code": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "event_hashtag": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "other_notes": content.Schema(
                            type=content.Type.ARRAY,
                            items=content.Schema(
                                type=content.Type.STRING,
                            ),
                        ),
                    },
                ),
                "weather": content.Schema(
                    type=content.Type.STRING,
                ),
            },
        ),
    },
)
