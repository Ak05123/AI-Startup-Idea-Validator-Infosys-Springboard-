"""Market Intelligence - Collect and analyze external business information."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Market Intelligence", page_icon="📊", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_hero, render_section, render_card, render_workflow, render_tech_badges, render_table, render_advantages, render_challenges, render_faqs, render_summary, render_page_footer
from components.charts import create_market_size_chart, create_growth_chart, create_revenue_projection_chart
from utils.helpers import get_market_data

render_breadcrumb("📊 Market Intelligence")
render_hero("📊", "Market Intelligence", "Collect and analyze external business information to understand market conditions", "Market Intelligence involves gathering real-time data about your industry, competitors, customers, and market trends. Our AI-powered system continuously monitors multiple sources to provide actionable insights for strategic decision-making.")

data = get_market_data()
trends = data.get("industry_trends", {})
overview = data.get("market_overview", {})

render_section("🔍 What is Market Intelligence?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Market Intelligence</strong> is the process of gathering and analyzing external data about your market environment. It covers industry trends, customer behavior, competitive movements, technological innovations, and regulatory changes. AI-powered market intelligence automates data collection and provides real-time insights.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Informed Decisions:</strong> Make data-driven strategic decisions with real-time market insights.</p><p><strong>Competitive Edge:</strong> Stay ahead of competitors by identifying trends early.</p><p><strong>Growth Opportunities:</strong> Discover untapped market segments and revenue opportunities.</p><p><strong>Risk Mitigation:</strong> Identify market threats before they impact your business.</p><p><strong>Customer Understanding:</strong> Deep insights into customer needs and behavior.</p></div>""", unsafe_allow_html=True)

render_section("⚡ How It Works")
render_workflow([("🔍", "Data Collection", "Gather from 10+ sources"), ("🤖", "AI Analysis", "Process and analyze"), ("📊", "Trend Detection", "Identify patterns"), ("📈", "Insights Generation", "Actionable insights")])

render_section("📈 Market Trends")
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(create_market_size_chart(trends.get("years",[]), trends.get("market_sizes",[]), "Market Size ($B)"), use_container_width=True)
with col2:
    st.plotly_chart(create_growth_chart(trends.get("years",[]), trends.get("ai_adoption_rate",[]), "AI Adoption Rate (%)"), use_container_width=True)

render_section("🔮 Key Trends & Opportunities")
cols = st.columns(3)
for i, trend in enumerate(overview.get("key_trends",[])):
    with cols[i % 3]:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;"><div style="font-size:1.5rem;margin-bottom:0.25rem;">📈</div><div style="font-weight:600;font-size:0.85rem;">{trend}</div></div>', unsafe_allow_html=True)

render_section("👥 Customer Needs & Emerging Technologies")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;height:100%;"><div style="font-weight:600;margin-bottom:0.75rem;">👥 Customer Needs</div><ul style="list-style:none;padding:0;"><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Real-time market validation</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Automated competitor tracking</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Data-driven decision support</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Affordable intelligence tools</li><li style="padding:0.4rem 0;">▸ Easy-to-understand reports</li></ul></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;height:100%;"><div style="font-weight:600;margin-bottom:0.75rem;">⚡ Emerging Technologies</div><ul style="list-style:none;padding:0;"><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Multi-agent AI architectures</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Real-time data pipelines</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ NLP-powered analysis</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">▸ Predictive market modeling</li><li style="padding:0.4rem 0;">▸ Automated report generation</li></ul></div>""", unsafe_allow_html=True)

render_section("💰 Demand Forecast")
st.plotly_chart(create_revenue_projection_chart(data.get("revenue_projection",{})), use_container_width=True)

render_section("💡 Recent Innovations")
cols = st.columns(4)
innovations = [("🤖", "AI Sentiment Analysis", "Real-time customer sentiment"), ("📡", "Auto Data Collection", "100+ source monitoring"), ("🧠", "Predictive Analytics", "87% accuracy predictions"), ("🔗", "Multi-Source Integration", "Structured + unstructured data")]
for i, (icon, title, desc) in enumerate(innovations):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;height:100%;"><div style="font-size:1.5rem;margin-bottom:0.25rem;">{icon}</div><div style="font-weight:600;font-size:0.8rem;margin-bottom:0.25rem;">{title}</div><div style="font-size:0.7rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

render_section("📥 Input & Output")
col1, col2 = st.columns(2)
with col1:
    render_section("Input")
    render_table(["Source", "Data Type"], [("Web Search", "Articles, news"), ("Social Media", "Customer sentiment"), ("Industry Reports", "Market research"), ("Company Data", "Financial information")])
with col2:
    render_section("Output")
    render_table(["Output", "Description"], [("Trends", "Market trends and patterns"), ("Opportunities", "Growth opportunities"), ("Risks", "Market threats"), ("Insights", "Actionable intelligence")])

render_tech_badges([("🤖", "NLP"), ("📊", "Data Analytics"), ("📡", "Web Scraping"), ("🧠", "ML Models"), ("📈", "Visualization")])

render_section("✅ Advantages")
render_advantages([("⚡", "Real-Time", "Continuous market monitoring"), ("🎯", "Comprehensive", "10+ data sources"), ("📊", "Visual", "Interactive dashboards"), ("🔄", "Automated", "No manual research needed"), ("📈", "Predictive", "AI-powered forecasts"), ("💰", "Cost-Effective", "Saves research costs")])

render_section("⚠️ Challenges")
render_challenges([("📊", "Data Overload", "Filtering signal from noise"), ("🌐", "Source Reliability", "Varying data quality"), ("🎯", "Relevance", "Finding truly relevant data"), ("🔄", "Timeliness", "Keeping data current")])

render_faqs([("What is market intelligence?", "Market intelligence is the process of gathering and analyzing external data about your market, competitors, and customers to make better business decisions."), ("How does AI improve market intelligence?", "AI automates data collection from multiple sources, identifies patterns humans might miss, and provides real-time insights at scale."), ("What sources does the system use?", "The system aggregates data from DuckDuckGo, Google News, Crunchbase, Statista, Reddit, LinkedIn, GitHub, Medium, and more."), ("How often is data updated?", "Market intelligence data is updated in real-time during active searches. The system can be configured for periodic auto-refresh."), ("Can I export intelligence data?", "Yes! Data can be exported in CSV, JSON, and Markdown formats."), ("How accurate are the insights?", "Insights are based on multi-source data with confidence scores typically above 85%.")])
render_summary("📋 Summary", "Market Intelligence provides real-time, AI-powered insights about your market environment. By monitoring 10+ sources continuously, it identifies trends, opportunities, and threats, enabling data-driven strategic decisions.")
render_page_footer()