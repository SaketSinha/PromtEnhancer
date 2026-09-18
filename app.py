import streamlit as st
from openai import OpenAI


# --------------------------------------------------
# Page setup
# --------------------------------------------------

st.set_page_config(
    page_title="Prompt Enhancer",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Prompt Enhancer")

st.write(
    "Enter your Role, Context, and Task. "
    "The app will turn them into a clearer and more effective prompt."
)


# --------------------------------------------------
# API key
# --------------------------------------------------

api_key = st.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="sk-..."
)

st.caption(
    "Your API key is used only to make the API request during this session."
)


# --------------------------------------------------
# User inputs
# --------------------------------------------------

role = st.text_area(
    "Role",
    placeholder="Example: You are an experienced marketing strategist."
)

context = st.text_area(
    "Context",
    placeholder=(
        "Example: I run a small education company and want to improve "
        "our LinkedIn marketing."
    )
)

task = st.text_area(
    "Task",
    placeholder=(
        "Example: Help me create a LinkedIn content strategy for the next month."
    )
)


# --------------------------------------------------
# Generate enhanced prompt
# --------------------------------------------------

if st.button("Enhance Prompt", type="primary"):

    if not api_key:
        st.error("Please enter your OpenAI API key.")

    elif not role or not context or not task:
        st.error("Please complete Role, Context, and Task.")

    else:

        client = OpenAI(api_key=api_key)

        user_prompt = f"""
ROLE:
{role}

CONTEXT:
{context}

TASK:
{task}
"""

        instructions = """
You are an expert prompt engineer.

Your job is to transform the user's Role, Context, and Task into a much
clearer and more effective prompt for another GPT model.

Do NOT perform the task.

Do NOT answer the user's original question.

Return only the enhanced prompt.

The enhanced prompt should:

1. Preserve the user's original intention.
2. Clearly define the role the AI should play.
3. Include all relevant context supplied by the user.
4. Clearly state the task and expected outcome.
5. Add useful instructions about reasoning, structure, constraints,
   quality, or output format when appropriate.
6. Avoid inventing information that the user did not provide.
7. Explicitly instruct the AI to clarify important assumptions,
   ambiguities, or missing information before giving its final response.
8. Be written so that the user can copy and paste it directly into
   another AI conversation.

Return only the improved prompt. Do not explain what you changed.
"""

        try:

            with st.spinner("Improving your prompt..."):

                response = client.responses.create(
                    model="gpt-5-mini",
                    instructions=instructions,
                    input=user_prompt
                )

                enhanced_prompt = response.output_text.strip()

            # Extra safeguard:
            # make sure the required clarification instruction
            # is always present in the final prompt.
            clarification_instruction = (
                "\n\nBefore providing your final response, identify and "
                "clarify any important assumptions, ambiguities, or missing "
                "information that could materially affect the answer."
            )

            if "clarif" not in enhanced_prompt.lower():
                enhanced_prompt += clarification_instruction

            st.subheader("Enhanced Prompt")

            st.text_area(
                "Copy this prompt:",
                value=enhanced_prompt,
                height=450
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")