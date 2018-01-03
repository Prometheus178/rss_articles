
from django.contrib.syndication.views import Feed
from articlesfeed.models import *

class ArticlesFeed(Feed):
    title = "EVILEG - Practic programmers"
    description = "Last article site EVILEG about programmers and IT"
    link = "articles/"

    def items(self):
        return Article.objects.exclude(article_status=False).order_by('-article_date')[:10]

    def item_title(self, item):
        return item.article_title

    def item_description(self, item):
        return item.article_content[0:400] + "<p>Article first be on - Practic programmers</p>"
