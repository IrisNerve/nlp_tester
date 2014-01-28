$(document).ready(function(){
	var token = $('#csrf').children('input').val()
	$('#article_url_form').submit(function(){
		var article_url = $('#article_url').val();
		$.post("/analyze/", {'url': article_url, 'csrfmiddlewaretoken':token}, 
			function(data){
				var elements = $(data).filter('li');
				$('#article_tags').text(data);
		});
		return false;
	});
});