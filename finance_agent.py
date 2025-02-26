from phi.agent import Agent
import streamlit as st
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
    result=finance_agent.run(user,markdown=True, period="3mo")
    return (result)
    
    
    
def main():
    st.title("💰 Financial AI Assistant")

    user = st.text_area("Enter your financial question:", placeholder="Example: Summarize analyst recommendations for TSLA")

    if user:
        res = first(user) 
        if res:  
            st.write(res)
        else:
            st.write("No response received.")

if __name__ == "__main__":
    main()