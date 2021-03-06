from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.response import Response

from .filters import CaseInsensitiveOrderingFilter
from .serializers import ArtistSerializer, SongSerializer, RegisterSerializer, UserSerializer, ProposalSerializer, \
    FeedbackSerializer
from .models import Artist, Song, Proposal, Feedback


class ArtistView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_backends = [CaseInsensitiveOrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name']
    ordering = ['name']
    filterset_fields = ['id']


class SongView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SongSerializer
    queryset = Song.objects.all().prefetch_related('artist', 'featuring_artist')
    filter_backends = [CaseInsensitiveOrderingFilter, DjangoFilterBackend, SearchFilter]
    ordering_fields = ['title', 'created_at', 'artist__name']
    filterset_fields = ['artist', 'featuring_artist']
    search_fields = ['title__unaccent', 'artist__name__unaccent', 'featuring_artist__name__unaccent']


class ProposalView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()
    ordering_fields = ['created_at']
    filterset_fields = ['created_by', 'rejected', 'song']


class FeedbackView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all().prefetch_related('created_by')
    filterset_fields = ['created_by', 'treated']


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class UserView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']


class RetrieveCurrentUserView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)
