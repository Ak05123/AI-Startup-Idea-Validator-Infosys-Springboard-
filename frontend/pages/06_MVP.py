"""MVP Recommendation - Minimum Viable Product strategy and roadmap."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="MVP Recommendation", page_icon="💡", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_hero, render_section, render_card, render_workflow, render_tech_badges, render_table, render_advantages, render_challenges, render_faqs, render_summary, render_page_footer
from utils.helpers import get_market_data

render_breadcrumb("💡 MVP Recommendation")
render_hero("💡", "MVP Recommendation", "Minimum Viable Product strategy and development roadmap", "MVP (Minimum Viable Product) is the version of your product with just enough features to be usable by early customers. Our AI analyzes market needs, competitor features, and technical feasibility to recommend the optimal MVP feature set.")

data = get_market_data()
mvp = data.get("mvp_recommendations", {})
features = mvp.get("core_features", [])
timeline = mvp.get("development_timeline", {})
costs = mvp.get("estimated_cost", {})

render_section("🔍 What is an MVP?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Minimum Viable Product (MVP)</strong> is the most pared-down version of a product that can still be released. An MVP has just enough features to satisfy early customers and provide feedback for future development. The goal is to maximize learning about customers with the least effort.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Faster Time to Market:</strong> Launch quickly and start learning from real users.</p><p><strong>Lower Initial Investment:</strong> Build only essential features first.</p><p><strong>Validate Assumptions:</strong> Test your hypotheses with minimal risk.</p><p><strong>Iterate Based on Feedback:</strong> Use real user feedback to guide development.</p><p><strong>Attract Early Adopters:</strong> Get your product in users' hands sooner.</p></div>""", unsafe_allow_html=True)

render_section("💰 Cost Overview")
cols = st.columns(4)
cost_items = [("Development", costs.get("development","N/A"), "#4d94ff"), ("Infrastructure", costs.get("infrastructure","N/A"), "#00d4aa"), ("API Costs", costs.get("api_costs","N/A"), "#ffd93d"), ("Team Size", costs.get("team_size","N/A"), "#ff6b6b")]
for i, (label, value, color) in enumerate(cost_items):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{label}</div><div style="font-size:1.3rem;font-weight:700;color:{color};margin-top:0.25rem;">{value}</div></div>', unsafe_allow_html=True)

render_section("🎯 Core Features", "Prioritized feature set")
priority_colors = {"P0": "#ff6b6b", "P1": "#ffd93d", "P2": "#4d94ff"}
for feat in features:
    p = feat.get("priority","P2")
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;border-left:4px solid {priority_colors.get(p,"#4d94ff")};"><div style="display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.95rem;">{feat.get("feature","")}</div><div style="display:flex;gap:1rem;margin-top:0.25rem;"><span style="font-size:0.8rem;color:{priority_colors.get(p,"#4d94ff")};font-weight:500;">{p} Priority</span><span style="font-size:0.8rem;color:rgba(255,255,255,0.5);">📊 {feat.get("complexity","")} Complexity</span></div></div><div style="text-align:right;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Impact</div><div style="font-size:1rem;">{"⭐"*feat.get("impact",0)}</div></div></div></div>', unsafe_allow_html=True)

render_section("📅 Development Timeline")
phases = list(timeline.items())
phase_colors = ["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d"]
cols = st.columns(len(phases))
for i, (phase, desc) in enumerate(phases):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;border-top:4px solid {phase_colors[i]};height:100%;"><div style="font-size:1.2rem;font-weight:700;color:{phase_colors[i]};margin-bottom:0.5rem;">Phase {i+1}</div><div style="font-size:0.85rem;color:rgba(255,255,255,0.6);line-height:1.5;">{desc}</div></div>', unsafe_allow_html=True)

render_section("📥 Input & Output")
col1, col2 = st.columns(2)
with col1:
    render_section("Input")
    render_table(["Source", "Data"], [("Market Analysis", "Market needs and gaps"), ("Competitor Analysis", "Competitor features"), ("SWOT", "Strategic priorities"), ("User Research", "Customer requirements")])
