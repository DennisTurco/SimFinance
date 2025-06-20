import matplotlib.pyplot as plt
import streamlit as st

class Plotter():

    @staticmethod
    def generate_random_walk_chart(generations: list[int]):
        st.divider()
        st.subheader("Random Walk Simulation")

        fig, ax = plt.subplots()

        for i, generation in enumerate(generations):
            ax.plot(generation, alpha=0.5, label=f'Simulation {i+1}')

        ax.set_title("Random Walk Simulation")
        ax.set_xlabel("Year")
        ax.set_ylabel("Cumulative value")
        ax.grid(True)

        if len(generations) <= 10:
            ax.legend()

        st.pyplot(fig)
