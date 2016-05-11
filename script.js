
    var margin = { top: 30, right: 30, bottom: 40, left:70 }

    var height = 800 - margin.top - margin.bottom,
        width = 1800 - margin.left - margin.right,
        barWidth = 50,
        barOffset = 5;

    var tempColor;

    var colors = d3.scale.linear()
    .domain([0, 3000])
    .range(['#B58929','#C61C6F'])

    var yScale = d3.scale.linear()
            .range([0, height]);

    var xScale = d3.scale.ordinal()
            .rangeBands([0, width], 0.05)

    var tooltip = d3.select('body').append('div')
            .style('position', 'absolute')
            .style('padding', '0 10px')
            .style('background', 'white')
            .style('opacity', 0)

    d3.csv("trips.csv", type, function(error, data) {
  if (error) throw error;

    xScale.domain(data.map(function(d) { return d.Day; }));
    yScale.domain([0, d3.max(data, function(d) { return d.Trips; })]);

    var myChart = d3.select('#chart').append('svg')
        .style('background', '#E7E0CB')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', 'translate('+ margin.left +', '+ margin.top +')')
        .selectAll('rect').data(data) // edit.
        .enter().append('rect')
            .style('fill', function(d,i) {
                return colors(i);
            })
            .attr('width', xScale.rangeBand())
            .attr('x', function(d,i) {
                return xScale(d.Day);
            })
            .attr('height', 0)
            .attr('y', height)

        .on('mouseover', function(d) {

            tooltip.transition()
                .style('opacity', .9)

            tooltip.html(d.Trips)
                .style('left', (d3.event.pageX - 35) + 'px')
                .style('top',  (d3.event.pageY - 30) + 'px')


            tempColor = this.style.fill;
            d3.select(this)
                .style('opacity', .5)
                .style('fill', 'yellow')
        })

        .on('mouseout', function(d) {
            d3.select(this)
                .style('opacity', 1)
                .style('fill', tempColor)
        })

    myChart.transition()
        .attr('height', function(d) {
            return yScale(d.Trips);
        })
        .attr('y', function(d) {
            return height - yScale(d.Trips);
        })
        .delay(function(d, i) {
            return i;
        })
        .duration(1000)
        .ease('elastic')

    var vGuideScale = d3.scale.linear()
        .domain([0, d3.max(data, function(d) { return d.Trips; })])
        .range([height, 0])

    var vAxis = d3.svg.axis()
        .scale(vGuideScale)
        .orient('left')
        .ticks(10)

    var vGuide = d3.select('svg').append('g')
        vAxis(vGuide)
        vGuide.attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')')
        vGuide.selectAll('path')
            .style({ fill: 'none', stroke: "#000"})
        vGuide.selectAll('line')
            .style({ stroke: "#000"})

    var hAxis = d3.svg.axis()
        .scale(xScale)
        .orient('bottom')
        .ticks(10)

    var hGuide = d3.select('svg').append('g')
        hAxis(hGuide)
        hGuide.attr('transform', 'translate(' + margin.left + ', ' + (height + margin.top) + ')')
        hGuide.selectAll('path')
            .style({ fill: 'none', stroke: "#000"})
        hGuide.selectAll('line')
            .style({ stroke: "#000"})
});
    
function type(d) {
  d.Trips = +d.Trips;
  return d;
}