with col2:
    render_section("Output")
    render_table(["Output", "Description"], [("Feature List", "Prioritized features"), ("Timeline", "Development phases"), ("Cost Estimate", "Budget requirements"), ("Team Plan", "Resource allocation")])

render_tech_badges([("💡", "Product Strategy"), ("📊", "Cost Analysis"), ("📅", "Project Planning"), ("🎯", "Priority Matrix")])

render_section("✅ Advantages")
render_advantages([("⚡", "Fast Launch", "Get to market in 6-8 weeks"), ("💰", "Cost Effective", "Minimal initial investment"), ("📊", "Data-Driven", "Based on market research"), ("🔄", "Iterative", "Improve based on feedback"), ("🎯", "Focused", "Build only what matters"), ("📈", "Scalable", "Add features later")])

render_section("⚠️ Challenges")
render_challenges([("🎯", "Scope Creep", "Resist adding extra features"), ("📊", "Feature Selection", "Choosing the right features"), ("⏱️", "Time Pressure", "Balancing speed and quality"), ("📈", "User Adoption", "Getting early users")])

render_section("🏗️ Real-World Example")
st.markdown("""<div style="background:rgba(0,102,255,0.05);border:1px solid rgba(0,102,255,0.15);border-radius:12px;padding:1.5rem;margin:1rem 0;"><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>Startup:</strong> TaskFlow - AI project management tool</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>MVP Features (P0):</strong> AI task prioritization, smart scheduling, team collaboration</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>Phase 1 (6 weeks):</strong> Core AI engine + basic task management</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>Phase 2 (4 weeks):</strong> Team features + integrations</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>Result:</strong> Launched with 3 core features, gained 500 beta users in first month</p></div>""", unsafe_allow_html=True)

render_section("🔗 AI Pipeline")
st.markdown('<div style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">MVP Agent receives data from <strong>Market Analysis</strong>, <strong>Competitor Analysis</strong>, and <strong>SWOT</strong> agents. Output goes to <strong>GTM Strategy</strong> and <strong>Report Generator</strong>.</div>', unsafe_allow_html=True)

render_section("🔮 Future Improvements")
cols = st.columns(3)
for i, (icon, title, desc) in enumerate([("🤖", "AI Feature Suggestion", "AI suggests features based on market gaps"), ("📊", "Cost Optimization", "Optimize development costs"), ("📈", "Success Prediction", "Predict MVP success probability"), ("🔄", "Iteration Planning", "Plan post-MVP iterations"), ("👥", "User Testing", "Integrate user testing tools"), ("📡", "Analytics Integration", "Built-in usage analytics")]):
    with cols[i % 3]:
        st.markdown(f'<div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.12);border-radius:12px;padding:1.25rem;text-align:center;height:100%;"><div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div><div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;">{title}</div><div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

render_faqs([("What is an MVP?", "An MVP is the simplest version of your product that delivers value to early customers and provides learning for future development."), ("How are features prioritized?", "Features are ranked by impact vs. effort. P0 = must-have, P1 = important, P2 = nice-to-have."), ("How long does MVP development take?", "Typical MVP development takes 6-16 weeks depending on complexity and team size."), ("How much does an MVP cost?", "MVP development typically costs $150K-$200K for a 5-7 person team over 3-4 months."), ("Can I change features later?", "Yes! The MVP is designed to be iterated based on user feedback."), ("What if my MVP fails?", "Failure is learning. MVP approach minimizes investment, so you can pivot quickly.")])
render_summary("📋 Summary", f"The recommended MVP includes {len(features)} core features across {len(phases)} development phases. Total estimated cost: {costs.get('development','N/A')} with a team of {costs.get('team_size','N/A')}. Focus on P0 features first: AI-powered search agent and market analysis dashboard.")
render_page_footer()