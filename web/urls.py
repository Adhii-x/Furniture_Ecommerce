from django.urls import path

from . import views
from .views import CreateStripeCheckoutSessionView

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("login", views.user_login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("cart/add/<int:id>/", views.cart_add, name="cart_add"),
    path("cart/item_clear/<int:id>/", views.item_clear, name="item_clear"),
    path("cart/item_increment/<int:id>/", views.item_increment, name="item_increment"),
    path("cart/item_decrement/<int:id>/", views.item_decrement, name="item_decrement"),
    path("cart/cart_clear/", views.cart_clear, name="cart_clear"),
    path("cart/cart-details/", views.cart_detail, name="cart_details"),
    path("checkout", views.checkout, name="checkout"),
    path("placeorder", views.placeorder, name="placeorder"),
    path(
        "create-checkout-session",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
]
