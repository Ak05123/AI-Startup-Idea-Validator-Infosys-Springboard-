"""
Backend Client for the AI Startup Idea Validator.
Connects the Streamlit frontend to the existing backend pipeline.
No business logic - only API calls and response handling.
"""

import importlib.util
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st
from dotenv import load_dotenv

# Add backend folder to Python path for imports
# This ensures the backend's agents/ and app/ packages are importable
BACKEND_ROOT = Path(__file__).resolve().parent.parent.parent / "backend"
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))
else:
    # Ensure backend path is first
    sys.path.remove(str(BACKEND_ROOT))
    sys.path.insert(0, str(BACKEND_ROOT))

# Load .env file from the project root if present
load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")
load_dotenv(BACKEND_ROOT / ".env")

# Remove the frontend root from sys.path to prevent app.py from
# shadowing the backend's app/ package
# Handle both relative and absolute path formats
FRONTEND_ROOT = Path(__file__).resolve().parent.parent
for path in list(sys.path):
    if path and Path(path).resolve() == FRONTEND_ROOT.resolve():
        sys.path.remove(path)


def get_pipeline() -> Optional[Any]:
    """
    Dynamically import and return the backend pipeline class.
    Returns None if backend is unavailable.

    Ensures the backend path is first in sys.path and the frontend
    root is removed, so that `from app.pipeline import ...` resolves
    to the backend's app namespace package, not the frontend's app.py.
    """
    try:
        # Ensure backend path is first in sys.path
        if str(BACKEND_ROOT) in sys.path:
            sys.path.remove(str(BACKEND_ROOT))
        sys.path.insert(0, str(BACKEND_ROOT))

        # Remove the frontend root from sys.path to prevent app.py
        # from shadowing the backend's app/ namespace package
        for path in list(sys.path):
            if path and Path(path).resolve() == FRONTEND_ROOT.resolve():
                sys.path.remove(path)

        # Remove any cached 'app' module that might be the frontend's app.py
        for module_name in list(sys.modules.keys()):
            if module_name == "app" or module_name.startswith("app."):
                del sys.modules[module_name]

        # Import the backend pipeline using regular imports
        # The backend's app/ and agents/ are namespace packages
        import importlib
        pipeline_module = importlib.import_module("app.pipeline")

        return pipeline_module.StartupValidationPipeline
    except (ImportError, AttributeError, ValueError) as e:
        print(f"[backend_client] Failed to load pipeline: {e}")
        return None


def check_backend_health() -> Tuple[bool, str]:
    """
    Check if the backend is available and responsive.

    Returns:
        Tuple of (is_healthy, message)
    """
    pipeline = get_pipeline()
    if pipeline is None:
        return False, "Backend service is currently unavailable."
    return True, "Backend is available"


def run_validation_pipeline(startup_idea: str) -> Dict[str, Any]:
    """
    Run the full validation pipeline via the backend orchestrator.

    Args:
        startup_idea: The startup idea text

    Returns:
        Dictionary with pipeline results or error information
    """
    pipeline_class = get_pipeline()

    if pipeline_class is None:
        return {
            "status": "error",
            "error": "Backend service is currently unavailable.",
            "data": None,
        }

    try:
        pipeline = pipeline_class()
        result = pipeline.run(startup_idea)

        return {
            "status": "success",
            "error": None,
            "data": result,
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "data": None,
        }


def ask_advisor(question: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Send a question to the Conversational Advisor agent.

    Args:
        question: User's question
        context: Current startup context from session state

    Returns:
        Advisor response
    """
    try:
        from agents.conversational_advisor import ConversationalAdvisor
        advisor = ConversationalAdvisor()
        response = advisor.answer(question, context)
        return {"status": "success", "response": response}
    except ImportError:
        return {
            "status": "error",
            "response": "AI Advisor is not available. Please ensure agents/conversational_advisor.py exists.",
        }
    except Exception as e:
        return {"status": "error", "response": f"Error: {str(e)}"}


def parse_json_response(raw: Any) -> Dict[str, Any]:
    """
    Parse a JSON string response from a backend agent.
    Handles both string and dict/list inputs.

    Args:
        raw: Raw response from backend agent

    Returns:
        Parsed dictionary
    """
    if raw is None:
        return {}

    if isinstance(raw, dict):
        return raw

    if isinstance(raw, list):
        return {"items": raw}

    if isinstance(raw, str):
        cleaned = raw.strip()
        # Remove markdown code fences if present
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[-1]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return {"raw": raw}

    return {"raw": str(raw)}


def parse_list_response(raw: Any) -> List[str]:
    """
    Parse a list response from a backend agent.
    Handles both string and list inputs.

    Args:
        raw: Raw response from backend agent

    Returns:
        List of strings
    """
    if raw is None:
        return []

    if isinstance(raw, list):
        return [str(item) for item in raw]

    if isinstance(raw, str):
        cleaned = raw.strip()
        # Remove markdown code fences if present
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[-1]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()

        try:
            parsed = json.loads(cleaned)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            pass

        # Try Python-style list parsing
        if cleaned.startswith("[") and cleaned.endswith("]"):
            inner = cleaned[1:-1]
            items = [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
            return items

        return [cleaned]

    return [str(raw)]