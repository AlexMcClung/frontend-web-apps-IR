import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    # Import libraries
    import marimo as mo
    import polars as pl
    import altair as alt

    return alt, mo, pl


@app.cell
def _(mo, pl):
    # Import data files

    genderLoc = mo.notebook_location() / 'public' / 'data_gender.csv'
    citzLoc = mo.notebook_location() / 'public' / 'data_citz.csv'

    df_gender = pl.read_csv(str(genderLoc))
    df_citz = pl.read_csv(str(citzLoc))
    return df_citz, df_gender


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Degree Completions by Level and Subgroup
    """)
    return


@app.cell
def _(mo):
    # Create and display degree level dropdown
    dd = mo.ui.dropdown(["Associates", "Bachelors", "Masters", "PhD"], label="Select degree level:", value="Bachelors")
    dd
    return (dd,)


@app.cell
def _(mo):
    # Create and display group selection radio buttons
    radio = mo.ui.radio(["Gender", "Citizenship"], label="Select subgroup:", value="Gender", inline=True)
    radio
    return (radio,)


@app.cell
def _(df_citz, df_gender, radio):
    # Determine which dataframe to use based on the radio button selection
    if radio.value == 'Gender':
        df_grp = df_gender
    else:    
        df_grp = df_citz
    return (df_grp,)


@app.cell
def _(dd, df_grp, pl):
    # Filter data based on degree level selection from the dropdown
    df_display = df_grp.filter(pl.col("Level") == dd.value)
    return (df_display,)


@app.cell
def _(alt, dd, df_display, mo, radio):
    # Create barchart
    chart = alt.Chart(df_display).mark_bar().encode(
        x=alt.X('Year:O').title('Fiscal Year'),
        y=alt.Y('Degrees').title('Degrees Awarded'),
        color=alt.Color('Group'),
    ).properties(
        title=f"{dd.value} Degrees by {radio.value}" # Dynamic title based on selections
    )
    mo.ui.altair_chart(chart)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Source: IPEDS Degree Completions Complete Data Files, FY 2011-24*
    """)
    return


if __name__ == "__main__":
    app.run()
