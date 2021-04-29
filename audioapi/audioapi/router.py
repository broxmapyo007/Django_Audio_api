from audioapp.viewsets import SongsViewset,PodcastViewset,AudiobookViewset,ParticipantViewset
from rest_framework import routers

router1 = routers.DefaultRouter()
router1.register('song',SongsViewset)


router2 = routers.DefaultRouter()
router2.register('podcast',PodcastViewset)
router2.register('participant',ParticipantViewset)

router3 = routers.DefaultRouter()
router3.register('audiobook',AudiobookViewset)
