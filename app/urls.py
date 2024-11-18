from django.urls import path
from .views import (
    UserListCreateView, UserDetailView,
    CourseListCreateView, CourseDetailView,
    SectionListCreateView, SectionDetailView,
    ContentListCreateView, ContentDetailView,
    EnrollmentListCreateView, EnrollmentDetailView,
    ReviewListCreateView, ReviewDetailView,
    QuizListCreateView, QuizDetailView,
    QuestionListCreateView, QuestionDetailView,
)

urlpatterns = [
    # User URLs
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    # Course URLs
    path('courses/', CourseListCreateView.as_view(), name='course_list_create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),

    # Section URLs
    path('sections/', SectionListCreateView.as_view(), name='section_list_create'),
    path('sections/<int:pk>/', SectionDetailView.as_view(), name='section_detail'),

    # Content URLs
    path('contents/', ContentListCreateView.as_view(), name='content_list_create'),
    path('contents/<int:pk>/', ContentDetailView.as_view(), name='content_detail'),

    # Enrollment URLs
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment_list_create'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),

    # Review URLs
    path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),

    # Quiz URLs
    path('quizzes/', QuizListCreateView.as_view(), name='quiz_list_create'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),

    # Question URLs
    path('questions/', QuestionListCreateView.as_view(), name='question_list_create'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
]
