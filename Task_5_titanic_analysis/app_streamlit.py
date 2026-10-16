"""
Titanic Interactive Dashboard — Streamlit + Plotly
Run locally with:  streamlit run app_streamlit.py
Requires: titanic_cleaned.csv in the same folder (produced by titanic_analysis.ipynb / .py)
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Titanic Analytics", page_icon="🚢", layout="wide")

# ---------------------------------------------------------------- data ----
@st.cache_data
def load_data():
    df = pd.read_csv("titanic_cleaned.csv")
    return df

df = load_data()

# ---------------------------------------------------------------- sidebar filters ----
st.sidebar.header("Filters")
classes = st.sidebar.multiselect("Passenger class", sorted(df["Pclass_name"].unique()),
                                  default=sorted(df["Pclass_name"].unique()))
sexes = st.sidebar.multiselect("Sex", sorted(df["Sex"].unique()), default=sorted(df["Sex"].unique()))
ports = st.sidebar.multiselect("Port of embarkation", sorted(df["Embarked_name"].dropna().unique()),
                                default=sorted(df["Embarked_name"].dropna().unique()))
age_range = st.sidebar.slider("Age range", int(df.Age.min()), int(df.Age.max()),
                               (int(df.Age.min()), int(df.Age.max())))
alone_opt = st.sidebar.radio("Travel status", ["All", "Travelling alone", "With family"])

f = df[df.Pclass_name.isin(classes) & df.Sex.isin(sexes) & df.Embarked_name.isin(ports) &
       df.Age.between(*age_range)]
if alone_opt == "Travelling alone":
    f = f[f.IsAlone == 1]
elif alone_opt == "With family":
    f = f[f.IsAlone == 0]

st.sidebar.markdown("---")
st.sidebar.caption(f"Showing **{len(f)}** of {len(df)} passengers")

# ---------------------------------------------------------------- header ----
st.title("🚢 Titanic Passenger Analytics")
st.caption("Cleaned & analysed with Pandas/NumPy · visualised with Plotly · served with Streamlit")

st.warning(
    "**Data integrity note:** in this file `Survived` is perfectly determined by `Sex` "
    "(100% of women marked survived, 0% of men). This is the Kaggle *gender_submission* "
    "baseline label, not a real historical outcome — treat survival figures below as a "
    "property of the label, not of history. Every other column is genuine.",
    icon="⚠️",
)

# ---------------------------------------------------------------- KPI row ----
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Passengers", len(f))
c2.metric("Marked survived", int(f.Survived.sum()))
c3.metric("Survival rate", f"{f.Survived.mean()*100:.1f}%" if len(f) else "—")
c4.metric("Average age", f"{f.Age.mean():.1f}" if len(f) else "—")
c5.metric("Average fare", f"£{f.Fare.mean():.1f}" if len(f) else "—")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Demographics", "Class & Fare", "Insights"])

# ---------------------------------------------------------------- Overview ----
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        rate = (f.groupby("Pclass_name")["Survived"].mean() * 100).reindex(
            ["1st Class", "2nd Class", "3rd Class"]).reset_index()
        fig = px.bar(rate, x="Pclass_name", y="Survived", title="Survival rate by class",
                     labels={"Survived": "Survival %", "Pclass_name": ""}, color="Pclass_name",
                     color_discrete_sequence=["#CFA14B", "#59A6A8", "#7A8C99"])
        fig.update_layout(showlegend=False, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.histogram(f, x="Sex", color="Status", barmode="group",
                            title="Survival by gender",
                            color_discrete_map={"Survived": "#59A6A8", "Died": "#C9584A"})
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        port = f.groupby("Embarked_name").agg(count=("Survived", "size"),
                                               rate=("Survived", lambda s: s.mean()*100)).reset_index()
        fig = go.Figure()
        fig.add_bar(x=port.Embarked_name, y=port["count"], name="Passengers", marker_color="#1B3B4B")
        fig.add_trace(go.Scatter(x=port.Embarked_name, y=port.rate, name="Survival %",
                                  yaxis="y2", mode="lines+markers", line=dict(color="#CFA14B", width=3)))
        fig.update_layout(title="Port of embarkation", template="plotly_white",
                           yaxis=dict(title="Passengers"),
                           yaxis2=dict(title="Survival %", overlaying="y", side="right", range=[0, 100]))
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        corr = f[["Pclass", "Age", "Fare", "FamilySize", "IsAlone", "HasCabin", "Survived"]].corr()["Survived"].drop("Survived")
        fig = px.bar(corr.sort_values(), orientation="h", title="Correlation with survival",
                     color=corr.sort_values().values, color_continuous_scale="RdBu", range_color=[-.3, .3])
        fig.update_layout(template="plotly_white", coloraxis_showscale=False, yaxis_title="", xaxis_title="Pearson r")
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- Demographics ----
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(f, x="Age", color="Status", nbins=20, barmode="overlay", opacity=0.7,
                            title="Age distribution by outcome",
                            color_discrete_map={"Survived": "#59A6A8", "Died": "#C9584A"})
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        order = ["Child (0-12)", "Teen (13-18)", "Young Adult (19-35)", "Adult (36-60)", "Senior (60+)"]
        rate = (f.groupby("AgeGroup")["Survived"].mean() * 100).reindex(order).reset_index()
        fig = px.bar(rate, x="AgeGroup", y="Survived", title="Survival rate by age group",
                     labels={"Survived": "Survival %", "AgeGroup": ""}, color_discrete_sequence=["#CFA14B"])
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        rate = f.groupby("FamilySize")["Survived"].mean().mul(100).reset_index()
        fig = px.line(rate, x="FamilySize", y="Survived", markers=True,
                      title="Survival rate by family size",
                      labels={"Survived": "Survival %", "FamilySize": "People on the ticket"})
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        fig = px.histogram(f, x="Title", color="Status", title="Titles extracted from names",
                            color_discrete_map={"Survived": "#59A6A8", "Died": "#C9584A"})
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- Class & Fare ----
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.box(f, x="Pclass_name", y="Fare_capped", color="Pclass_name",
                     title="Fare distribution by class (capped)",
                     color_discrete_sequence=["#CFA14B", "#59A6A8", "#7A8C99"])
        fig.update_layout(template="plotly_white", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.scatter(f, x="Age", y="Fare_capped", color="Status", hover_data=["Pclass_name", "Sex", "Title"],
                          title="Age vs Fare", color_discrete_map={"Survived": "#59A6A8", "Died": "#C9584A"})
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        rate = f.groupby("HasCabin")["Survived"].mean().mul(100)
        fig = px.bar(x=["No cabin recorded", "Cabin recorded"], y=[rate.get(0, 0), rate.get(1, 0)],
                     title="Survival by cabin availability", labels={"x": "", "y": "Survival %"},
                     color=["No cabin recorded", "Cabin recorded"],
                     color_discrete_sequence=["#C9584A", "#59A6A8"])
        fig.update_layout(template="plotly_white", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        deck = f[f.Deck != "Unknown"]["Deck"].value_counts().reset_index()
        deck.columns = ["Deck", "Count"]
        fig = px.pie(deck, names="Deck", values="Count", title="Deck distribution (known cabins)", hole=0.4)
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- Insights ----
with tab4:
    st.subheader("Key Insights")
    st.error(
        "**The target column is not real data.** Survival is perfectly separable by gender — "
        "every woman is labelled survived, every man died. No model trained on this file learns "
        "anything beyond \"female = survived\"; treat the other columns as the analysable content."
    )
    st.info(
        "**Class buys a better cabin, not just a better label.** First-class passengers pay a "
        "noticeably higher average fare and have a cabin recorded far more often — wealth shows "
        "up in `Fare` and `HasCabin` more than anywhere else."
    )
    st.info(
        "**Third class carried over half the ship** (218 of 418, ~52%). Every cross-class "
        "comparison should account for this imbalance."
    )
    st.info(
        "**Age needed group-wise imputation.** A fifth of ages were missing; filling by "
        "Title + Pclass median keeps `Master`/`Miss` young rather than pulling everyone toward "
        "a flat global median."
    )
    st.info(
        "**Travelling alone is the strongest non-gender signal** — solo travellers skew toward "
        "young, third-class men."
    )
    st.info(
        "**Southampton dominates boarding**; Cherbourg passengers carry the highest average fare, "
        "entangling port with class."
    )
    st.info(
        "**Fare is heavily right-skewed** — 55 fares sit above the IQR fence, capped for plotting "
        "rather than deleted since they represent genuine first-class fares."
    )

st.markdown("---")
st.caption("Built with Python — Pandas, NumPy, Plotly, Streamlit.")
