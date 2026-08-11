import pandas as pd
import streamlit as st
st.set_page_config(page_title="Job Recommendation System")
st.title("💼 Job Recommendation System")
st.write("Find suitable jobs based on your skills.")
jobs = pd.read_csv("jobs.csv")
skills_input = st.text_input("Enter your skills",placeholder="Example: Python, SQL, Machine Learning")
if st.button("🔍 Recommend Jobs"):
    if not skills_input.strip():
        st.warning("Please enter at least one skill.")
    else:
        user_skills=[skill.strip().lower() for skill in skills_input.split(",") if skill.strip()]
        results=[]
        for _,row in jobs.iterrows():
            job_skills=[skill.strip().lower() for skill in str(row["Skills"]).split(",") if skill.strip()]
            matched_skills=[skill for skill in job_skills if skill in user_skills]
            missing_skills=[skill for skill in job_skills if skill not in user_skills]
            if job_skills:
                match_percentage=round(len(matched_skills)/len(job_skills)*100)
            else:
                match_percentage=0
            if match_percentage>0:
                results.append({"Job Title":row["Job Title"],"Match":match_percentage,"Matched Skills":matched_skills,"Missing Skills":missing_skills})
        results.sort(key=lambda x:x["Match"],reverse=True)
        st.subheader("🎯 Recommended Jobs")
        if results:
            for job in results[:5]:
                st.markdown("---")
                st.subheader(job["Job Title"])
                st.write(f"📊 *Match: {job['Match']}%*")
                if job["Matched Skills"]:
                    st.write("✅ *Your matching skills:* "+", ".join(job["Matched Skills"]))
                if job["Missing Skills"]:
                    st.write("📚 *Skills to learn:* "+", ".join(job["Missing Skills"]))
                else:
                    st.success("🎉 You have all the required skills!")
        else:
            st.info("No matching jobs found. Try adding more skills.")
                    
