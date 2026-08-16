from crewai import Task
def evidence_task(
    agent,
    industry,
    opportunity_task
):

    return Task(

        description=f"""
        Verify the AI opportunities identified for:

        INDUSTRY:
        {industry}

        For important recommendations, find supporting
        evidence from reliable external sources.

        Prefer:

        - research papers
        - government sources
        - industry reports
        - company case studies
        - reputable business publications

        For each recommendation provide:

        Source title
        Source URL
        Claim supported
        Confidence
        """,

        expected_output="""
        Evidence-backed recommendations with:

        Recommendation
        Source
        URL
        Claim supported
        Confidence
        """,

        context=[opportunity_task],

        agent=agent
    )