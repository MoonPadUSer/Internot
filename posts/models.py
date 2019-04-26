from django.db import models
from django.utils import timezone

import datetime

class Post(models.Model):
    post_content = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    post_user_id = models.IntegerField()
    private = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    comment = models.BooleanField(default=False)
    parent_id = models.IntegerField(default=-1)


    def is_comment(self):
        return self.comment

    def get_parent_id(self):
        if self.is_comment():
            return self.parent_id
        else:
            return -1

    def is_private(self):
        return self.private

    def vote_count(self):
        return self.votes

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"
