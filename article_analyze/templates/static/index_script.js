$(document).ready(function(){
	// CSRF token for all post calls
	var token = $('#csrf').children('input').val()
	
	// Analyze article URL
	$('#article_url_form').submit(function(){
		var article_url = $('#article_url').val();
		$.post("/analyze/", {'url': article_url, 'csrfmiddlewaretoken':token}, 
			function(data){
				$('div.article_tags').html(data);
		});
		return false;
	});


});