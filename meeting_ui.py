import streamlit as st

# Page settings
st.set_page_config(page_title="AI Meeting Minutes Generator", layout="centered")

# Title and description
st.title("🧠 AI Meeting Minutes Generator")
st.markdown("This tool uses IBM Granite model logic to generate meeting summaries and action items from transcripts.")

# Text input box
transcript = st.text_area("📄 Paste your meeting transcript here", height=250)

# Sample mocked output from Granite
mock_summary = """
### 📝 Summary
The team discussed the new campaign launch, newsletter layout, pitch deck updates, and scheduling a client demo.

### ✅ Action Items
- Finalize social media plan (Owner: Shreyas, Deadline: Wednesday)
- Design newsletter layout (Owner: Allan, Deadline: Friday)
- Update client pitch deck (Owner: Shreyas, Deadline: Monday)
- Schedule demo for Tuesday (Owner: Allan, Deadline: Today)
- 
"""

# Button to simulate generation
if st.button("🧠 Generate Summary"):
    if transcript.strip() == "":
        st.warning("⚠️ Please paste a meeting transcript first.")
    else:
        st.success("✅ AI Summary Generated!")
        st.markdown(mock_summary)
