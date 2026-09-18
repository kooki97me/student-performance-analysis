import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="📊",
    layout="wide"
)


# -------------------------
# Title
# -------------------------

st.title("📊 Student Performance Analysis")
st.write(
    "An interactive dashboard to analyze factors affecting "
    "students' academic performance."
)


# -------------------------
# Load Dataset
# -------------------------

try:
    data = pd.read_excel("student_data.xlsx")

except Exception as e:
    st.error(f"Unable to load the dataset: {e}")
    st.stop()


# -------------------------
# Dataset Overview
# -------------------------

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(data))

with col2:
    st.metric(
        "Average Final Marks",
        f"{data['Final_Marks'].mean():.2f}"
    )

with col3:
    st.metric(
        "Average Attendance",
        f"{data['Attendance (%)'].mean():.2f}%"
    )


st.dataframe(
    data,
    use_container_width=True
)


# -------------------------
# Top Performing Students
# -------------------------

st.header("🏆 Top Performing Students")

top_students = data.sort_values(
    "Final_Marks",
    ascending=False
).head(5)

st.dataframe(
    top_students,
    use_container_width=True
)


# -------------------------
# Attendance vs Final Marks
# -------------------------

st.header("📈 Attendance vs Final Marks")

fig1, ax1 = plt.subplots()

ax1.scatter(
    data["Attendance (%)"],
    data["Final_Marks"]
)

ax1.set_xlabel("Attendance (%)")
ax1.set_ylabel("Final Marks")
ax1.set_title("Attendance vs Final Marks")
ax1.grid(True)

st.pyplot(fig1)

plt.close(fig1)


# -------------------------
# Study Hours vs Final Marks
# -------------------------

st.header("📚 Study Hours vs Final Marks")

fig2, ax2 = plt.subplots()

ax2.scatter(
    data["Study_Hours"],
    data["Final_Marks"]
)

ax2.set_xlabel("Study Hours")
ax2.set_ylabel("Final Marks")
ax2.set_title("Study Hours vs Final Marks")
ax2.grid(True)

st.pyplot(fig2)

plt.close(fig2)


# -------------------------
# Summary
# -------------------------

st.header("💡 Key Insights")

attendance_corr = data["Attendance (%)"].corr(
    data["Final_Marks"]
)

study_hours_corr = data["Study_Hours"].corr(
    data["Final_Marks"]
)

st.write(
    f"- Correlation between attendance and final marks: "
    f"**{attendance_corr:.2f}**"
)

st.write(
    f"- Correlation between study hours and final marks: "
    f"**{study_hours_corr:.2f}**"
)

st.write(
    "These visualizations help understand the relationship "
    "between student habits and academic performance."
)
