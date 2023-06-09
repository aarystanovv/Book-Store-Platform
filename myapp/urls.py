from django.contrib import admin
from django.urls import *
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm

urlpatterns = [
    path('support/', views.support, name="support"),
    path('', views.home, name="home"),
    path('account/', views.account),
    path('cart/', views.cart, name="cart"),
    path('home/', views.home, name="home"),
    path('products/', views.product, name="products"),
    path('details/<int:id>/', views.details),
    path('comm/', views.comm),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('admins/<slug:post_slug>', views.admins),
    path('car/', views.cart_buy),
    path('dele/<int:id>', views.dele),
    path('AdminUser', views.AdminUser, name='AdminUser'),
    path('all/', views.all, name='all'),
    path('allUsers/', views.allUsers, name='all'),
    path('insert/', views.insert, name='insert'),
    path('insertUsers/', views.insertUsers, name='insert'),
    path('<int:pk>/updateItems', views.updateItems, name='updateItems'),
    path('<int:pk>/deleteItems', views.deleteItems, name='deleteItems'),
    path('<int:id>/detail', views.detail, name='detail'),
    path('allForClients', views.allForClients, name='allForClients'),
    path('profile1', views.profile, name='profile1'),
    path('UU', views.UU, name='UU'),
    path('allEdit', views.allEdit, name='allEdit'),
    path('<int:pk>/edit1', views.edit1, name='edit1'),
    path('search_books', views.search_books, name='search_books'),
    path('AdminUser/<int:pk>/delete', views.updateOnlyUser, name='updateOnlyUser'),
    path('item_list', views.item_list, name='item_list'),
    path('wikipedia', views.wiki, name='wikipedia'),
    path('sendemail/', views.contactsendmail, name='contactpage'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html',
                                                                     authentication_form=LoginForm), name='login'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
