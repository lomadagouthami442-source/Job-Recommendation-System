import pandas as pd
import streamlit as st
st.title("Job Recommendation System")
jobs = pd.read_csv("jobs.csv")
skills = st.text_input("Enter your skills")
if st.button("Recommend Jobs"):
    skills = skills.lower()
    results = []
    for i, row in jobs.iterrows():
        job_skills = row["Skills"].lower().split()
        matches = 0
        for skill in job_skills:
            if skill in skills:
                matches += 1
        if matches > 0:
            results.append((row["Job Title"], matches))
    results.sort(key=lambda x: x[1], reverse=True)
    st.subheader("Recommended Jobs")
    if results:
        for job, matches in results[:3]:
            st.write(job)
    else:
        st.write("No matching jobs found.")
