import streamlit as st
import pandas as pd
import datetime

# Title
st.title("Learning Growth Management App")

# Sidebar for navigation
menu = [
    "Topics", "Practice", "Tasks", "Assignments", 
    "Exam", "MCQs", "Set Learning Goals", 
    "Track Progress", "Daily Challenges", "Motivation"
]
choice = st.sidebar.selectbox("Navigation", menu)

# Session State to Store Data
if 'goals' not in st.session_state:
    st.session_state['goals'] = []
    st.session_state['progress'] = {}
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = {}

# Topics List
topics = {
    "Introduction to Python": [
        "Install Python and set up your environment",
        "Run your first Python script"
    ],
    "Variables and Data Types": [
        "Declare variables and assign values",
        "Understand different data types in Python"
    ],
    "Conditional Statements": [
        "Write if-else conditions",
        "Use logical operators in conditions"
    ],
    "Loops": [
        "Write a for loop to iterate over a list",
        "Use while loops for repetitive tasks"
    ],
    "Functions": [
        "Create a function that takes parameters",
        "Return values from a function"
    ],
    "Object-Oriented Programming": [
        "Define a class and create objects",
        "Use inheritance in Python"
    ],
    "Data Structures": [
        "Implement lists and dictionaries",
        "Work with sets and tuples"
    ]
}

# Initialize session state tasks with default topics if empty
for topic in topics:
    if topic not in st.session_state['tasks']:
        st.session_state['tasks'][topic] = []

# Topics Section
if choice == "Topics":
    st.subheader("Topics")
    for topic in topics.keys():
        st.write(f"- {topic}")

# Practice Section
elif choice == "Practice":
    st.subheader("Practice Tasks")
    for topic, task_list in topics.items():
        st.write(f"### {topic}")
        for task in task_list:
            st.write(f"- {task}")

# Tasks Section
elif choice == "Tasks":
    st.subheader("Select a Topic to Get Tasks")
    selected_topic = st.selectbox("Choose a Topic", list(topics.keys()))
    
    if selected_topic:
        st.write(f"### Tasks for {selected_topic}")
        for task in topics[selected_topic]:
            st.write(f"- {task}")
    
    task = st.text_input("Enter a new task:")
    if st.button("Add Task"):
        if task:
            if task in topics[selected_topic]:
                if task not in st.session_state['tasks'][selected_topic]:
                    st.session_state['tasks'][selected_topic].append(task)
                    st.success(f"✅ Task added: {task}")
                else:
                    st.warning("⚠️ This task is already added!")
            else:
                st.error(f"❌ Incorrect task! The correct tasks for {selected_topic} are:")
                correct_tasks_list = "\n".join([f"- {correct_task}" for correct_task in topics[selected_topic]])
                st.text(correct_tasks_list)
            st.rerun()

# Assignments Section
elif choice == "Assignments":
    st.subheader("Assignments")
    assignments = [
        "Build a basic calculator in Python",
        "Create a simple To-Do List App",
        "Write a Python script to manage student records"
    ]
    for assignment in assignments:
        st.write(f"- {assignment}")

# Exam Section
elif choice == "Exam":
    st.subheader("Exam Preparation")
    st.write("Get ready for your exam with these topics and practice tests!")

# MCQs Section
elif choice == "MCQs":
    st.subheader("Multiple Choice Questions (MCQs)")
    mcqs = {
        "What is the output of print(2**3)?": ["A) 6", "B) 8", "C) 9", "D) 16"],
        "Which keyword is used to define a function in Python?": ["A) func", "B) define", "C) def", "D) function"]
    }
    
    for question, options in mcqs.items():
        st.write(f"**{question}**")
        st.radio("Select the correct answer:", options)

# Set Learning Goals Section
elif choice == "Set Learning Goals":
    st.subheader("Set Your Learning Goals")
    goal = st.text_input("Enter a new learning goal:")
    if st.button("Add Goal"):
        if goal:
            st.session_state['goals'].append(goal)
            st.session_state['progress'][goal] = 0  # Initialize progress to 0%
            st.success(f"Goal added: {goal}")
    
    # Display existing goals
    if st.session_state['goals']:
        st.write("### Your Learning Goals")
        for g in st.session_state['goals']:
            st.write(f"- {g}")

# Track Progress Section
elif choice == "Track Progress":
    st.subheader("Track Your Learning Progress")
    if st.session_state['goals']:
        for goal in st.session_state['goals']:
            progress = st.slider(f"{goal} Progress (%)", 0, 100, st.session_state['progress'][goal])
            st.session_state['progress'][goal] = progress
    else:
        st.warning("No learning goals set yet. Please add goals first!")

# Daily Challenges Section
elif choice == "Daily Challenges":
    st.subheader("Daily Growth Mindset Challenges")
    challenges = [
        "Write down 3 things you learned today.",
        "Explain a concept you learned to someone else.",
        "Try learning something outside your comfort zone.",
        "Find a mistake you made and learn from it.",
        "Spend 10 minutes reflecting on today's progress.",
    ]
    st.write(f"### Your Challenge for Today: **{challenges[datetime.datetime.now().day % len(challenges)]}**")

# Motivation Section (default case)
else:
    st.subheader("Stay Motivated!")
    quotes = [
        "Failure is not the opposite of success; it's part of success.",
        "The only way to learn is to fail forward.",
        "Consistency beats intensity. Keep learning!",
        "Growth is a journey, not a destination.",
        "Mistakes are proof that you are trying."
    ]
    st.write(f"### Inspirational Quote: **{quotes[datetime.datetime.now().day % len(quotes)]}**")




  







