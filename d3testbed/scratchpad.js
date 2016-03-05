.attr("x", function(d, i) {
   var cumulative_x_offset = 0;
   for (var x = 0; x <= i; x++){
     cumulative_x_offset += scale(dataset[i])
   }
   return(cumulative_x_offset + scale(d));
})

var array_sum = function(array, i){
    if (i == 0){
      return(array[0])
    }
    else{
      return(d3.sum(array.slice(0, (i+1))))
    }
}
