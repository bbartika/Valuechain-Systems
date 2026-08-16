from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults


@tool
def search_industry_information(query: str):
    """
    Search the web for information about an industry,
    its value chain, processes, business problems,
    AI applications, and supporting evidence.
    """

    search_tool = DuckDuckGoSearchResults(
        num_results=8,
        verbose=True
    )

    return search_tool.run(query)