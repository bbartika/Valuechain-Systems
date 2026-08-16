# import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()

# from crewai import Crew, Process


# from crewai import LLM
# llm = LLM(model="gemini/gemini-3.5-flash")
 
# print(llm.call("Say hello in one sentence."))

# from ValueChainAgents.research_agent import research_expert
# from ValueChainAgents.value_chain_agent import value_chain_expert
# from ValueChainAgents.opportunity_agent import opportunity_expert
# from ValueChainAgents.evidence_agent import evidence_expert
# from ValueChainAgents.chief_analyst_agent import chief_analyst

# from ValueChainTasks.research_tasks import research_task
# from ValueChainTasks.value_chain_tasks import value_chain_task
# from ValueChainTasks.opportunity_tasks import opportunity_task
# from ValueChainTasks.evidence_tasks import evidence_task
# from ValueChainTasks.final_analysis_tasks import final_analysis_task

# from score import calculate_priority



# st.title("🏭 ValueChain AI")

# st.markdown("""
# ### AI-Powered Value Chain Opportunity Intelligence

# Enter any industry and the system will dynamically:

# - Research the industry
# - Construct its value chain
# - Identify business problems
# - Find AI opportunities
# - Identify relevant AI capabilities
# - Analyze benefits and risks
# - Find supporting evidence
# - Rank AI opportunities
# """)


# industry = st.text_input(
#     "🏭 Enter Industry",
#     "Agriculture"
# )


# if st.button("🚀 Analyze Industry"):

#     if not industry.strip():

#         st.error("Please enter an industry.")

#     else:

#         st.info(
#             f"🔎 Analyzing the {industry} industry..."
#         )

#         # -------------------------
#         # CREATE TASKS
#         # -------------------------

#         research = research_task(
#             research_expert,
#             industry
#         )

#         value_chain = value_chain_task(
#             value_chain_expert,
#             industry,
#             research
#         )

#         opportunities = opportunity_task(
#             opportunity_expert,
#             industry,
#             value_chain
#         )

#         evidence = evidence_task(
#             evidence_expert,
#             industry,
#             opportunities
#         )

#         final_analysis = final_analysis_task(
#             chief_analyst,
#             industry,
#             opportunities,
#             evidence
#         )

#         # -------------------------
#         # CREATE CREW
#         # -------------------------

#         crew = Crew(

#             agents=[
#                 research_expert,
#                 value_chain_expert,
#                 opportunity_expert,
#                 evidence_expert,
#                 chief_analyst
#             ],

#             tasks=[
#                 research,
#                 value_chain,
#                 opportunities,
#                 evidence,
#                 final_analysis
#             ],

#             process=Process.sequential,

#             verbose=True
#         )

#         # -------------------------
#         # RUN
#         # -------------------------

#         import time

#         max_retries = 3
#         result = None

#         for attempt in range(max_retries):
#             try:
#                 result = crew.kickoff()
#                 break
#             except Exception as e:
#                 if "503" in str(e) or "UNAVAILABLE" in str(e):
#                     st.warning(f"Model busy, retrying... ({attempt+1}/{max_retries})")
#                     time.sleep(5)
#                 else:
#                     raise

#         if result is None:
#             st.error("The model is still overloaded after several attempts. Please try again in a few minutes.")
#             st.stop()


#         # -------------------------
#         # DISPLAY
#         # -------------------------

#         st.success(
#             f"✅ {industry} analysis completed!"
#         )

#         st.subheader(
#             "📊 Value Chain AI Analysis"
#         )

#         st.markdown(str(result))
import streamlit as st
import time

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from crewai import LLM

# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = LLM(
    model="gemini/gemini-3.5-flash"
)

# --------------------------------------------------
# AGENTS
# --------------------------------------------------

from ValueChainAgents.research_agent import research_expert
from ValueChainAgents.value_chain_agent import value_chain_expert
from ValueChainAgents.opportunity_agent import opportunity_expert
from ValueChainAgents.evidence_agent import evidence_expert
from ValueChainAgents.chief_analyst_agent import chief_analyst

# --------------------------------------------------
# TASKS
# --------------------------------------------------

from ValueChainTasks.research_tasks import research_task
from ValueChainTasks.value_chain_tasks import value_chain_task
from ValueChainTasks.opportunity_tasks import opportunity_task
from ValueChainTasks.evidence_tasks import evidence_task
from ValueChainTasks.final_analysis_tasks import final_analysis_task

