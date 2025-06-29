import requests

API_KEY = "U-_PyVnNrQDq394epO1VEK5hEQ6oZuuaJQ3kEvvA7fYP"
PROJECT_ID = "845b3199-ab96-4870-9495-440a0708e6e5"

def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={api_key}"
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

def summarize_meeting(transcript, token, project_id):
    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    prompt = (
        "Summarize this meeting transcript and extract action items:\n"
        + transcript +
        "\n\nFormat as:\n"
        "### Summary\n[concise summary]\n\n"
        "### Action Items\n- [task] (owner: [name], deadline: [date])"
    )

    body = {
        "model_id": "granite-3b-instruct-v1",  # ✅ This is the model YOU have access to
        "project_id": project_id,
        "input": prompt,
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ API ERROR:", response.status_code)
        print(response.text)
        return None

if __name__ == "__main__":
    print("🔐 Getting token...")
    token = get_iam_token(API_KEY)

    print("🤖 Sending meeting text to Granite model...")
    meeting_text = """- Alice: Let's finalize the client report by Friday.
- Bob: I'll share a draft on Wednesday.
- Clara: Slide deck will be ready by tomorrow.
- Bob: I'll also schedule a demo for Tuesday and send invites."""

    result = summarize_meeting(meeting_text, token, PROJECT_ID)

    if result and "results" in result:
        output = result["results"][0]["generated_text"]
        print("\n✅ MEETING SUMMARY:\n")
        print(output)

        with open("meeting_summary.txt", "w", encoding="utf-8") as f:
            f.write(output)
            print("\n📝 Saved to 'meeting_summary.txt'")
    else:
        print("⚠️ No response received from the model.")
