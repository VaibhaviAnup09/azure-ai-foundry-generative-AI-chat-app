# Azure AI Foundry Simple Chat App

This is a basic Python application that uses the Azure AI Foundry SDK to interact with GPT models. It demonstrates how to set up a project client, send prompts, and receive AI-generated responses in a chat-like interface.

## 🚀 Tech Stack

- Python
- Azure AI Foundry SDK
- Azure OpenAI
- dotenv (for secure config management)

## ⚙️ Setup Instructions

1. Clone the repository:

git clone https://github.com/vaibhavigs15/azure-ai-foundry-chat-app.git
cd azure-ai-foundry-generative-AI-chat-app

2. (Optional but recommended) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt


4. Create a `.env` file with the following:

PROJECT_ENDPOINT=https://<your-project-endpoint>.projects.azure.com
MODEL_DEPLOYMENT=<your-model-deployment-name>

5. Run the chat application:

python chat-app.py

## 📝 Notes

This project was created as part of my learning and exploration of Azure AI Foundry during the Azure AI Skills Challenge.



