import uvicorn
from fastapi import FastAPI
from api.requirementExtractingAgent import RequirementExtractingAgent
from api.locationSuggestingAgent import LocationSuggestingAgent
from pydantic import BaseModel


class Prompt(BaseModel):
    prompt: str


class RequirementSet(BaseModel):
    company_name: str
    event_title: str
    event_mood: str
    number_of_days: str
    date_range: str
    number_of_days: str
    number_of_people: str
    age_group_of_people: str
    country: str
    state: str
    city: str
    budget: str
    hotel_quality: str
    is_accomodation_required: str
    is_food_required: str
    is_wifi_required: str
    is_auditorium_required: str
    auditorium_capacity: str
    itinerary_requirements: list
    hotel_characteristics: list
    dietary_restrictions: str


app = FastAPI()
req_agent = RequirementExtractingAgent()
loc_agent = LocationSuggestingAgent()


@app.post("/extract-requirements/")
async def extract_requirements(prompt: Prompt):
    return req_agent.extract_requirements(prompt)


@app.post("/suggest-locations/")
async def suggest_locations(requirement_set: RequirementSet):
    return loc_agent.suggest_locations(requirement_set)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
