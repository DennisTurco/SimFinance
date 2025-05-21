import streamlit as st

def main_title() -> None:
    st.title("SimFinance - Financial Simulator")

def main_description() -> None:
    st.markdown("""
Welcome to **SimFinance**, your personal financial simulation tool.

With this app, you can:
- Model and simulate various investment scenarios
- Analyze the effects of compound interest over time
- Compare different financial strategies

To learn more about how SimFinance works and the mathematics behind it, use the link below:
""")

    st.page_link("./pages/1_how_it_works.py", label="📘 How it works")

    st.markdown("""
This project is **open source** and free to use or modify.
Feel free to explore the repository or contribute to its development:
""")

    st.page_link("https://github.com/DennisTurco/SimFinance", label="🟢 GitHub Repository")

    st.markdown("**Note:** All simulations are intended for educational purposes only.")