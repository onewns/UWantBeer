from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:beer_id>', views.createReview), #리뷰 생성
    path('<int:review_id>/edit/', views.editReview), #리뷰 수정
    path('<int:review_id>/delete/', views.deleteReview), #리뷰 삭제
    path('all/', views.getAllReview), #전체 리뷰 출력
    path('<int:review_id>/', views.getReview), #review_id에 해당하는 리뷰 출력
    path('<int:beer_id>/all', views.getReviewByBeer), #특정 맥주의 모든 리뷰 출력
    path('user/<int:user_id>/', views.getReviewByAuthor) #특정 유저의 모든 리뷰 출력
]