from crewai import Task
def final_analysis_task(
    agent,
    industry,
    opportunity_task,
    evidence_task
):

    return Task(

        description=f"""
        Produce the final Value Chain AI analysis for:

        INDUSTRY:
        {industry}

        Combine:

        - Value-chain analysis
        - Business problems
        - AI opportunities
        - AI capabilities
        - Benefits
        - Risks
        - Evidence
        - Priority information

        Answer:

        1. Where across the industry's value chain
           can AI create the greatest value?

        2. Why?

        3. What evidence supports the recommendation?

        Rank the strongest opportunities first.
        """,

        expected_output="""
        Final structured analysis containing:

        Industry
        Value Chain
        Processes
        Business Problems
        AI Opportunities
        AI Capabilities
        Benefits
        Risks
        Priority
        Evidence

        Also provide the TOP AI OPPORTUNITIES.
        """,

        context=[
            opportunity_task,
            evidence_task
        ],

        agent=agent
    )