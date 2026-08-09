import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.title("Job Recommendation System")
jobs = pd.read_csv("jobs.csv")
skills = st.text_input("Enter your skills")
if st.button("Recommend Jobs"):
    if skills:
        vectorizer = TfidfVectorizer()
        data = vectorizer.fit_transform(jobs["Skills"].tolist() + [skills])
        similarity = cosine_similarity(data[-1], data[:-1]).flatten()
        jobs["Match"] = similarity * 100
        recommendations = jobs.sort_values("Match", ascending=False).head(3)
        st.subheader("Recommended Jobs")
        for _, job in recommendations.iterrows():
            st.write(f"*{job['Job Title']}* - {job['Match']:.2f}% match")
    else:
        st.warning("Please enter your skills.")
