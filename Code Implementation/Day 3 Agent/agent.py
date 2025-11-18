import os
from typing import Any, Dict
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.models.google_llm import Gemini
from google.adk.tools.tool_context import ToolContext

# --- Configuration (from Section 1.5) ---
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# --- Session State Tools (from Section 5.1) ---
# These tools let the agent read and write to the session's memory.

def save_userinfo(
    tool_context: ToolContext, user_name: str, country: str
) -> Dict[str, Any]:
    """
    Tool to record and save user name and country in session state.
    Args:
        user_name: The username to store in session state
        country: The name of the user's country
    """
    # Write to session state using the 'user:' prefix for user data
    tool_context.state["user:name"] = user_name
    tool_context.state["user:country"] = country
    return {"status": "success"}

def retrieve_userinfo(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Tool to retrieve user name and country from session state.
    """
    # Read from session state
    user_name = tool_context.state.get("user:name", "Username not found")
    country = tool_context.state.get("user:country", "Country not found")
    return {"status": "success", "user_name": user_name, "country": country}


# --- Main Agent Definition (from Section 5.2) ---
# This agent is given the tools to manage session state.
root_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="text_chat_bot",
    description="""A text chatbot.
    Tools for managing user context:
    * To record username and country when provided use `save_userinfo` tool.
    * To fetch username and country when required use `retrieve_userinfo` tool.
    """,
    tools=[save_userinfo, retrieve_userinfo],
)

# --- App Definition (from Section 4.1) ---
# This is the main entry point for ADK.
# We wrap our agent in an "App" to add features like compaction.
root_app = App(
    name="day3_app",
    root_agent=root_agent,
    # This enables the context compaction from Section 4
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3,  # Summarize history after 3 turns
        overlap_size=1,         # Keep 1 turn of history for context
    ),
)