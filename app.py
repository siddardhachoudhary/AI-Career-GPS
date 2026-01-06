import streamlit as st

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Skill Assessment", "My Roadmap", "Community"]
)

# --- PAGE 1: HOME ---
if page == "Home":
    st.title("🚀 AI-Powered Career GPS")
    st.write(
        "Welcome! In normal apps you should search for, "
"Here AI will guide you.**"
    )
    st.image(
        "https://img.freepik.com/free-vector/learning-concept-illustration_114360-6186.jpg",
        width=400
    )
    st.info("Select 'Skill Assessment' in the sidebar and start your journey..")

# --- PAGE 2: SKILL ASSESSMENT ---
elif page == "Skill Assessment":
    st.title("🎯 Skill-DNA Assessment")
    st.write("Let's check your current knowledge.")

    q1 = st.slider("How good is your grip on Python? (1-10)", 1, 10, 5)
    q2 = st.selectbox("Have you ever done any projects?", ["No", "Basic", "Advanced"])

    if st.button("Save My Profile"):
        st.success("Your profile has been updated! Now check out 'My Roadmap'.")

# --- PAGE 3: MY ROADMAP ---
elif page == "My Roadmap":
    st.title("🗺️ Your Personalized Path")

    goal = st.selectbox(
        "Mee Career Goal?",
        ["Data Scientist", "Web Developer"]
    )

    level = st.select_slider(
        "Current Level",
        options=["Beginner", "Intermediate", "Expert"]
    )

    if st.button("Generate Roadmap"):
        st.subheader(f"Custom Path for {goal}:")

        if level == "Beginner":
            st.write(f"✅ Phase 1: Basics of {goal}")
            st.progress(25)
            st.info(f"Recommendation: Watch 'Intro to {goal}' on YouTube.")
        else:
            st.write("🚀 Phase 1: Advanced Portfolio Projects")
            st.progress(60)

# --- PAGE 4: COMMUNITY ---
elif page == "Community":
    st.title("🤝 Peer Connection")
    st.write("Connect with people with similar goals as you.")

    doubt = st.text_input("Ask a doubt to the community:")

    if st.button("Post Doubt"):
        st.success("Doubt posted! Expert mentors will reply soon.")
