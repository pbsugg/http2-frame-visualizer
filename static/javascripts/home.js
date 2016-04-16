$(document).ready(function(){
	
	$("#makeRequest").click(function(){
		$.ajax({
			url: "/http2",
			type: "GET",
			dataType:"json",
		})
		.done(function(json){
		$("<p>").text(json.title)
		})
	})
})
		
