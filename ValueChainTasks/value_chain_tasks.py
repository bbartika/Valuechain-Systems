from crewai import Task


def value_chain_task(agent, industry, research_result):

    return Task(

        description=f"""
        Construct the end-to-end value chain for:

        INDUSTRY:
        {industry}

        Use the following research produced by the previous task:

        ---------------- RESEARCH ----------------

        {research_result}

        --------------------------------------------

        Identify:

        Stage 1
        Stage 2
        Stage 3
        ...

        For every stage identify its major processes.

        IMPORTANT:

        Do NOT use hard-coded industry stages.

        Construct the value chain from the research.
        """,

        expected_output="""
        A structured value chain containing:

        Industry
        ↓
        Value Chain Stages
        ↓
        Processes
        """,

        agent=agent
    )