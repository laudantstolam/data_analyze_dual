
var data = [10, 20, 30, 40, 50];

// Create an SVG container
var svg = d3.select("body").append("svg")
    .attr("width", 300)
    .attr("height", 150);

// Create bars based on the data
svg.selectAll("rect")
    .data(data)
    .enter().append("rect")
    .attr("x", function(d, i) { return i * 60; })
    .attr("y", function(d) { return 150 - d; })
    .attr("width", 50)
    .attr("height", function(d) { return d; })
    .attr("fill", "lightblue");


console.log("YOU IDOT");