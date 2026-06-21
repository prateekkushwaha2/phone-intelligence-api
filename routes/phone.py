from fastapi import APIRouter
from services.phone_lookup import lookup_phone
from services.risk_engine import calculate_risk

router = APIRouter()

@router.get("/phone/{number}")
def phone_intelligence(number: str):
  data = lookup_phone(number)
  risk = calculate_risk(data)
  return {
    "phone": data,
    "risk": risk
  }
