"""
Frontend configuration for the AI Startup Validator.

The Streamlit frontend runs the EXISTING validation pipeline directly
in-process — there is no FastAPI backend URL to configure anymore.
"""

# The validation pipeline runs many multi-agent LLM calls and can take
# several minutes; no network configuration is required here.
APP_TITLE = "AI Startup Validator"
