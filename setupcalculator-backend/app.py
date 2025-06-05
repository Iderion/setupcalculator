from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from logic.aerodynamics import calculate_aero_adjustments
from logic.tire_management import calculate_tire_adjustments
from logic.suspension import calculate_suspension_adjustments

app = FastAPI()

class SetupRequest(BaseModel):
    track: str
    temperature: float
    fuel: float
    top_speed: float
    front_tire_wear: float
    rear_tire_wear: float
    understeer: bool
    oversteer: bool
    target: str
    current_setup: dict

@app.post("/calculate-setup")
async def calculate_setup(request: SetupRequest):
    try:
        # Aerodynamische Anpassungen berechnen
        aero_adjustments = calculate_aero_adjustments(
            request.current_setup,
            request.top_speed,
            request.understeer,
            request.oversteer,
            request.target
        )
        
        # Reifenanpassungen berechnen
        tire_adjustments = calculate_tire_adjustments(
            request.current_setup,
            request.front_tire_wear,
            request.rear_tire_wear,
            request.temperature,
            request.target
        )
        
        # Dämpfereinstellungen berechnen
        suspension_adjustments = calculate_suspension_adjustments(
            request.current_setup,
            request.understeer,
            request.oversteer,
            request.fuel,
            request.target
        )
        
        # Ergebnisse zusammenführen
        result = {
            "setup_proposal": {**request.current_setup, **aero_adjustments, **tire_adjustments, **suspension_adjustments},
            "reasoning": [
                *aero_adjustments.get("reasons", []),
                *tire_adjustments.get("reasons", []),
                *suspension_adjustments.get("reasons", [])
            ]
        }
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))