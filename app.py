import streamlit as st

from chain import analyze_incident

st.set_page_config(
    page_title="Incident Intelligence AI",
    page_icon="🚨",
    layout="wide"
)

st.markdown(
"""
<style>

.stApp {
    background:
    radial-gradient(circle at top left,#1e3a8a,transparent 40%),
    radial-gradient(circle at bottom right,#7c3aed,transparent 40%),
    #020617;
    color:white;
}

.block-container {
    padding-top:2rem;
    padding-left:4rem;
    padding-right:4rem;
}

.hero {
    background:
    linear-gradient(135deg,
    rgba(59,130,246,0.25),
    rgba(139,92,246,0.25));

    padding:35px;
    border-radius:25px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.15);
    backdrop-filter:blur(15px);
}

.hero h1 {
    font-size:48px;
    font-weight:900;
    background:
    linear-gradient(90deg,#38bdf8,#c084fc);
    -webkit-background-clip:text;
    color:transparent;
}

.hero p {
    color:#cbd5e1;
    font-size:18px;
}

.card {
    background:rgba(255,255,255,0.08);
    border-radius:25px;
    padding:30px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0px 20px 40px rgba(0,0,0,0.35);
}

.summary-box {
    background:rgba(15,23,42,0.8);
    padding:25px;
    border-radius:20px;
    font-size:18px;
    line-height:1.7;
    border-left:5px solid #38bdf8;
}

.priority-box {
    text-align:center;
    font-size:38px;
    font-weight:900;
    padding:20px;
    border-radius:20px;
    background:linear-gradient(135deg,#ef4444,#f97316);
}

.tag {
    display:inline-block;
    padding:10px 18px;
    margin:5px;
    border-radius:50px;
    background:rgba(56,189,248,0.2);
    color:#7dd3fc;
    font-weight:700;
}

.stButton button {
    width:100%;
    height:55px;
    border-radius:15px;
    font-size:18px;
    font-weight:700;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    border:none;
}

.stButton button:hover {
    transform:scale(1.02);
}

textarea {
    background:rgba(15,23,42,0.8) !important;
    color:white !important;
    border-radius:20px !important;
}

</style>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="hero">
<h1>🚨 Incident Intelligence AI</h1>
<p>
AI-powered incident summarization,
priority classification and emergency response recommendation
</p>
</div>
""",
unsafe_allow_html=True
)

st.write("")

st.markdown(
"""
<div class="card">
<h2>📝 Incident Report</h2>
</div>
""",
unsafe_allow_html=True
)

incident_text = st.text_area(
    "",
    height=220,
    placeholder="""
Example:

A major fire broke out in a chemical factory.
Several workers are injured.
Emergency teams have reached the location.
"""
)

st.write("")

analyze = st.button("🚀 Analyze Incident")

if analyze:

    if not incident_text.strip():

        st.warning("Please enter an incident description.")

    else:

        with st.spinner("AI is analyzing the incident..."):

            try:

                result = analyze_incident(incident_text)

                st.success(
                    "Incident analysis completed successfully!"
                )

                st.divider()

                st.markdown(
                    "## 📌 Incident Summary"
                )

                st.markdown(
                    f"""
<div class="summary-box">
{result["summary"]}
</div>
""",
                    unsafe_allow_html=True
                )

                st.write("")

                col1,col2 = st.columns(2)

                with col1:

                    st.markdown(
                    """
<div class="card">
<h3>⚠️ Priority Level</h3>
<div class="priority-box">
""",
                    unsafe_allow_html=True
                    )

                    st.markdown(
                        result["priority"]
                    )

                    st.markdown(
                    """
</div>
</div>
""",
                    unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                    """
<div class="card">
<h3>🏢 Required Agencies</h3>
""",
                    unsafe_allow_html=True
                    )

                    for agency in result["agencies"]:

                        st.markdown(
                        f"""
<span class="tag">
{agency}
</span>
""",
                        unsafe_allow_html=True
                        )

                    st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                    )

                st.divider()

                with st.expander(
                    "🔍 View Structured JSON Output"
                ):

                    st.json(result)

            except Exception as e:

                st.error(
                    "Something went wrong while analyzing the incident."
                )

                st.exception(e)

st.markdown(
"""
<br><br>

<center>
<p style="color:#94a3b8">
Built with Gemini + LangChain + Streamlit
</p>
</center>
""",
unsafe_allow_html=True
)