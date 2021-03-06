from collections import OrderedDict
from django.db.models import Avg, F
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from .models import Page
from .serializers import PageSerializer, PageCreateSerializer, PageDetailSerializer
from .tasks import buy
from post.models import Post
from post.views import PostView
from post.serializers import PostSerializer, PostCreateSerializer
from post.renderers import MyRenderer


class PageView(GenericViewSet, ListModelMixin):
    renderer_classes = [JSONRenderer, MyRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    queryset = Page.objects.all()

    serializers = {
        'list': PageSerializer,
        'retrieve': PostSerializer,
        'create': PageCreateSerializer,
        'create_post': PostCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    def retrieve(self, request, **kwargs):
        request.last_url = request.path
        page = Page.objects.get(pk=kwargs['pk'])
        page_info = PageDetailSerializer(page, context={'request': request})

        qs = Post.objects.filter(
            page=page
        ).annotate(
            average_rate=Avg('rates__rate')
        ).order_by(
            F('average_rate').desc(nulls_first=True), '-create_date'
        )

        queryset = SearchFilter().filter_queryset(
            request,
            qs,
            PostView()
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(OrderedDict([
                ('count', self.paginator.page.paginator.count),
                ('next', self.paginator.get_next_link()),
                ('previous', self.paginator.get_previous_link()),
                ('category_info', page_info.data),
                ('results', serializer.data),
            ]))

        serializer = self.get_serializer(queryset, many=True)
        return Response(OrderedDict([
            ('category_info', page_info.data),
            ('post', serializer.data),
        ]))

    def create(self, request):
        data = request.data
        data['owners'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'page creates'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def buy(self, request, **kwargs):
        if 'Authorization' in request.COOKIES:
            buy.delay(request.user, kwargs['pk'])
            return HttpResponseRedirect(reverse('page-detail', kwargs={'pk': kwargs['pk']}))
        else:
            return HttpResponseRedirect(reverse('login'))

    @action(methods=['post'], detail=True)
    def create_post(self, request, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(reverse('page-add-media', kwargs={'pk': kwargs['pk']}))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
