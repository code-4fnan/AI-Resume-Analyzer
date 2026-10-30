
import streamlit as st

from modules.resume_parser import extract_resume_text
from modules.predictor import predict_resume
from modules.skill_extractor import extract_skills
from modules.job_matcher import calculate_match


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Application heading
st.title("📄 AI Resume Analyzer")
st.write(
    "Analyze your resume using a fine-tuned DistilBERT model "
    "and identify your skills and job compatibility."
)

st.divider()

# Resume upload
st.subheader("Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume (PDF)",
    type=["pdf"]
)

# Job description
st.subheader("Job Description")

job_description = st.text_area(
    "Paste the job description here (optional)",
    height=180
)


if st.button("Analyze Resume", type="primary"):

    if uploaded_file is None:
        st.error("Please upload a resume PDF.")

    else:

        with st.spinner("Analyzing your resume..."):

            # Step 1: Extract resume text
            resume_text = extract_resume_text(uploaded_file)

            if not resume_text.strip():
                st.error(
                    "No text found. Please upload a text-based PDF."
                )
                st.stop()

            # Step 2: Predict job categories using DistilBERT
            predictions = predict_resume(resume_text)

            # Step 3: Extract skills
            skills = extract_skills(resume_text)

        st.success("Resume analyzed successfully!")

        # Step 4: Display AI predictions
        st.subheader("🤖 Predicted Job Categories")

        for prediction in predictions:

            st.write(
                f"**{prediction['category']}**"
            )

            st.progress(
                min(prediction["confidence"] / 100, 1.0)
            )

            st.caption(
                f"Model confidence: {prediction['confidence']}%"
            )

        st.caption(
            "These are model estimates, not guaranteed job suitability scores."
        )

        st.divider()

        # Step 5: Display extracted skills
        st.subheader("💻 Extracted Skills")

        if skills:

            st.write(", ".join(skills))

            st.metric(
                "Total Skills Identified",
                len(skills)
            )

        else:
            st.warning("No listed skills detected.")

        st.divider()

        # Step 6: Job description matching
        if job_description.strip():

            st.subheader("🎯 Job Description Match")

            with st.spinner("Calculating job similarity..."):

                match_score = calculate_match(
                    resume_text,
                    job_description
                )

            st.metric(
                "Semantic Similarity",
                f"{match_score}%"
            )

            # Extract required job skills
            job_skills = extract_skills(job_description)

            # Identify missing skills
            missing_skills = [
                skill
                for skill in job_skills
                if skill.lower() not in
                [s.lower() for s in skills]
            ]

            st.subheader("📌 Missing Skills")

            if missing_skills:

                st.write(", ".join(missing_skills))

            else:

                st.success(
                    "No missing skills from our predefined skill list."
                )

        else:

            st.info(
                "Add a job description to calculate job similarity "
                "and identify missing skills."
            )

        st.divider()

        # Step 7: Optional resume text preview
        with st.expander("View Extracted Resume Text"):

            st.text_area(
                "Resume Text",
                resume_text[:5000],
                height=300
            )

        # Disclaimer
        st.info(
            "AI predictions and similarity scores are estimates, "
            "not hiring recommendations."
        )
