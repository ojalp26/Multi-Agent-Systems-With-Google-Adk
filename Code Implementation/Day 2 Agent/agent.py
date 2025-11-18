from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import AgentTool
from google.adk.code_executors import BuiltInCodeExecutor

# --- Configuration (from cell 1.5) ---
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# --- Tool 1: Fee Lookup (from cell 2.2) ---
def get_fee_for_payment_method(method: str) -> dict:
    """Looks up the transaction fee percentage for a given payment method.
    This tool simulates looking up a company's internal fee structure based on
    the name of the payment method provided by the user.
    Args:
        method: The name of the payment method. It should be descriptive,
                e.g., "platinum credit card" or "bank transfer".
    Returns:
        Dictionary with status and fee information.
        Success: {"status": "success", "fee_percentage": 0.02}
        Error: {"status": "error", "error_message": "Payment method not found"}
    """
    fee_database = {
        "platinum credit card": 0.02,  # 2%
        "gold debit card": 0.035,  # 3.5%
        "bank transfer": 0.01,  # 1%
    }
    fee = fee_database.get(method.lower())
    if fee is not None:
        return {"status": "success", "fee_percentage": fee}
    else:
        return {
            "status": "error",
            "error_message": f"Payment method '{method}' not found",
        }

# --- Tool 2: Exchange Rate (from cell 2.2) ---
def get_exchange_rate(base_currency: str, target_currency: str) -> dict:
    """Looks up and returns the exchange rate between two currencies.
    Args:
        base_currency: The ISO 4217 currency code of the currency you
                       are converting from (e.g., "USD").
        target_currency: The ISO 4217 currency code of the currency you
                         are converting to (e.g., "EUR").
    Returns:
        Dictionary with status and rate information.
        Success: {"status": "success", "rate": 0.93}
        Error: {"status": "error", "error_message": "Unsupported currency pair"}
    """
    rate_database = {
        "usd": {
            "eur": 0.93,  # Euro
            "jpy": 157.50,  # Japanese Yen
            "inr": 83.58,  # Indian Rupee
        }
    }
    base = base_currency.lower()
    target = target_currency.lower()
    rate = rate_database.get(base, {}).get(target)
    if rate is not None:
        return {"status": "success", "rate": rate}
    else:
        return {
            "status": "error",
            "error_message": f"Unsupported currency pair: {base_currency}/{target_currency}",
        }

# --- Agent Tool: Calculator (from cell 3.1) ---
calculation_agent = LlmAgent(
    name="CalculationAgent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction="""You are a specialized calculator that ONLY responds with Python code. You are forbidden from providing any text, explanations, or conversational responses.
      Your task is to take a request for a calculation and translate it into a single block of Python code that calculates the answer.
        **RULES:**
    1.  Your output MUST be ONLY a Python code block.
    2.  Do NOT write any text before or after the code block.
    3.  The Python code MUST calculate the result.
    4.  The Python code MUST print the final result to stdout.
    5.  You are PROHIBITED from performing the calculation yourself. Your only job is to generate the code that will perform the calculation.
       Failure to follow these rules will result in an error.
       """,
    code_executor=BuiltInCodeExecutor(),
)

# --- Main Agent Definition ---
root_agent = LlmAgent(
    name="enhanced_currency_agent",
    # USE LITE (Because it supports Code Execution)
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction="""You are a smart currency conversion assistant. 
    
    **CRITICAL RULES:**
    1. AUTOMATICALLY use tools. Do NOT ask the user which tool to use.
    2. If you see a payment method (like 'Bank Transfer'), immediately use `get_fee_for_payment_method`.
    3. If you see currencies (like USD to INR), immediately use `get_exchange_rate`.
    4. Do NOT explain the process. Just RUN THE TOOLS.
    
    **Workflow:**
    1. Call `get_fee_for_payment_method` to get the fee % (e.g. 0.01).
    2. Call `get_exchange_rate` to get the rate (e.g. 83.58).
    3. Call the `CalculationAgent` tool to do the math.
    4. Output the final result.
    """,
    tools=[
        get_fee_for_payment_method,
        get_exchange_rate,
        AgentTool(agent=calculation_agent),
    ],
)

#to run in terminal enter this in terminal : adk run day2_agent
#to run on web enter this in terminal :adk web --port 8000