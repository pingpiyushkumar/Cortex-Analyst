import streamlit as st

st.set_page_config(page_title="Zero-Ops Data Engineering (Prototype)", layout="wide")

st.set_page_config(page_title="Zero-Ops Data Engineering", layout="wide")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("📥 Zero-Ops Data Engineering — Step 1 Prototype")
st.write("Upload your data files and add a brief description.")

# --- User Text Input ---
user_prompt = st.text_area(
    "📝 Describe what you'd like to do with your data",
    placeholder="Example: 'Clean this dataset and generate summary statistics'"
)

# --- File Upload Widget ---
uploaded_files = st.file_uploader(
    "📂 Upload your files (CSV, Excel, JSON, PDF, ZIP)",
    type=["csv", "xlsx", "xls", "json", "pdf", "zip"],
    accept_multiple_files=True
)

st.divider()

# --- Display Basic Debug Information ---
st.header("🔍 Debug Output (Step 1)")
st.subheader("User Instruction")

if user_prompt:
    st.code(user_prompt)

st.subheader("Uploaded Files")

if uploaded_files:
    for file in uploaded_files:
        st.write(f"**Filename:** {file.name}")
        st.write(f"**Type:** {file.type}")
        st.write(f"**Size:** {file.size / 1024:.2f} KB")
else:
    st.write("No files uploaded yet.")

st.divider()

# Done
st.success("Step 1 UI ready. No processing implemented yet.")
