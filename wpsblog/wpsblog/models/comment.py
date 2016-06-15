from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Comment(models.Model):

    # 같은 어플리케이션 안에 있을 때 이렇게 부를 수 있음
    post = models.ForeignKey("Post")
    user = models.ForeignKey(User)
    content = models.TextField()

    def __str__(self):
        return "id=" + str(self.id) + ", content=" + self.content + ", post_id=" + str(self.post_id)

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "pk": self.post.id,
            },
        ) + "#comment-" + str(self.id)
