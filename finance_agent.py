# %% [markdown]
# # Personal Finance AI Agents
# 
# Build an AI-powered Personal Finance Assistant using LangChain Agents and Tools.
# The agent should help users perform financial calculations and planning such as EMI calculation,investment returns, and budget allocation. The LLM must decide which tool to use depending on the user query.
# 

# %%
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import tool

# %%
#load environments
load_dotenv()

# %%
#Initialize LLM
llm = ChatOpenAI(
    model = 'gpt-6-luna',
    temperature= 1
)

# %% [markdown]
# ## EMI calculator

# %% [markdown]
# ### create the tools

# %%
#EMI calculator
@tool
def EMI_calculator(loan_amount: float, rate : float, number_of_months: float) -> float:
    '''Here we use this tool to calculate the EMI of the given values an give it's output, where it converts the rate in monlthly rate and then add in the formula given and then returns the value'''
    rate = rate/100
    monthly_rate = rate/12
    EMI = (loan_amount * monthly_rate * (1 + monthly_rate)**number_of_months)/((1 + monthly_rate)**number_of_months - 1)

    return EMI

# %% [markdown]
# ## Calculator Tool 

# %%
# here it does the normal multiplication, division, subtraction, and addition in the calculator
search_tool = DuckDuckGoSearchRun()
repltool = PythonREPLTool()

# %% [markdown]
# ## SIP Investment Calculator

# %%
@tool
def SIP_calc(monthly_Investment : float, Return : float, no_Months: int) -> str:
    ''' Here we returns the Simple investment that they returns the estimated final value'''
    monthly_Return = ((1+(Return/100))**(1/12))-1
    FV = monthly_Investment * (((1 + monthly_Return)**no_Months)-1) / monthly_Return
    total_invested = round(monthly_Investment*no_Months)
    estimated_gain = round(FV - (monthly_Investment*no_Months))
    return f"future value after {no_Months} is: {FV:,.2f}, where you have invested around: {total_invested:,.2f}, with an estimated gain of:{estimated_gain:,.2f}"

# %% [markdown]
# ## Budget Planner Tool

# %%
@tool
def Budget_Planner(budget: float) -> float:
    ''' here we create a tool for a budget planning for the user if they asks for monthly budget planning for there budget they for the month'''

    Needs = budget*0.5

    Wants = budget*0.3

    Saving = budget*0.2

    return Needs, Wants, Saving

# %%
agent = create_agent(
    model = llm,
    tools = [search_tool, repltool, Budget_Planner, EMI_calculator, SIP_calc],
    system_prompt="""
        You are a financial analyst that all the calculation work.

        Following this reasoning patterns:
        1. If  they give some basic calculation like multiplication, division, subtraction, addition or other the extract the nuremric values and use repltool to do the excecution.
        2. If the user asks to create a budget for me and gave only the budget value then use Budget_Planner tool for it and give them how much they need, what they want and there savings give the budget value in float type format.
        3. If they ask for SIP and also gave you the numbers like monthly value, monthly return and no of month(if they give it in year then convert it into months using repltool) in float type format then use it in SIP_calc tool for giving the SIP value which is how will you get and how much did you invest and also the estimate gain of it.
        4. If they ask to calculate EMI then use EMI_calculator where it calculate the EMI taking loan amount, rate and number of months(if they give it in year then convert it into months using repltool) also add these values in float type format.
        5. also make sure if they any other than financial question then tell them "Here we don't reply any generic question as we mainly works on fincial type works which we can help you."
        6. If the user ask financial related questions like the current scenario and all use search_tool and repltool for it.
    """
)

# %%
#while True:
#    user_input = input("\nAsk about an order (or type 'exit'): ")

#    if user_input.lower() == "exit":
#        break

#    response = agent.invoke({
#        "messages": [
#            {"role": "user", "content": user_input}
#        ]
#    })

#    print("\nResponse:")
#    print(response["messages"][-1].content)




