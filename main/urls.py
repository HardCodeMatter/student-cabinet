from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/update/', views.profile_update, name='profile_update'),

    path('course/', views.course_view, name='course_view'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:id>/update/', views.course_update, name='course_update'),
    path('course/<int:id>/delete/', views.course_delete, name='course_delete'),

    path('course/<int:course_id>/<int:student_id>/point/', views.course_set_point, name='course_set_point'),
    path('course/list/', views.course_list, name='course_list'),
    path('course/<int:id>/add/', views.course_add, name='course_add'),

    path('course/grades/', views.course_grade_list, name='course_grade_list'),
]
