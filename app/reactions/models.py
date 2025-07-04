from django.db import models
from common.models import CommonModel

# - User: Fk
# - video: FK
# - reaction (like, dislike, cancel) => 실제 youtube rest api

# User : Reaction => User : Reaction, Reaction, Reaction => 1:N(FK)
# video : Reaction => Video : Reaction, Reaction, Reaction => 1:N(FK)

class Reaction(CommonModel):
    # user = models.ForeignKey(User) # Circular Import Error
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'like'),
        (DISLIKE, 'dislike'),
        (NO_REACTION, 'no reaction')
    )
    # LIKE(1), DISLIKE(-1), NO_REACTION(0)
    reaction = models.TextField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )
