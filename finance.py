from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


def first(user):
    finance_agent=Agent(
        name="Financial AI Agent",
        model=Groq(id="llama-3.2-11b-vision-preview"),
        tools=[
            YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True,historical_prices=True)
        ],
        instructions=["Use tables to display the data"],
        show_tool_calls=True,
        markdown=True,
    )
    result=finance_agent.print_response(user,markdown=True, period="3mo")
    return (result)
    

user=input("Enter your Query:")
oj=first(user)
print(oj)


# finance_agent.print_response("Summarize analyst recommendation for Tesla and also the stock news", markdown=True, period="3mo")