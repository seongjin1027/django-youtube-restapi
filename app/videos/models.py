from django.db import models
from common.models import CommonModel
from users.models import User

# - title
# - description
# - link
# - views_count
# - thumbnail
# - video_file: link
# - User: FK

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 Bucker -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # upload_to'저장경로'

    user = models.ForeignKey(User, on_delete=models.CASCADE) #운영단에서의 문제


# User : Video => 1 : N => 부모:자녀(FK)
    # => User : Video, Video, Video ... => O
    # => Video : User, User, User ... => X