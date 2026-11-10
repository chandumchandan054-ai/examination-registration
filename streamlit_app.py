import streamlit as st
import pandas as pd
from datetime import date

# Configure the application page
st.set_page_config(
    page_title="Examination Registration and Hall Ticket Management System",
    page_icon="🎓"
)

# Display the application title
st.title("Examination Registration and Hall Ticket Management System")

st.subheader("Student Information")

st.write("Enter your details to view your personalized greeting.")

# Accept student details
with st.form("student_details_form"):

    name = st.text_input("Enter Student Name")

    age = st.number_input(
        "Enter Student Age",
        min_value=1,
        max_value=120,
        value=18,
        step=1
    )

    submit = st.form_submit_button("Submit")

# Process the entered details
if submit:

    if name.strip():

        current_year = date.today().year

        estimated_birth_year = current_year - int(age)

        # Display personalized greeting
        st.success(f"Welcome, {name.strip()}!")

        st.write("Your examination registration details are:")

        st.write("Student Name:", name.strip())
        st.write("Student Age:", int(age))
        st.write("Estimated Year of Birth:", estimated_birth_year)

        # Create a DataFrame for visualization
        data = pd.DataFrame({
            "Year of Birth": [estimated_birth_year],
            "Age": [int(age)]
        })

        # Display the scatter chart
        st.subheader("Student Age vs. Estimated Year of Birth")

        st.scatter_chart(
            data,
            x="Year of Birth",
            y="Age"
        )

        st.caption(
            "Note: The year of birth is an estimate based on "
            "the current year and entered age."
        )

    else:
        st.error("Please enter the student's name.")