from score import calculate_priority


# ==================================================
# SESSION STATE
# ==================================================

if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "value_chain_result" not in st.session_state:
    st.session_state.value_chain_result = None

if "opportunity_result" not in st.session_state:
    st.session_state.opportunity_result = None

if "evidence_result" not in st.session_state:
    st.session_state.evidence_result = None

if "final_analysis_result" not in st.session_state:
    st.session_state.final_analysis_result = None


# ==================================================
# HELPER FUNCTION
# ==================================================

def run_crew(agents, tasks):

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    max_retries = 3

    for attempt in range(max_retries):

        try:

            result = crew.kickoff()

            return result

        except Exception as e:

            if "503" in str(e) or "UNAVAILABLE" in str(e):

                st.warning(
                    f"Model busy, retrying... "
                    f"({attempt + 1}/{max_retries})"
                )

                time.sleep(5)

            else:

                raise

    return None


# ==================================================
# PAGE
# ==================================================

st.title("🏭 ValueChain AI")

st.markdown("""
### AI-Powered Value Chain Opportunity Intelligence

Enter any industry and analyze it step-by-step.
""")

# --------------------------------------------------
# INDUSTRY INPUT
# --------------------------------------------------

industry = st.text_input(
    "🏭 Enter Industry",
    "Agriculture"
)


# ==================================================
# TASK BUTTONS
# ==================================================

st.subheader("🔎 Analysis Tasks")


# ==================================================
# ROW 1
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# 1. RESEARCH INDUSTRY
# --------------------------------------------------

with col1:

    if st.button(
        "🔍 Research Industry",
        use_container_width=True
    ):

        if not industry.strip():

            st.error("Please enter an industry.")

        else:

            st.info(
                f"🔎 Researching the {industry} industry..."
            )

            research = research_task(
                research_expert,
                industry
            )

            result = run_crew(
                agents=[
                    research_expert
                ],
                tasks=[
                    research
                ]
            )

            if result is not None:

                st.session_state.research_result = result

                # Clear dependent results
                st.session_state.value_chain_result = None
                st.session_state.opportunity_result = None
                st.session_state.evidence_result = None
                st.session_state.final_analysis_result = None

                st.success(
                    "✅ Industry research completed!"
                )

                st.subheader("🔍 Industry Research")

                st.markdown(str(result))


# --------------------------------------------------
# 2. VALUE CHAIN
# --------------------------------------------------

with col2:

    if st.button(
        "🔗 Construct Value Chain",
        use_container_width=True
    ):

        if not industry.strip():

            st.error("Please enter an industry.")

        elif st.session_state.research_result is None:

            st.warning(
                "⚠️ Please run 'Research Industry' first."
            )

        else:

            st.info(
                f"🔗 Constructing value chain for {industry}..."
            )

            value_chain = value_chain_task(
                value_chain_expert,
                industry,
                st.session_state.research_result
            )

            result = run_crew(
                agents=[
                    value_chain_expert
                ],
                tasks=[
                    value_chain
                ]
            )

            if result is not None:

                st.session_state.value_chain_result = result

                # Clear dependent results
                st.session_state.opportunity_result = None
                st.session_state.evidence_result = None
                st.session_state.final_analysis_result = None

                st.success(
                    "✅ Value chain constructed!"
                )

                st.subheader("🔗 Value Chain")

                st.markdown(str(result))


# ==================================================
# ROW 2
# ==================================================

col3, col4 = st.columns(2)


# --------------------------------------------------
# 3. AI OPPORTUNITIES
# --------------------------------------------------

with col3:

    if st.button(
        "🤖 Find AI Opportunities",
        use_container_width=True
    ):

        if not industry.strip():

            st.error("Please enter an industry.")

        elif st.session_state.value_chain_result is None:

            st.warning(
                "⚠️ Please construct the Value Chain first."
            )

        else:

            st.info(
                f"🤖 Finding AI opportunities for {industry}..."
            )

            opportunities = opportunity_task(
                opportunity_expert,
                industry,
                st.session_state.value_chain_result
            )

            result = run_crew(
                agents=[
                    opportunity_expert
                ],
                tasks=[
                    opportunities
                ]
            )

            if result is not None:

                st.session_state.opportunity_result = result

                # Clear dependent results
                st.session_state.evidence_result = None
                st.session_state.final_analysis_result = None

                st.success(
                    "✅ AI opportunities identified!"
                )

                st.subheader("🤖 AI Opportunities")

                st.markdown(str(result))


