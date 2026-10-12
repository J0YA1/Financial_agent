# Financial_agent

An AI-powered Personal Finance Assistant built with **LangChain and Streamlit** that helps users perform financial calculations through natural-language conversations. The agent interprets user queries and selects the appropriate tool to calculate EMI, estimate SIP investment returns, and support personal budgeting.

## Features

- **EMI Calculator:** Calculate monthly loan installments based on loan amount, interest rate, and loan tenure.
- **SIP Calculator:** Estimate the future value of monthly investments based on the investment amount, duration, and expected annual return.
- **Budget Planning:** Help users organize their monthly income across expenses, savings, and investments.
- **AI Agent:** Uses LangChain to interpret user questions and select the appropriate calculation tool.
- **Natural-Language Interface:** Ask financial questions conversationally instead of entering values into separate calculators.
- **Interactive Web App:** Streamlit provides a simple interface for interacting with the assistant.

## Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **Interface:** Streamlit
- **Environment Variables:** python-dotenv
- **AI Model:** Configured language model supported by your LangChain integration

## Project Structure

```text
Finance_Agent/
├── app.py
├── finance_agent.py
├── .env
├── requirements.txt
└── README.md
```

- `app.py` — Streamlit chat interface.
- `finance_agent.py` — LangChain agent and financial calculation tools.
- `.env` — Stores API credentials locally; do not upload this file.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Finance_Agent.git
cd Finance_Agent
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes Streamlit, LangChain, the relevant model-provider integration, and any additional packages used by your tools.

### 4. Configure API credentials

Create a `.env` file in the project root and add the API key required by your configured model provider.

```env
OPENAI_API_KEY=your_api_key_here
```

Use the environment variable name expected by your code. Never commit actual API keys or other secrets to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## Example Queries

Try asking the assistant:

- "Calculate EMI for a ₹10 lakh loan at 8% annual interest for 20 years."
- "If I invest ₹7,000 monthly for 15 years at a 10% annual return, what could my investment grow to?"
- "Help me plan a monthly budget with an income of ₹40,000."

## How It Works

1. The user enters a financial question through the Streamlit interface.
2. The LangChain agent interprets the request.
3. The agent selects the relevant financial calculation tool.
4. The tool performs the calculation using the supplied parameters.
5. The agent presents the result in a natural-language response.

## Future Improvements

- Add savings-goal planning.
- Add loan affordability analysis.
- Visualize investment growth over time using charts.
- Improve input validation and handling of missing information.
- Add downloadable financial summaries.
- Deploy the application online.

## Disclaimer

This application is intended for educational and informational purposes. Financial calculations are estimates based on the supplied inputs and assumptions. Investment returns are not guaranteed, and this tool does not provide personalized financial advice.

## Author

**Joyal Joseph**
