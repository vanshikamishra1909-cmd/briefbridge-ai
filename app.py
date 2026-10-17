
import requests
import streamlit as st

st.set_page_config(
    page_title="BriefBridge AI",
    page_icon="📚",
    layout="centered",
)

MODEL = "qwen3:0.6b"
OLLAMA_URL = "http://localhost:11434/api/generate"

st.title("📚 BriefBridge AI")
st.subheader("From assignment brief to action plan")

st.write(
    "Turn assignment instructions into a checklist, "
    "a suggested outline, and a practical work plan."
)

brief = st.text_area(
    "Paste your assignment instructions",
    height=200,
    placeholder=(
        "Example: Write an 8-page assignment on business "
        "ethics. Include an introduction, definition, "
        "characteristics, examples, and conclusion."
    ),
)

subject = st.text_input("Subject (optional)")

level = st.selectbox(
    "Study level",
    ["School", "Undergraduate", "Postgraduate", "Other"],
)

if st.button("Create my action plan", type="primary"):
    if len(brief.strip()) < 20:
        st.warning("Please enter a more detailed assignment brief.")
    else:
        prompt = f"""
You are BriefBridge, an assignment planning assistant.

Help students understand and plan their own work.
Do not invent missing deadlines or teacher requirements.
Label your recommendations as suggestions.

Study level: {level}
Subject: {subject or "Not specified"}

Original assignment instructions:
{brief}

Create these five sections:

1. REQUIREMENTS
List deliverables, topics, format, and page limits
only when they are specified.

2. CHECKLIST
List the tasks the student needs to complete.

3. SUGGESTED OUTLINE
Suggest headings and explain what each section
could contain.

4. WORK PLAN
Give a sensible order for completing the assignment.

5. VERIFY BEFORE SUBMISSION
Identify details the student should confirm against
the original instructions or with their teacher.
"""

        with st.spinner("Your local AI is preparing your plan..."):
            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": MODEL,
                        "prompt": prompt,
                        "stream": False,
                        "options": {"temperature": 0.3},
                    },
                    timeout=240,
                )
                response.raise_for_status()
                result = response.json()["response"].strip()

                st.markdown("## Your assignment action plan")
                st.markdown(result)

                st.download_button(
                    "Download action plan",
                    data=result,
                    file_name="briefbridge_action_plan.txt",
                    mime="text/plain",
                )

                st.caption(
                    "AI-generated suggestions. Verify them "
                    "against your original assignment brief."
                )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to Ollama. Make sure "
                    "Ollama is running on your laptop."
                )
            except requests.exceptions.Timeout:
                st.error(
                    "The model took too long to respond. "
                    "Try a shorter assignment brief."
                )
            except requests.exceptions.RequestException as exc:
                st.error(f"The request failed: {exc}")
            except (ValueError, KeyError):
                st.error("Ollama returned an unexpected response.")
