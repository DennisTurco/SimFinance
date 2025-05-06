import streamlit as st

st.title("SimFinance - How it works")

st.markdown("""
SimFinance relies on two main algorithms to simulate financial scenarios:

- [**Monte Carlo Method**](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [**Normal Distribution (Gaussian Distribution)**](https://en.wikipedia.org/wiki/Normal_distribution)

---
""")

st.subheader("📊 Monte Carlo Method")
st.image("imgs/montecarlo-simulation.png", width=500, caption="Monte Carlo Simulation")

st.markdown("""
SimFinance uses the **Monte Carlo method** to simulate how your finances might evolve over time under uncertain conditions — whether you invest or not.

This method works by:

- Running thousands of simulations with randomized yearly changes
- Sampling returns from a normal distribution, based on your input data (e.g., income growth, inflation, or investment returns)
- Generating a wide range of future outcomes to reflect real-world uncertainty

By visualizing these possibilities, SimFinance helps you understand:

- The likelihood of reaching your financial goals (retirement, savings, etc.)
- How your capital might evolve under various life events, even without investing
- The impact of inflation, unexpected costs, or different savings rates

Even if you choose not to invest, SimFinance still offers valuable insights into how your savings and expenses may grow or shrink — helping you plan ahead with more confidence.
""")

st.markdown("---")

st.subheader("🧮 Normal Distribution")
st.image("imgs/normal-distribution.jpg", width=500, caption="Normal (Gaussian) Distribution")

st.markdown("""
SimFinance assumes that investment returns follow a **normal (Gaussian) distribution**, also known as the **bell curve**.

This approach allows the simulation to:
- Apply the expected annual return as the average (mean)
- Use volatility (standard deviation) to represent how much returns can vary
- Generate a realistic range of outcomes, from conservative to aggressive scenarios

This statistical model reflects how, in many real-world financial cases, most results cluster around the average, while extreme outcomes are less frequent but still possible.
""")

st.markdown("---")

st.subheader("🔐 How Your Data Is Used")

st.markdown("""
The data you provide is used solely to simulate your personal financial path, including:

- Age and retirement goals
- Monthly expenses and income growth
- Investment contributions and risk profile
- Inflation and unexpected events

All inputs are used **locally in your browser** to compute projections — no data is stored or sent externally.
""")

st.markdown("---")

st.markdown("**Note:** These simulations are for educational purposes only and do not represent financial advice.")
