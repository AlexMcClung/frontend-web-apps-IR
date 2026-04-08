## Degree Completions by Level and Subgroup

```js
// Import data
const genderData = FileAttachment("./data/data_gender.csv").csv({typed: true})
const citzData = FileAttachment("./data/data_citz.csv").csv({typed: true})
```

```js
// Create and display user input for degree level
const selectedLevel = view(Inputs.select(["Associates","Bachelors","Masters","PhD"], {value: "Bachelors", label: "Select degree level:"}))
```

```js
// Create and display user input for subgroup
const selectedDemo = view(Inputs.radio(["Gender", "Citizenship"], {value: "Gender", label: "Select subgroup:"}))
```

```js
// Choose and subset data based on user input
const sourceData = selectedDemo === "Gender" ? genderData : citzData;
const tableData = sourceData.filter((d) => d.Level === selectedLevel);
```

```js
// Plot data user selected data
Plot.plot({
  marginLeft: 70,
  x: {type: "band", label: "Fiscal Year"},
  y: {label: "Degrees awarded"},
  marks: [
    Plot.rectY(
      tableData, {
      x: (d) => String(d.Year),
      y: "Degrees",
      fill: "Group",
      tip: true
    }
    ),
  ],
})
```

```js
const dataPivoted = aq
  .from(sourceData)
  .groupby(["Year", "Level"])
  .pivot("Group", "Degrees")
  .objects();
```

```js
const withTotal = dataPivoted.map(row => ({
  ...row,
  Year: String(row.Year),
  Total: selectedDemo === "Gender" 
    ? row.Men + row.Women 
    : row["Nonresident Alien"] + row["US Cit Perm Res"]
}));
```

```js
const search = view(Inputs.search(withTotal)) 
```

```js
Inputs.table(search, {select: false, maxWidth: "60%"})
```

<small>Source: IPEDS Degree Completions Complete Data Files FY 2011-24</small>