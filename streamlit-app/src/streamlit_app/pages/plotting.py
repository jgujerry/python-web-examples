import time

import numpy as np
import pandas as pd
import streamlit as st


# st.set_page_config(
#     page_title="Timeseries Plotting",
#     page_icon="📈"
# )


def main():

    st.markdown("# Timeseries Plotting")
    st.write(
        """
        This is a demo about timeseries data
        """
    )


    # Generate sample time series data
    date_range = pd.date_range(start='2024-01-01', end='2024-03-01')
    data = np.random.randn(len(date_range))
    df = pd.DataFrame(data, index=date_range, columns=['Value'])

    # Display the DataFrame
    st.subheader('Input Data:')
    st.write(df)

    # Plot time series data
    st.subheader('Time Series Plot:')
    plot_type = st.selectbox('Select plot type:', ['Line Plot', 'Bar Plot'])

    if plot_type == 'Line Plot':
        st.line_chart(df)
    elif plot_type == 'Bar Plot':
        st.bar_chart(df)


if __name__ == '__main__':
    main()
