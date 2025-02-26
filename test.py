import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Initialize the Financial AI Agent
def tool(user_query):
    finance_agent = Agent(
        name="Financial AI Agent",
        model=Groq(id="llama-3.2-11b-vision-preview"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True,
                historical_prices=True,
            )
        ],
        instructions=["Use tables to display the data"],
        show_tool_calls=True,
        markdown=True,
    )
    result=finance_agent.print_response
# Streamlit UI
st.title("💰 Financial AI Assistant")

# User input
user_query = st.text_area("Enter your financial question:", placeholder="Example: Summarize analyst recommendations for TSLA")

# Button to process query
if st.button("Ask AI"):
    if user_query.strip():
        with st.spinner("Fetching response..."):
            response = finance_agent.run(user_query)  # Use `run()` to capture output
            
            # Display the response
            if isinstance(response, str):  # If response is a string, display directly
                st.markdown(response)
            else:
                st.json(response)  # If response is structured data, show it as JSON
    else:
        st.warning("Please enter a valid question.")
