## AI Meeting Minutes Generator

##  IBM Watsonx AI & Automation Unpacked Hackathon Submission  
By: Sanika Mangesh Jadhav

---

##  Problem Statement

Meetings generate a lot of valuable information, but capturing it manually is time-consuming and often inconsistent. Teams waste time writing summaries, remembering who owns which task, and tracking deadlines.

**Can AI automate meeting minutes and action item extraction — clearly, accurately, and instantly?**

---

##  What I Built

I built an AI-powered **Meeting Minutes Generator** using IBM’s **Granite foundation models** via **Watsonx Prompt Lab**, along with a custom front-end in Streamlit.

This tool:
- Accepts raw meeting transcripts
- Summarizes key discussion points
- Extracts actionable tasks
- Lists deadlines and task owners

---

## Tools & Technologies Used

| Tool | Purpose |

IBM Watsonx Granite (`granite-3-3-8b-instruct`) | Language model used to summarize and extract actions  
 Prompt Lab | For testing prompt behavior and tuning AI instructions  
 Python + Requests | Scripted API calls (attempted outside sandbox)  
 IBM Sandbox (limitation) | Prevented API model access, as expected  
 Streamlit | Front-end UI to simulate live user experience  
 OBS Studio (or Loom) | For screen recording the demo  

---

##  How It Works

### Prompt Lab

- I used Prompt Lab to interact with `granite-3-3-8b-instruct`
- Designed a custom prompt format:


Summary
[short overview]

Action Items
[task] (owner: [name], deadline: [date])

- The model generated accurate, structured output

###  Python Automation

- I created a Python script to:
- Get IAM token
- Call the model via API
- Process transcript input and show AI response

-  Due to IBM sandbox restrictions, the API call failed with `"model_not_supported"`  
-  The code logic remains correct and ready for production use

### Streamlit UI

- To simulate full functionality, I built a front-end UI
- Users can paste a transcript → click a button → see summary & tasks
- Output shown is mocked based on actual Prompt Lab results

---

##  Demo Video

A 3-minute video walkthrough is included in the submission, showing:
- Prompt Lab testing
- Python script (backend logic)
- Streamlit UI flow

---

##  Sandbox Limitation Note

> IBM sandbox does not allow foundation model API calls — only Prompt Lab is available for model access.  
> As recommended in IBM's docs, Prompt Lab was used for model interaction, and the front-end simulates production behavior.

---

## Future Improvements

- Connect Streamlit UI to live IBM model (outside sandbox)
- Add file upload for `.txt` transcripts
- Save summaries to `.pdf` or send via email
- Add team collaboration features

---
##Note: AI-Meeting-Summarizer/meeting_summary
This script demonstrates how the model would be used in production with full API access. In the hackathon sandbox, Prompt Lab was used instead.


## 🙋‍♀️ About Me

I'm Sanika Mangesh Jadhav, a B.Tech 1st yr student and a beginner developer, participating solo in my first hackathon.  
This project helped me explore real-world AI, prompt design, APIs, and UI development — and I built a complete workflow using IBM Watsonx.

## ✅ Thank you IBM & Watsonx Team!

This hackathon was a hands-on learning experience that helped me think like an AI builder — not just a user.