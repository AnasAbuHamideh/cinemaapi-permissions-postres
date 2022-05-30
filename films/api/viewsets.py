from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )

from films.models import Film
from .serializers import FilmsSerializer
from .permissions import IsOwnerOrReadOnly

class FilmsListView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer
    


class FilmsDetailView(RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer
    permission_classes = (IsOwnerOrReadOnly, )