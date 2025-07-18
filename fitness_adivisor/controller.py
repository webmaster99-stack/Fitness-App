from fastapi import APIRouter
from .service import analyze_profile
from .models import FitnessProfile

router = APIRouter(
    prefix="/advisor",
    tags=["Fitness Advisor"]
)


@router.post("/analise")
async def analyze_fitness(fitness_profile: FitnessProfile):
    return await analyze_profile(fitness_profile)