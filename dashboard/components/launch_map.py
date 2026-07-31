import pandas as pd
import plotly.express as px
import streamlit as st


def show_launch_map(launch):

    lat = launch.get("latitude")
    lon = launch.get("longitude")

    if lat is None or lon is None:
        st.info("Launch coordinates unavailable.")
        return

    df = pd.DataFrame(
        {
            "Latitude": [float(lat)],
            "Longitude": [float(lon)],
            "Mission": [launch["name"]],
        }
    )

    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Mission",
        zoom=3,
        height=500,
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0,
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )