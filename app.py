import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="TalentLens AI",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("outputs/submission.csv")

df = load_data()

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("🤖 TalentLens AI")

st.sidebar.markdown("### AI Resume Intelligence Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🏆 Top Candidates",
        "📊 Analytics"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
TalentLens AI ranks candidates using

• Semantic Matching (40%)

• Career Analysis (20%)

• Skill Matching (15%)

• Behavior Analysis (15%)

• Experience (10%)
"""
)

st.sidebar.markdown("---")
st.sidebar.caption("👨‍💻 Developed by Souvik Pal")

# ----------------------------------------------------
# DASHBOARD
# ----------------------------------------------------

if page == "🏠 Dashboard":

    st.title("🤖 TalentLens AI")

    st.subheader("AI-Powered Resume Intelligence Platform")

    st.info("""
TalentLens AI uses Hybrid Artificial Intelligence to rank resumes based on:

• Semantic Resume Matching (40%)

• Career Progression Analysis (20%)

• Skill Matching (15%)

• Behavioral Analysis (15%)

• Experience Scoring (10%)

The system generates an explainable 100-point ranking for recruiters.
""")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "👥 Candidates",
        len(df)
    )

    col2.metric(
        "🥇 Highest Score",
        f"{df['Display_Score'].max():.2f}/100"
    )

    col3.metric(
        "📈 Average Score",
        f"{df['Display_Score'].mean():.2f}/100"
    )

    st.divider()

    st.subheader("🏅 Top 3 Candidates")

    top3 = df.head(3)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success("🥇 Rank #1")

        st.code(top3.iloc[0]["Candidate_ID"])

        st.metric(
            "Final Score",
            f"{top3.iloc[0]['Display_Score']}/100"
        )

    with c2:

        st.info("🥈 Rank #2")

        st.code(top3.iloc[1]["Candidate_ID"])

        st.metric(
            "Final Score",
            f"{top3.iloc[1]['Display_Score']}/100"
        )

    with c3:

        st.warning("🥉 Rank #3")

        st.code(top3.iloc[2]["Candidate_ID"])

        st.metric(
            "Final Score",
            f"{top3.iloc[2]['Display_Score']}/100"
        )

    st.divider()

    st.subheader("📈 Candidate Score Distribution")

    fig = px.histogram(
        df,
        x="Display_Score",
        nbins=20,
        color_discrete_sequence=["#1f77b4"]
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.divider()

    st.subheader("📋 Top 10 Candidates")

    st.dataframe(
        df.head(10),
        width="stretch",
        hide_index=True
    )
# ----------------------------------------------------
# TOP CANDIDATES PAGE
# ----------------------------------------------------

elif page == "🏆 Top Candidates":

    st.title("🏆 Top Ranked Candidates")

    st.write("### Search Candidate")

    search = st.text_input(
        "Enter Candidate ID (Example: CAND_0000021)"
    )

    if search:

        result = df[
            df["Candidate_ID"].str.contains(
                search,
                case=False
            )
        ]

        if len(result) > 0:

            st.success("Candidate Found")

            st.dataframe(
                result,
                width="stretch",
                hide_index=True
            )

        else:

            st.error("Candidate Not Found")

    st.divider()

    st.write("## Top 10 Candidates")

    st.dataframe(
        df.head(10),
        width="stretch",
        hide_index=True
    )

    st.divider()

    best = df.iloc[0]

    st.subheader("🧠 AI Explanation")

    st.success(f"""
### 🥇 {best['Candidate_ID']}

Final AI Score : **{best['Display_Score']}/100**

### Score Breakdown

✅ Semantic Matching : {best['Semantic']}/40

✅ Career Analysis : {best['Career']}/20

✅ Skill Matching : {best['Skill']}/15

✅ Behavioral Score : {best['Behavior']}/15

✅ Experience Score : {best['Experience']}/10

---

### Why was this candidate ranked first?

✔ Excellent semantic similarity with the Job Description

✔ Strong career progression

✔ Relevant technical skills

✔ Positive behavioral profile

✔ Valuable professional experience
""")

# ----------------------------------------------------
# ANALYTICS PAGE
# ----------------------------------------------------

elif page == "📊 Analytics":

    st.title("📊 Candidate Analytics")

    st.write("### Top 10 Candidate Scores")

    fig = px.bar(
        df.head(10),
        x="Candidate_ID",
        y="Display_Score",
        color="Display_Score",
        text="Display_Score"
    )

    fig.update_layout(
        xaxis_title="Candidate",
        yaxis_title="Score"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.divider()

    st.write("### Recruiter Insights")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Highest Score",
        f"{df['Display_Score'].max():.2f}"
    )

    c2.metric(
        "Lowest Score",
        f"{df['Display_Score'].min():.2f}"
    )

    c3.metric(
        "Average Score",
        f"{df['Display_Score'].mean():.2f}"
    )

    st.divider()

    st.write("### Download Results")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download submission.csv",
        data=csv,
        file_name="submission.csv",
        mime="text/csv"
    )

    st.success("TalentLens AI Ranking Completed Successfully ✅")