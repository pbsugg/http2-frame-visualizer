$(document).ready(function(){
	
	$("#makeRequest").click(function(){
		$.ajax({
			url: "/http2",
			type: "POST",
		})
		.done(function(json){
		$("<p>").text(json.title)
		})
	})
})
		
