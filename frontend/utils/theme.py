"""
Theme configuration for the AI Startup Idea Validator.
Defines colors, fonts, and styling constants.
"""

# Color Palette
PRIMARY = "#0066ff"
PRIMARY_LIGHT = "#4d94ff"
PRIMARY_DARK = "#0044cc"
SECONDARY = "#00d4aa"
ACCENT = "#ff6b6b"
WARNING = "#ffd93d"
INFO = "#00b4d8"

# Gradients
GRADIENT_PRIMARY = "linear-gradient(135deg, #0066ff 0%, #00d4aa 100%)"
GRADIENT_DARK = "linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 100%)"
GRADIENT_CARD = "linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%)"
GRADIENT_BUTTON = "linear-gradient(135deg, #0066ff 0%, #00d4aa 100%)"
GRADIENT_HERO = "linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 50%, #0a0a1a 100%)"

# Glassmorphism
GLASS_BACKGROUND = "rgba(255, 255, 255, 0.05)"
GLASS_BORDER = "1px solid rgba(255, 255, 255, 0.1)"
GLASS_BLUR = "blur(20px)"
GLASS_SHADOW = "0 8px 32px rgba(0, 0, 0, 0.3)"

# Typography
FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_MONO = "'JetBrains Mono', 'Fira Code', monospace"

# Font Sizes
FONT_XS = "0.75rem"
FONT_SM = "0.875rem"
FONT_BASE = "1rem"
FONT_LG = "1.125rem"
FONT_XL = "1.25rem"
FONT_2XL = "1.5rem"
FONT_3XL = "2rem"
FONT_4XL = "2.5rem"
FONT_5XL = "3.5rem"

# Spacing
SPACING_XS = "0.25rem"
SPACING_SM = "0.5rem"
SPACING_MD = "1rem"
SPACING_LG = "1.5rem"
SPACING_XL = "2rem"
SPACING_2XL = "3rem"
SPACING_3XL = "4rem"

# Border Radius
RADIUS_SM = "8px"
RADIUS_MD = "12px"
RADIUS_LG = "16px"
RADIUS_XL = "24px"
RADIUS_FULL = "9999px"

# Shadows
SHADOW_SM = "0 2px 8px rgba(0, 0, 0, 0.2)"
SHADOW_MD = "0 4px 16px rgba(0, 0, 0, 0.3)"
SHADOW_LG = "0 8px 32px rgba(0, 0, 0, 0.4)"
SHADOW_GLOW = "0 0 20px rgba(0, 102, 255, 0.3)"

# Transitions
TRANSITION_FAST = "all 0.2s ease"
TRANSITION_NORMAL = "all 0.3s ease"
TRANSITION_SLOW = "all 0.5s ease"

# Breakpoints
BREAKPOINT_SM = "640px"
BREAKPOINT_MD = "768px"
BREAKPOINT_LG = "1024px"
BREAKPOINT_XL = "1280px"

# Page Configuration
PAGE_CONFIG = {
    "page_title": "AI Startup Idea Validator",
    "page_icon": "🚀",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# Sidebar Configuration
SIDEBAR_ITEMS = [
    {"label": "Home", "icon": "🏠", "page": "Home"},
    {"label": "Orchestrator", "icon": "🤖", "page": "Orchestrator"},
    {"label": "Web Search Agent", "icon": "🌐", "page": "Web_Search_Agent"},
    {"label": "Market Analysis", "icon": "📈", "page": "Market_Analysis"},
    {"label": "Competitor Analysis", "icon": "🏆", "page": "Competitor_Analysis"},
    {"label": "SWOT Analysis", "icon": "⚠", "page": "SWOT"},
    {"label": "MVP Recommendation", "icon": "💡", "page": "MVP"},
    {"label": "GTM Strategy", "icon": "📢", "page": "GTM"},
    {"label": "Final Report", "icon": "📄", "page": "Report"},
    {"label": "AI Advisor", "icon": "🤖", "page": "AI_Advisor"},
]

# Search Agent Stages
SEARCH_STAGES = [
    "Initializing AI Agents...",
    "Planning Search Strategy...",
    "Querying Google Search...",
    "Querying Tavily API...",
    "Querying Serper API...",
    "Collecting Industry Reports...",
    "Scanning Funding News...",
    "Identifying Competitors...",
    "Analyzing Customer Discussions...",
    "Deduplicating Sources...",
    "Ranking Source Quality...",
    "Generating Comprehensive Summary...",
]

# Confidence Score Descriptions
CONFIDENCE_LEVELS = {
    (90, 100): "Very High",
    (75, 89): "High",
    (60, 74): "Moderate",
    (40, 59): "Low",
    (0, 39): "Very Low",
}