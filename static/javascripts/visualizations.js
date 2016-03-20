

dataset = [ 20, 8144, 4096, 400, 2]


var svgContainer = d3.select("body")
.append("svg")
.attr("height","1500")
.attr("width","1500")

var min = d3.min(dataset)
var max = d3.max(dataset)

var scale = d3.scale.log()
            .domain([min, max])
            .range([50, 200])

var rectangles = svgContainer.selectAll("rect")
.data(dataset)
.enter()
.append("rect")


//Refactor this hack--no global vars!!
cumulative_x_offset = 0
spacing = 0
// All four values will be affected by this scale
rectangles.attr("width", function(d) {
             return(scale(d))
          })
          .attr("x", function(d, i) {
             var offset = cumulative_x_offset + spacing
             cumulative_x_offset += scale(d)
             spacing += 10
             return(offset)
          })
          .attr("y", function(d) {
             return(200 - (scale(d)/2))
          })
          .attr("height", function(d) {
             return(scale(d))
          })
          .attr("padding","2")
	  .attr("fill", "#eddc6d")
