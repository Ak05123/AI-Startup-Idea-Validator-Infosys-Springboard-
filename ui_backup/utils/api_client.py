"""
API Client for connecting to the backend orchestrator.
Handles all communication with app/orchestrator.py.
No business logic - just API calls and response handling.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st

# Add project root to path for backend imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def get_orchestrator() -> Optional[Any]:
    """
    Dynamically import and return the orchestrator module.
    Returns None if backend is unavailable.
    """
    try:
        from app.orchestrator import StartupOrchestrator
        return StartupOrchestrator
    except ImportError:
        try:
            from app.main import run_pipeline
            return run_pipeline
        except ImportError:
            return None


def run_validation_pipeline(form_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run the full validation pipeline via the backend orchestrator.

    Args:
        form_data: Dictionary containing startup form data

    Returns:
        Dictionary with pipeline results or error information
    """
    orchestrator = get_orchestrator()

    if orchestrator is None:
        return {
            "status": "error",
            "error": "Backend orchestrator not available. Please ensure app/orchestrator.py exists.",
            "data": None,
        }

    try:
        # If orchestrator is a class, instantiate and run
        if isinstance(orchestrator, type):
            instance = orchestrator()
            result = instance.run(form_data)
        else:
            # If it's a function
            result = orchestrator(form_data)

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


def run_single_agent(agent_name: str, form_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run a single agent from the backend.

    Args:
        agent_name: Name of the agent to run
        form_data: Startup form data

    Returns:
        Agent results
    """
    orchestrator = get_orchestrator()

    if orchestrator is None:
        return {"status": "error", "error": "Backend not available", "data": None}

    try:
        if isinstance(orchestrator, type):
            instance = orchestrator()
            agent_method = getattr(instance, f"run_{agent_name}", None)
            if agent_method:
                result = agent_method(form_data)
            else:
                result = instance.run_agent(agent_name, form_data)
        else:
            result = {"message": f"Agent {agent_name} not available via function interface"}

        return {"status": "success", "error": None, "data": result}
    except Exception as e:
        return {"status": "error", "error": str(e), "data": None}


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


def check_backend_health() -> Tuple[bool, str]:
    """
    Check if the backend is available and responsive.

    Returns:
        Tuple of (is_healthy, message)
    """
    orchestrator = get_orchestrator()
    if orchestrator is None:
        return False, "Backend orchestrator not found"
    return True, "Backend is available"