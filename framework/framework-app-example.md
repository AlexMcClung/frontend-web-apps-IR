# Observable Framework App Example

For more information, visit [Framework](https://observablehq.com/framework/).

```js
const iris = FileAttachment("data/iris.csv").csv({ typed: true });
```

```js
const species = view(
  Inputs.checkbox(["setosa", "virginica", "versicolor"], {
    sort: true,
    unique: true,
    value: ["setosa", "virginica", "versicolor"],
    label: "Select Species:",
  })
);
```

```js
const dat = iris.filter((d) => species.includes(d.Species));
```

```js
const chart = Plot.plot({
  width,
  grid: true,
  x: { label: "Length" },
  y: { label: "Width" },
  color: { legend: true },
  marks: [
    Plot.dot(dat, {
      x: "SepalLength",
      y: "SepalWidth",
      stroke: "Species",
      tip: true,
    }),
  ],
});
display(chart);
```

```js
const tab = view(Inputs.search(dat))
tab
```

```js
Inputs.table(tab)
```
