from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('contractor/<int:road_id>/', views.contractor, name='contractor'),
    path('engineer/<int:road_id>/', views.engineer, name='engineer'),
    path('administrator/<int:road_id>/', views.administrator, name='administrator'),
    
    # path('register/', views.register_page, name='register'),
    # path('logout/', views.logout_page, name='logout'),
    # path('profile/', views.profile_page, name='profile'),
    # path('change_password/', views.change_password_page, name='change_password'),
    # path('forgot_password/', views.forgot_password_page, name='forgot_password'),
    # path('reset_password/', views.reset_password_page, name='reset_password'),
    # path('dashboard/', views.dashboard_page, name='dashboard'),
    # path('add_user/', views.add_user_page, name='add_user'),
    # path('edit_user/<int:id>/', views.edit_user_page, name='edit_user'),
    # path('delete_user/<int:id>/', views.delete_user_page, name='delete_user'),
    # path('add_role/', views.add_role_page, name='add_role'),
    # path('edit_role/<int:id>/', views.edit_role_page, name='edit_role'),
    # path('delete_role/<int:id>/', views.delete_role_page, name='delete_role'),
    # path('add_permission/', views.add_permission_page, name='add_permission'),
    # path('edit_permission/<int:id>/', views.edit_permission_page, name='edit_permission'),
    # path('delete_permission/<int:id>/', views.delete_permission_page, name='delete_permission'),
    # path('add_group/', views.add_group_page, name='add_group'),
    # path('edit_group/<int:id>/', views.edit_group_page, name='edit_group'),
    # path('delete_group/<int:id>/', views.delete_group_page, name='delete_group'),
    # path('add_menu/', views.add_menu_page, name='add_menu'),
    # path('edit_menu/<int:id>/', views.edit_menu_page, name='edit_menu'),
    # path('delete_menu/<int:id>/', views.delete_menu_page, name='delete_menu'),
    # path('add_sub_menu/', views.add_sub_menu_page, name='add_sub_menu'),
    # path('edit_sub_menu/<int:id>/', views.edit_sub_menu_page, name='edit_sub_menu'),
    # path('delete_sub_menu/<int:id>/', views.delete_sub_menu_page, name='delete_sub_menu'),
    # path('add_sub_menu_item/', views.add_sub_menu_item_page, name='add_sub_menu_item'),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

