
//setup size of line chart
var margin = {top: 20, right: 20, bottom: 30, left: 70},
    width = 1500 - margin.left - margin.right,
    height = 800 - margin.top - margin.bottom;

//parse data from file
    var parseDate = d3.time.format("%Y-%m-%d %H:%M").parse;

//set scales
var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

//create axes
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

//construct the line using points from data
var line = d3.svg.line()
    .x(function(d) { return x(d.Day); })
    .y(function(d) { return y(d.Trips); });

var svg = d3.select(".linechart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("trips.csv", function(error, data) {
  if (error) throw error;
//traverse through the data 
  data.forEach(function(d) {
    d.Day = parseDate(d.Day);
    d.Trips = +d.Trips;
  });
//establish the domain for x and y axes
  x.domain(d3.extent(data, function(d) { return d.Day; }));
  y.domain(d3.extent(data, function(d) { return d.Trips; }));

//add "groups" 
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Trips (unique)");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
});


