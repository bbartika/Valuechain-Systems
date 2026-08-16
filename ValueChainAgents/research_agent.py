from crewai import Agent, LLM
from ValueChainTools import search_industry_information


from dotenv import load_dotenv
load_dotenv()
llm = LLM(model="gemini/gemini-3.5-flash")


research_expert = Agent(

    role="Industry Research Expert",

    goal="""
    Research the user's selected industry and collect reliable
    information about its end-to-end value chain, major processes,
    business challenges, AI adoption and supporting evidence.
    """,

    backstory="""
    You are a senior industry research analyst.
    You specialize in understanding unfamiliar industries
    using external research rather than relying only on
    your pretrained knowledge.
    """,

    tools=[search_industry_information],

    llm=llm,

    verbose=True,

    max_iter=5,

    allow_delegation=False
)
# # --------------------------------------------------
# # RESEARCH AGENT
# # --------------------------------------------------

# research_expert = Agent(

#     role="Industry Research Expert",

#     goal="""
#     Research the user's selected industry and collect
#     reliable, current information about its end-to-end
#     value chain, major processes, business challenges,
#     AI adoption and supporting evidence.

#     Use the available MCP research tools whenever
#     external information is required.
#     """,

#     backstory="""
#     You are a senior industry research analyst.

#     You specialize in researching unfamiliar industries
#     using external sources rather than relying only on
#     pretrained knowledge.

#     You must distinguish researched facts from assumptions
#     and preserve useful source information for downstream
#     evidence analysis.
#     """,

#     tools= [search_industry_information] + mcp_tools,

#     llm=llm,

#     verbose=True,

#     max_iter=5,

#     allow_delegation=False
# )