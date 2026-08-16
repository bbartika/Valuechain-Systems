from crewai import Agent, LLM
from ValueChainTools import search_industry_information


from dotenv import load_dotenv
load_dotenv()

llm = LLM(model="gemini/gemini-3.5-flash")







opportunity_expert = Agent(

    role="AI Opportunity Intelligence Expert",

    goal="""
    Analyze each value-chain stage and its processes.

    Identify:
    - business problems
    - AI opportunities
    - relevant AI capabilities
    - potential benefits
    - implementation risks

    Base recommendations on the provided industry research.
    """,

    backstory="""
    You are an AI strategy consultant who identifies
    where artificial intelligence can create measurable
    business value across industry value chains.
    """,

    tools=[search_industry_information],

    llm=llm,

    verbose=True,

    max_iter=5,

    allow_delegation=False
)