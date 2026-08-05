"""GTM Strategy - Go-to-market strategy and launch plan."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="GTM Strategy", page_icon="📢", layout="wide", initial_sidebar_state="expanded")
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

render_breadcrumb("📢 GTM Strategy")
render_hero("📢", "GTM Strategy", "Go-to-market strategy and launch plan for your startup", "A Go-to-Market (GTM) strategy is a plan that outlines how a company will launch a product to market. It covers target audience, pricing, distribution channels, marketing tactics, and sales strategy. Our AI analyzes market data to recommend the optimal GTM approach.")

data = get_market_data()
gtm = data.get("gtm_strategy", {})
channels = gtm.get("channels", [])
pricing = gtm.get("pricing_tiers", [])
timeline = gtm.get("launch_timeline", {})

render_section("🔍 What is GTM Strategy?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Go-to-Market (GTM) Strategy</strong> is the comprehensive plan for launching a product to market. It defines who the target customers are, how to reach them, what pricing model to use, and how to position the product against competitors.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Focused Launch:</strong> Target the right customers with the right message.</p><p><strong>Efficient Spending:</strong> Allocate marketing budget effectively.</p><p><strong>Faster Adoption:</strong> Accelerate customer acquisition.</p><p><strong>Competitive Positioning:</strong> Differentiate from competitors.</p><p><strong>Revenue Goals:</strong> Clear path to revenue generation.</p></div>""", unsafe_allow_html=True)

render_section("📅 Launch Timeline")
phases = list(timeline.items())
phase_icons = ["🔧", "🚀", "📈", "🌱"]
phase_colors = ["#ffd93d", "#00d4aa", "#4d94ff", "#0066ff"]
cols = st.columns(len(phases))
for i, (phase, duration) in enumerate(phases):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;border-top:4px solid {phase_colors[i]};height:100%;"><div style="font-size:2rem;margin-bottom:0.25rem;">{phase_icons[i]}</div><div style="font-size:0.95rem;font-weight:600;text-transform:capitalize;">{phase.replace("_"," ").title()}</div><div style="font-size:0.85rem;color:{phase_colors[i]};font-weight:500;margin-top:0.25rem;">{duration}</div></div>', unsafe_allow_html=True)

render_section("💰 Pricing Strategy")
pricing_cols = st.columns(len(pricing))
tier_colors = ["#4d94ff", "#0066ff", "#00d4aa"]
tier_icons = ["🌱", "⭐", "👑"]
for i, tier in enumerate(pricing):
    with pricing_cols[i]:
        features_list = "".join(f'<div style="padding:0.3rem 0;font-size:0.8rem;color:rgba(255,255,255,0.6);display:flex;align-items:center;gap:0.5rem;"><span style="color:{tier_colors[i]};">✓</span> {f}</div>' for f in tier.get("features",[]))
        st.markdown(f'<div style="text-align:center;padding:1.5rem;background:rgba(255,255,255,0.03);border:1px solid {tier_colors[i]}44;border-radius:12px;height:100%;"><div style="font-size:2rem;margin-bottom:0.25rem;">{tier_icons[i]}</div><div style="font-size:1.1rem;font-weight:700;color:{tier_colors[i]};">{tier.get("tier","")}</div><div style="font-size:1.75rem;font-weight:800;margin:0.75rem 0;">{tier.get("price","")}</div><div style="text-align:left;padding-top:0.75rem;border-top:1px solid rgba(255,255,255,0.1);">{features_list}</div></div>', unsafe_allow_html=True)

render_section("📡 Marketing Channels")
channel_icons = ["🚀", "📰", "💼", "🎓", "💬"]
cols = st.columns(3)
for i, channel in enumerate(channels):
    with cols[i % 3]:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;"><div style="font-size:2rem;margin-bottom:0.25rem;">{channel_icons[i]}</div><div style="font-weight:600;font-size:0.9rem;">{channel}</div></div>', unsafe_allow_html=True)

render_section("📥 Input & Output")
col1, col2 = st.columns(2)
with col1:
    render_section("Input")
    render_table(["Source", "Data"], [("Market Analysis", "Target market segments"), ("Competitor Analysis", "Competitor pricing"), ("MVP", "Product features"), ("SWOT", "Strategic positioning")])
with col2:
    render_section("Output")
    render_table(["Output", "Description"], [("Pricing Tiers", "Recommended pricing"), ("Channels", "Marketing channels"), ("Timeline", "Launch phases"), ("Strategy", "GTM recommendations")])

render_tech_badges([("📊", "Market Analysis"), ("💰", "Pricing Models"), ("📈", "Growth Strategy"), ("🎯", "Target Marketing")])

render_section("🎯 Strategic Initiatives")
strategies = [("🌱", "Product-Led Growth", "Free tier drives adoption and word-of-mouth"), ("🤝", "Community Building", "Engage startup communities on Product Hunt, HN, Reddit"), ("📝", "Content Marketing", "Publish market research and validation case studies"), ("🤝", "Partnership Program", "Partner with accelerators, VCs, and incubators")]
cols = st.columns(2)
for i, (icon, title, desc) in enumerate(strategies):
    with cols[i % 2]:
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.25rem;"><span style="font-size:1.5rem;">{icon}</span><span style="font-weight:600;font-size:0.9rem;">{title}</span></div><div style="font-size:0.85rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

render_faqs([("What is a GTM strategy?", "A Go-to-Market strategy is a comprehensive plan for launching a product, covering target audience, pricing, channels, and marketing tactics."), ("How is pricing determined?", "Pricing is based on competitor analysis, market willingness to pay, and value-based pricing principles."), ("What marketing channels work best?", "For B2B SaaS, Product Hunt, LinkedIn, content marketing, and community building are most effective."), ("How long does a launch take?", "A typical launch cycle is 14 weeks: 4 weeks pre-launch, 2 weeks launch, 8 weeks post-launch."), ("Can I change pricing later?", "Yes, pricing can be adjusted based on market feedback and adoption rates."), ("What if the launch fails?", "GTM strategy includes contingency plans. Pivot based on what you learn from the market.")])
render_summary("📋 Summary", "The recommended GTM strategy uses a tiered pricing model ($49-$149/month) with a 14-week launch timeline. Key channels include Product Hunt, TechCrunch, LinkedIn, and startup communities. Focus on product-led growth with a free tier to drive adoption.")
render_page_footer()