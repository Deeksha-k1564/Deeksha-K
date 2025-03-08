import streamlit as st
import time

# Title
st.title("🎭What's your true personality type?")
st.write("Answer the following questions to discover if you're a **Thinker, Feeler, Doer, or Dreamer!**")

# Personality categories and scoring
personality_types = {"Thinker": 0, "Feeler": 0, "Doer": 0, "Dreamer": 0}

# Questions and answer choices
questions = [
    "How do you make important decisions?",
    "How do you handle conflict?",
    "How do you react when something goes wrong?",
    "What’s your biggest strength?",
    "If you had a superpower, what would it be?",
    "How do you like to work?",
    "What describes your communication style?",
    "What do people admire about you?",
    "If you could live anywhere, where would it be?",
    "What type of friend are you?"
]

options = [
    ["Analyze all possible outcomes", "Trust my heart", "Make a quick choice", "Imagine possibilities"],
    ["Stay calm and analyze both sides", "Listen to emotions", "Resolve it directly", "Avoid it "],
    ["Fix it logically", "Talk about it", "Solve it immediately", "Escape into creativity"],
    ["Problem-solving skills", "Kindness", "Confidence", "Creativity"],
    ["Super intelligence", "Healing", "Super speed", "Time travel"],
    ["Work alone", "Teamwork", "Independent and fast", "Creative and flexible"],
    ["Logical and direct", "Warm and expressive", "Fast and confident", "Poetic and imaginative"],
    ["Intelligence", "Emotional depth", "Determination", "Creativity"],
    ["Library of knowledge", "Cozy home", "Fast-paced city", "Magical world"],
    ["Gives advice", "Always listens", "Brings action", "Inspires creativity"]
]

# Mapping answer choices to personality types
personality_map = {
    0: "Thinker",
    1: "Feeler",
    2: "Doer",
    3: "Dreamer"
}

# Progress bar setup
progress_bar = st.progress(0)
total_questions = len(questions)
question_count = 0

# Display questions
responses = []
for i, question in enumerate(questions):
    answer = st.radio(question, options[i], key=f"q{i}", index=None)

    # Ensure the user has selected an answer before proceeding
    if answer:
        responses.append(answer)

        # Update personality score
        choice_index = options[i].index(answer)
        personality_type = personality_map[choice_index]
        personality_types[personality_type] += 1

        # Update progress bar
        question_count += 1
        progress_bar.progress(int((question_count / total_questions) * 100))

# Submit button
if st.button("See Your Personality Type! 🚀"):
    if len(responses) < total_questions:
        st.warning("⚠ Please answer all questions before submitting!")
    else:
        st.markdown("###Analyzing your personality... Please wait... ⏳")
        time.sleep(2)  # Simulate processing time

        # Determine dominant personality type
        dominant_personality = max(personality_types, key=personality_types.get)

        # Display results
        st.subheader(f"🎭 Your True Personality Type: **{dominant_personality}**!")

        # Personality descriptions
        descriptions = {
            "Thinker": "🧠 You are **logical, analytical, and love solving problems.** You excel at critical thinking and planning!",
            "Feeler": "❤️ You are **empathetic, kind, and deeply connected to emotions.** You prioritize relationships and harmony!",
            "Doer": "🔥 You are **energetic, action-driven, and confident.** You take charge and always move forward!",
            "Dreamer": "🌙 You are **creative, imaginative, and visionary.** You love exploring new ideas and thinking outside the box!"
        }
        st.write(descriptions[dominant_personality])

        # Score breakdown
        st.write("### 🔢 Score Breakdown:")
        st.json(personality_types)

        # Retake quiz button
        if st.button("🔄 Retake Quiz"):
            st.experimental_rerun()
