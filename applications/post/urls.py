from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostCreateView, PostListView, PostUpdateView, PostDeleteView, CommentViewSet

router = DefaultRouter()
router.register('comment', CommentViewSet)

urlpatterns = [
    path('questions-create/', PostCreateView.as_view()),
    path('questions-list/', PostListView.as_view()),
    path('question-update/<int:pk>/', PostUpdateView.as_view()),
    path('question-delete/<int:pk>/', PostDeleteView.as_view()),
    path('', include(router.urls))
]
