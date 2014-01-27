$(document).ready(function(){
	var token = $('#csrf').children('input').val()
	$('#article_url_form').submit(function(){
		var article_url = $('#article_url').val();
		$.post("/analyze/", {'url': article_url, 'csrfmiddlewaretoken':token}, 
			function(data){
				$('#article_text').text(data);
		});
		return false;
	});
});