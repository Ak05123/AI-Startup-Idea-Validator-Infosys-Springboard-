"""
Global CSS styles for the AI Startup Validator frontend.

Premium dark AI/SaaS aesthetic with a focused, centered layout.
No navigation chrome — the app controls progression via session state.
"""

import streamlit as st


def inject_css() -> None:
    """Inject global custom CSS for a premium, focused look."""
    st.markdown(
        """
        <style>
        /* ============================================================
           GLOBAL
           ============================================================ */
        .stApp {
            background: radial-gradient(
                1100px 650px at 50% -10%,
                #1e1b4b 0%,
                #0f172a 48%,
                #0b1120 100%
            );
            color: #e2e8f0;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont,
                         'Segoe UI', Roboto, sans-serif;
        }

        /* Hide default Streamlit chrome for a focused product feel */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header[data-testid="stHeader"] {
            background: transparent;
            height: 0;
        }

        /* Focused content container — centered, not full-width */
        .block-container {
            max-width: 940px;
            margin: 0 auto;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* ============================================================
           TYPOGRAPHY
           ============================================================ */
        h1, h2, h3 {
            color: #f8fafc !important;
            letter-spacing: -0.02em;
        }

        .page-heading {
            font-size: 2rem;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }

        .page-subtitle {
            color: #94a3b8;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 8px;
        }

        .section-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #f8fafc;
            margin: 18px 0 12px;
        }

        /* ============================================================
           HOME / LANDING
           ============================================================ */
        .home-shell {
            padding-top: 8vh;
            text-align: center;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            color: #a5b4fc;
            border: 1px solid rgba(99, 102, 241, 0.4);
            border-radius: 999px;
            padding: 7px 20px;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 24px;
        }

        .hero-title {
            font-size: 2.9rem;
            font-weight: 800;
            line-height: 1.12;
            margin-bottom: 18px;
            background: linear-gradient(135deg, #f8fafc 0%, #c7d2fe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            color: #94a3b8;
            max-width: 580px;
            margin: 0 auto;
            line-height: 1.7;
        }

        /* Idea / validation form */
        [data-testid="stForm"] {
            background: rgba(30, 41, 59, 0.55);
            border: 1px solid rgba(148, 163, 184, 0.16);
            border-radius: 20px;
            padding: 30px 34px;
            margin-top: 30px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(2, 6, 23, 0.5);
        }

        /* ============================================================
           IDEA CARD
           ============================================================ */
        .idea-card {
            background: rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.22);
            border-radius: 16px;
            padding: 18px 22px;
            margin: 22px 0;
        }

        .idea-label {
            font-size: 0.7rem;
            color: #a5b4fc;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600;
            margin-bottom: 6px;
        }

        .idea-text {
            color: #e2e8f0;
            font-size: 1rem;
            line-height: 1.5;
        }

        /* ============================================================
           AGENT CARDS
           ============================================================ */
        .agent-card {
            display: flex;
            align-items: center;
            gap: 16px;
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 16px;
            padding: 18px 22px;
            margin-bottom: 12px;
        }

        .agent-icon {
            font-size: 1.35rem;
            width: 46px;
            height: 46px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 12px;
            flex-shrink: 0;
        }

        .agent-info { flex: 1; min-width: 0; }
        .agent-name { font-weight: 700; color: #f8fafc; font-size: 0.98rem; }
        .agent-desc { color: #94a3b8; font-size: 0.83rem; margin-top: 2px; }
        .agent-status { flex-shrink: 0; }

        /* ============================================================
           STATUS PILLS
           ============================================================ */
        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border-radius: 999px;
            padding: 5px 14px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.02em;
            white-space: nowrap;
        }

        .status-running {
            background: rgba(59, 130, 246, 0.15);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.4);
        }

        .status-completed {
            background: rgba(34, 197, 94, 0.15);
            color: #4ade80;
            border: 1px solid rgba(34, 197, 94, 0.4);
        }

        .status-failed {
            background: rgba(239, 68, 68, 0.15);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.4);
        }

        .status-waiting {
            background: rgba(148, 163, 184, 0.15);
            color: #94a3b8;
            border: 1px solid rgba(148, 163, 184, 0.4);
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: currentColor;
            animation: pulse-dot 1.2s ease-in-out infinite;
        }

        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.35; transform: scale(0.8); }
        }

        /* ============================================================
           CARDS
           ============================================================ */
        .card {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 16px;
            padding: 20px 24px;
            margin-bottom: 16px;
        }

        .card-title {
            font-size: 1.02rem;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 8px;
        }

        .card-body {
            color: #cbd5e1;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        /* ============================================================
           METRIC / SCORE CARDS
           ============================================================ */
        .metric-card {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 16px;
            padding: 20px 22px;
            text-align: center;
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #818cf8 0%, #a78bfa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .metric-label {
            font-size: 0.76rem;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 4px;
        }

        /* ============================================================
           ACTION CARDS (Results page)
           ============================================================ */
        .action-card {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 16px;
            padding: 20px 22px;
            text-align: center;
            transition: all 0.2s ease;
            cursor: pointer;
        }

        .action-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
        }

        .action-card-icon {
            font-size: 1.6rem;
            margin-bottom: 8px;
        }

        .action-card-title {
            font-size: 0.95rem;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 4px;
        }

        .action-card-desc {
            font-size: 0.78rem;
            color: #94a3b8;
            line-height: 1.5;
        }

        /* ============================================================
           BUTTONS
           ============================================================ */
        .stButton > button,
        [data-testid="stFormSubmitButton"] > button {
            background: rgba(30, 41, 59, 0.8);
            color: #cbd5e1;
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.2s ease;
        }

        .stButton > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
            background: rgba(51, 65, 85, 0.8);
            color: #f8fafc;
        }

        .stButton > button[kind="primary"],
        [data-testid="stFormSubmitButton"] > button[kind="primary"] {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            border: none;
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.35);
        }

        .stButton > button[kind="primary"]:hover,
        [data-testid="stFormSubmitButton"] > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.5);
        }

        .stButton > button:disabled,
        [data-testid="stFormSubmitButton"] > button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        [data-testid="stDownloadButton"] > button {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.35);
        }

        /* ============================================================
           INPUTS
           ============================================================ */
        .stTextInput input,
        .stNumberInput input,
        .stSelectbox select,
        .stTextArea textarea {
            background: rgba(15, 23, 42, 0.8) !important;
            color: #e2e8f0 !important;
            border: 1px solid rgba(148, 163, 184, 0.25) !important;
            border-radius: 10px !important;
        }

        .stTextInput input:focus,
        .stNumberInput input:focus,
        .stSelectbox select:focus,
        .stTextArea textarea:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
        }

        label {
            color: #cbd5e1 !important;
            font-weight: 500 !important;
        }

        /* ============================================================
           EXPANDERS
           ============================================================ */
        [data-testid="stExpander"] {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 14px;
            margin-bottom: 12px;
        }

        .streamlit-expanderHeader,
        [data-testid="stExpander"] summary {
            color: #e2e8f0 !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }

        /* ============================================================
           DIVIDERS / FOOTER / ALERTS
           ============================================================ */
        hr {
            border-color: rgba(148, 163, 184, 0.15) !important;
        }

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 0.78rem;
            margin-top: 48px;
        }

        .stAlert {
            border-radius: 12px;
        }

        /* ============================================================
           RESPONSIVE
           ============================================================ */
        @media (max-width: 768px) {
            .hero-title { font-size: 1.9rem; }
            .hero-subtitle { font-size: 0.95rem; }
            .metric-value { font-size: 1.5rem; }
            .page-heading { font-size: 1.5rem; }
            [data-testid="stForm"] { padding: 22px 18px; }
            .home-shell { padding-top: 4vh; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )