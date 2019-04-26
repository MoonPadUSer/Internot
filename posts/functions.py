from . import views
from .models import Post


def add_new_post(content, date, user_id, private, comment, parent_id=-1):
    post = Post(post_content=content, pub_date=date, post_user_id=user_id, private=private, votes=0, comment=comment, parent_id=parent_id)
    post.save()