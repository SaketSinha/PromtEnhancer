# ✨ Prompt Enhancer

A Streamlit web app that transforms your rough ideas into clear, effective AI prompts using OpenAI's GPT models.

## Features

- **Simple Interface**: Enter your Role, Context, and Task
- **AI-Powered Enhancement**: Uses GPT to transform your input into a well-structured, professional prompt
- **Copy-Ready Output**: Get an enhanced prompt you can directly use in other AI conversations
- **Automatic Clarification**: Ensures the enhanced prompt includes instructions for AI to clarify assumptions

## Setup

### Requirements
- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd PromtEnhancer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-your-api-key-here
```

Replace `sk-your-api-key-here` with your actual OpenAI API key from https://platform.openai.com/api-keys

### Running Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Deployment on Railway

1. Push your code to GitHub
2. Go to [Railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your PromtEnhancer repository
5. Railway will auto-detect and install dependencies from `requirements.txt`
6. Go to **Variables** and add:
   ```
   OPENAI_API_KEY=sk-your-actual-key
   ```
7. Deploy! Your app will be live at the provided Railway URL

## Alternative: Streamlit Community Cloud

1. Push your code to GitHub (excluding `.env` file - it's in `.gitignore`)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repository
4. In the app settings, go to **Secrets** and add:
   ```
   OPENAI_API_KEY = "sk-your-actual-key"
   ```
5. Deploy!

## How It Works

1. Enter your **Role** - The perspective or expertise the AI should take
2. Enter your **Context** - Background information about your situation
3. Enter your **Task** - What you want the AI to do
4. Click **Enhance Prompt** - The app sends this to GPT which transforms it into a clearer prompt
5. Copy the enhanced prompt and use it in your favorite AI tool

## Security Note

Your API key is never stored or logged. It's only used to make the API request during your session.

## License

MIT
