import uvicorn
from fastapi import FastAPI
from api.requirementExtractingAgent import RequirementExtractingAgent
from api.locationSuggestingAgent import LocationSuggestingAgent
from pydantic import BaseModel
from typing import Union
from api.itineraryGeneratingAgent import ItineraryGeneratingAgent
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()


class Prompt(BaseModel):
    prompt: str


class RequirementSet(BaseModel):
    company_name: str
    event_title: str
    event_mood: str
    number_of_days: Union[str, int]
    date_range: str
    number_of_days: Union[str, int]
    number_of_people: Union[str, int]
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
    auditorium_capacity: Union[str, int]
    itinerary_requirements: list
    hotel_characteristics: list
    dietary_restrictions: str
    owner_id: Union[str, None] = None


app = FastAPI()
req_agent = RequirementExtractingAgent()
loc_agent = LocationSuggestingAgent()
itin_agent = ItineraryGeneratingAgent()

app.mongodb_client = MongoClient(os.getenv("ATLAS_URI"))
app.database = app.mongodb_client[os.getenv("DB_NAME")]


@app.post("/extract-requirements/")
async def extract_requirements(prompt: Prompt):
    return req_agent.extract_requirements(prompt)


@app.post("/suggest-locations/")
async def suggest_locations(requirement_set: RequirementSet):
    return loc_agent.suggest_locations(requirement_set)


@app.post("/generate-itinerary/")
async def generate_itinerary(requirement_set: RequirementSet):
    print("----")
    print(requirement_set)
    generated_itinerary = itin_agent.generate_itinerary(requirement_set)
    generated_itinerary["owner_id"] = requirement_set.owner_id
    print(generate_itinerary)
    result = app.database["itineraries"].insert_one(generated_itinerary)
    return {"itinerary_id": str(result.inserted_id)}


from bson import ObjectId
from fastapi import HTTPException


@app.get("/get-itinerary/{itinerary_id}")
async def get_itinerary(itinerary_id: str):
    try:
        itinerary = app.database["itineraries"].find_one(
            {"_id": ObjectId(itinerary_id)}
        )
        if itinerary is None:
            raise HTTPException(status_code=404, detail="Itinerary not found")
        itinerary["_id"] = str(itinerary["_id"])
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return itinerary


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
