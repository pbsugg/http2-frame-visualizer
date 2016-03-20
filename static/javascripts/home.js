$(document).ready(function(){
	
	$("#makeRequest").click(function(){
		$.ajax({
			url: "/start",
			type: "GET",
			dataType:"json",
		})
		.done(function(json){
		$("<p>").text(json.title)
		})
	})
})
		
