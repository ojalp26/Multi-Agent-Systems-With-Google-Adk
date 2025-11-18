from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from google.adk.models.google_llm import Gemini
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

retry_config = types.HttpRetryOptions(attempts=5, exp_base=7, initial_delay=1, http_status_codes=[429, 500, 503, 504])

# --- Connect to Remote Agent ---
# This creates a "proxy" that looks like a local agent but talks to port 8001
remote_product_catalog_agent = RemoteA2aAgent(
    name="product_catalog_agent",
    description="Remote product catalog agent from external vendor.",
    # We tell it exactly where to find the 'Agent Card' (the metadata)
    agent_card=f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}",
)

# --- Main Support Agent ---
root_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="customer_support_agent",
    description="A customer support assistant.",
    instruction="""You are a helpful customer support agent.
    When customers ask about products:
    1. Use the product_catalog_agent sub-agent to look up information.
    2. Answer questions about price and availability.
    """,
    # We add the remote agent just like a normal sub-agent!
    sub_agents=[remote_product_catalog_agent],
)