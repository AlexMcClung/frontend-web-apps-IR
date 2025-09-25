# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "polars==1.33.1",
# ]
# ///

import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Marimo App Example""")
    return


@app.cell
def _(mo):
    mo.md(r"""For more information, visit [marimo.io](https://marimo.io).""")
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt

    dataLoc = mo.notebook_location() / "public" / "iris.csv"

    df = pl.read_csv(str(dataLoc))
    return alt, df, mo, pl


@app.cell
def _(mo):
    dd = mo.ui.multiselect(options=['setosa', 'versicolor', 'virginica'], value=['setosa', 'versicolor', 'virginica'], label='Select species:')
    dd
    return (dd,)


@app.cell
def _(alt, dd, df, mo, pl):
    filtered_data = df.filter(pl.col('Species').is_in(dd.value))
    _chart = (
        alt.Chart(filtered_data).mark_point().encode(
        x=alt.X("SepalWidth").scale(domain=[1, 5]),
        y=alt.Y("SepalLength").scale(domain=[3, 9]),
            color="Species"
        )
    )
    chart = mo.ui.altair_chart(_chart)
    chart
    return (filtered_data,)


@app.cell
def _(filtered_data):
    filtered_data[['Species', 'SepalWidth', 'SepalLength', 'PetalWidth', 'PetalLength']]
    return


if __name__ == "__main__":
    app.run()
