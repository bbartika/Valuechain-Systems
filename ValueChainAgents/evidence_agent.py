from crewai import Agent, LLM
from ValueChainTools import search_industry_information
# llm = LLM(
#     model="ollama/llama3.2",
#     base_url="http://localhost:11434"
# )

from crewai import LLM

from dotenv import load_dotenv
load_dotenv()
llm = LLM(model="gemini/gemini-3.5-flash")





evidence_expert = Agent(

    role="Evidence Verification Expert",

    goal="""
    Find reliable evidence supporting the AI opportunity
    recommendations.

    Identify credible research papers, industry reports,
    government sources, company case studies and other
    trustworthy sources.

    For each important recommendation, explain which
    source supports the claim.
    """,

    backstory="""
    You are a research verification specialist.
    You do not accept unsupported AI recommendations.
    You search for evidence and connect each recommendation
    to its supporting sources.
    """,

    tools=[search_industry_information],

    llm=llm,

    verbose=True,

    max_iter=5,

    allow_delegation=False
)