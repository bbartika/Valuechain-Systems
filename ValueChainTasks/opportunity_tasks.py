from crewai import Task
def opportunity_task(
    agent,
    industry,
    value_chain_task
):

    return Task(

        description=f"""
        Analyze the following industry:

        {industry}

        Using the constructed value chain, analyze
        every major stage and process.

        For every process identify:

        1. Business problems
        2. AI opportunities
        3. Relevant AI capabilities
        4. Potential benefits
        5. Implementation risks

        Do not provide generic AI suggestions.

        Recommendations must be connected to
        specific business problems.
        """,

        expected_output="""
        For every value-chain stage:

        Stage
        ↓
        Process
        ↓
        Business Problem
        ↓
        AI Opportunity
        ↓
        AI Capability
        ↓
        Benefits
        ↓
        Risks
        """,

        context=[value_chain_task],

        agent=agent
    )