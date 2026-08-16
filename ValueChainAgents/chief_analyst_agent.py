from crewai import Agent, LLM
from ValueChainTools import search_industry_information

from dotenv import load_dotenv
load_dotenv()
llm = LLM(model="gemini/gemini-3.5-flash")

chief_analyst = Agent(

    role="Chief Value Chain AI Analyst",
    

    goal="""
    Synthesize the research, value chain, AI opportunities,
    evidence, benefits and risks.

    Determine where AI can create the greatest value across
    the industry's value chain.

    Provide a clear ranked recommendation and explain why.
    """,

    backstory="""
    You are a senior AI strategy consultant.
    Your responsibility is to turn industry research into
    actionable, evidence-backed AI investment recommendations.
    """,

    llm=llm,

    verbose=True,

    max_iter=5,

    allow_delegation=False
)