# --------------------------------------------------
# 4. SUPPORTING EVIDENCE
# --------------------------------------------------

with col4:

    if st.button(
        "📚 Find Supporting Evidence",
        use_container_width=True
    ):

        if not industry.strip():

            st.error("Please enter an industry.")

        elif st.session_state.opportunity_result is None:

            st.warning(
                "⚠️ Please find AI Opportunities first."
            )

        else:

            st.info(
                f"📚 Finding evidence for {industry}..."
            )

            evidence = evidence_task(
                evidence_expert,
                industry,
                st.session_state.opportunity_result
            )

            result = run_crew(
                agents=[
                    evidence_expert
                ],
                tasks=[
                    evidence
                ]
            )

            if result is not None:

                st.session_state.evidence_result = result

                st.session_state.final_analysis_result = None

                st.success(
                    "✅ Supporting evidence found!"
                )

                st.subheader("📚 Supporting Evidence")

                st.markdown(str(result))


# ==================================================
# ROW 3
# ==================================================

col5, col6 = st.columns(2)


# --------------------------------------------------
# 5. FINAL ANALYSIS
# --------------------------------------------------

with col5:

    if st.button(
        "🏆 Rank AI Opportunities",
        use_container_width=True
    ):

        if not industry.strip():

            st.error("Please enter an industry.")

        elif st.session_state.opportunity_result is None:

            st.warning(
                "⚠️ Please find AI Opportunities first."
            )

        elif st.session_state.evidence_result is None:

            st.warning(
                "⚠️ Please find Supporting Evidence first."
            )

        else:

            st.info(
                f"🏆 Ranking AI opportunities for {industry}..."
            )

            final_analysis = final_analysis_task(
                chief_analyst,
                industry,
                st.session_state.opportunity_result,
                st.session_state.evidence_result
            )

            result = run_crew(
                agents=[
                    chief_analyst
                ],
                tasks=[
                    final_analysis
                ]
            )

            if result is not None:

                st.session_state.final_analysis_result = result

                st.success(
                    "✅ AI opportunities ranked!"
                )

                st.subheader(
                    "🏆 Final AI Opportunity Ranking"
                )

                st.markdown(str(result))


# ==================================================
# CLEAR RESULTS
# ==================================================

with col6:

    if st.button(
        "🗑️ Clear Analysis",
        use_container_width=True
    ):

        st.session_state.research_result = None
        st.session_state.value_chain_result = None
        st.session_state.opportunity_result = None
        st.session_state.evidence_result = None
        st.session_state.final_analysis_result = None

        st.success(
            "✅ Analysis cleared."
        )


# ==================================================
# DISPLAY PREVIOUS RESULTS
# ==================================================

if (
    st.session_state.research_result is not None
    or st.session_state.value_chain_result is not None
    or st.session_state.opportunity_result is not None
    or st.session_state.evidence_result is not None
    or st.session_state.final_analysis_result is not None
):

    st.divider()

    st.subheader("📊 Analysis Results")

    # Research
    if st.session_state.research_result is not None:

        with st.expander(
            "🔍 Industry Research",
            expanded=False
        ):

            st.markdown(
                str(st.session_state.research_result)
            )

    # Value Chain
    if st.session_state.value_chain_result is not None:

        with st.expander(
            "🔗 Value Chain",
            expanded=False
        ):

            st.markdown(
                str(st.session_state.value_chain_result)
            )

    # Opportunities
    if st.session_state.opportunity_result is not None:

        with st.expander(
            "🤖 AI Opportunities",
            expanded=False
        ):

            st.markdown(
                str(st.session_state.opportunity_result)
            )

    # Evidence
    if st.session_state.evidence_result is not None:

        with st.expander(
            "📚 Supporting Evidence",
            expanded=False
        ):

            st.markdown(
                str(st.session_state.evidence_result)
            )

    # Final Analysis
    if st.session_state.final_analysis_result is not None:

        with st.expander(
            "🏆 Final Ranking",
            expanded=True
        ):

            st.markdown(
                str(st.session_state.final_analysis_result)
            )

