from pydantic_ai import Agent, RunContext
from .models import FitnessProfile, FitnessReportResult

fitness_agent = Agent(
    model="gpt-4o",
    deps_type=FitnessProfile,
    output_type=FitnessReportResult,
    output_retries=3,
    system_prompt="Create personalized FitnessReportResult based on user's information provided."
    "for motivational quotes call the get_motivation tool and pick the single best one from the list you receive."
)

motivational_agent = Agent(
    model="gpt-4o",
    output_type=list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status.",
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile]) -> str:
    fitness_data = ctx.deps
    return f"User fitness profile and goals: {fitness_data!r}"


@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> list[str]:
    return await motivational_agent.run(
        f"Please generate 5 motivational quotes about working out and eating healthy.")


async def analyze_profile(profile: FitnessProfile) -> FitnessReportResult:
    result = await fitness_agent.run("Create a personalized fitness and nutrition plan.", deps=profile)
    return result.output
