from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestPosts(Feed):
    title = "Berd"
    link = "/feed"
    description = "Latest Posts"

    def items(self):
        return Post.objects.all()[:5]
