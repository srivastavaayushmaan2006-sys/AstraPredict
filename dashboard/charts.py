import plotly.express as px


def launches_per_year(df):

    yearly = (
        df.groupby("year")
        .size()
        .reset_index(name="Launches")
    )

    return px.line(
        yearly,
        x="year",
        y="Launches",
        markers=True,
        title="Launches Per Year",
    )


def provider_distribution(df):

    providers = (
        df["provider"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    providers.columns = ["Provider", "Launches"]

    return px.bar(
        providers,
        x="Provider",
        y="Launches",
        title="Top Providers",
    )


def mission_distribution(df):

    missions = (
        df["mission_type"]
        .value_counts()
        .reset_index()
    )

    missions.columns = ["Mission", "Count"]

    return px.pie(
        missions,
        values="Count",
        names="Mission",
        title="Mission Types",
    )