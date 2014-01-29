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

	$('#tag_vote_form').live('submit', function(){
		var tag_ids = []
		$('#tag_vote_form :checked').each(function(){
			tag_ids.push($(this).val());
		});

		$.post('/upvote/', {'tag_ids': tag_ids.join(), 'csrfmiddlewaretoken':token}, function(data){
			$('#article_tags').text('Thanks for voting!');
			return false;
		});
		return false;
	});

});