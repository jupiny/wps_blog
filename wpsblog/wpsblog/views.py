import requests
import json

from django.http.response import HttpResponse

# MVC Controller
def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
	# 방 번호 ( room_id) 직방의 데이터를 그대로 보여주는 뷰(컨트롤러)
	url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
	response = requests.get(url)
	return HttpResponse(
		response.content,
		content_type="application/json",
	)

def news(request):

	search = request.GET.get('search')
	response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
	news_dict = json.loads(response.text)
	news_list = news_dict.get("news")

	form_html = """
		<form method="GET" action="/news/">
			<input type="text" name="search">
			<input type="submit" value="검색">
		</form>
	"""

	if search:
		news_list = list(filter(
				lambda news: search in news.get('title'),
				news_list,
		))
	content = "<h1>News</h1>" +\
			   "<p>This is news page.</p>" +\
			   "".join([
					   "<h2>{title}</h2><img src={image_url}><p>{content}</p>".format(
						   title=news.get("title"),
						   image_url=news.get('image'),
						   content=news.get('content'),
						   )
					   for news in news_list
					   ])
	return HttpResponse(form_html + content)
