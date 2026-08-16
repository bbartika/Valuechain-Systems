from crewai import Agent, LLM
from ValueChainTools import search_industry_information

from dotenv import load_dotenv
load_dotenv()
llm = LLM(model="gemini/gemini-3.5-flash")


value_chain_expert = Agent(

    role="Value Chain Analysis Expert",

    goal="""
    Construct the complete end-to-end value chain of the
    selected industry using the research provided.

    Identify the major stages and important processes
    within each stage.

    Do not rely on hard-coded industry-specific stages.
    """,

    backstory="""
    You are a business strategy consultant specializing
    in value-chain analysis.

    You can analyze unfamiliar industries and construct
    their value chains from research evidence.
    """,

    tools=[search_industry_information],

    llm=llm,

    verbose=True,

    max_iter=5,

    allow_delegation=False
)