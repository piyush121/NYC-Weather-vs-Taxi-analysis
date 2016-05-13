'use strict';

//EXAMPLE ONE 
var sales = [
  { product: 'Snickers',  count: 12 },
  { product: 'Twix',  count: 30 },
  { product: 'Pez', count: 9 },
  { product: 'Nerds', count: 19 },
  { product: 'Rollos', count: 10 },
  { product: 'Altoids', count: 5 },
  { product: 'N/A', count: 15 },
];
//set up the angles of the pie chart using the pie layout helper
var pie = d3.layout.pie()
  .value(function(d) { return d.count })

//connect our data to the slices
var slices = pie(sales);

//size of the pie chart
var arc = d3.svg.arc()
  .innerRadius(0)
  .outerRadius(100);

// another helper that returns a color based on an ID, category10
var color = d3.scale.category10();


var svg = d3.select('svg.pie');
var g = svg.append('g')
  .attr('transform', 'translate(200, 100)')

g.selectAll('path.slice')
  .data(slices)
    .enter()
      .append('path')
        .attr('class', 'slice')
        .attr('d', arc)
        .attr('fill', function(d) {
          return color(d.data.product);
        });

// building a legend
svg.append('g')
  .attr('class', 'legend')
    .selectAll('text')
    .data(slices)
      .enter()
        .append('text')
          .text(function(d) { return '• ' + d.data.product + ' (' + d.data.count + ')'; })
          .attr('fill', function(d) { return color(d.data.product); })
          .attr('y', function(d, i) { return 20 * (i + 1); })


//EXAMPLE 2

//setup size of line chart
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

//parse data from file
var parseDate = d3.time.format("%d-%b-%y").parse;

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
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.users); });

var svg = d3.select(".linechart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("data.tsv", function(error, data) {
  if (error) throw error;
//traverse through the data 
  data.forEach(function(d) {
    d.date = parseDate(d.date);
    d.users = +d.users;
  });
//establish the domain for x and y axes
  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain(d3.extent(data, function(d) { return d.users; }));

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
      .text("Users (unique)");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
});


