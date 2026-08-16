from crewai import Task


def research_task(agent, industry):

    return Task(

        description=f"""
        Research the following industry:

        INDUSTRY:
        {industry}

        Investigate:

        1. Major value-chain stages
        2. Important processes
        3. Industry structure
        4. Major operational/business problems
        5. Existing AI applications
        6. Relevant industry trends
        7. Reliable supporting sources

        IMPORTANT:

        Do not assume the industry structure.
        Research it dynamically.

        The industry may be completely unfamiliar.
        """,

        expected_output="""
        A detailed research report containing:

        - industry overview
        - major value-chain stages
        - processes
        - business problems
        - relevant AI applications
        - supporting sources
        """,

        agent=agent
    )