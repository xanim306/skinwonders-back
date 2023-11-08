from django.urls import path
from . import views

app_name='products-api'



urlpatterns = [
    path('categories/',views.CategoryView.as_view(),name='category'),
    path('list/',views.ProductListView.as_view(),name='list'),
    path('news/',views.NewsletterView.as_view(),name='news'),
    path("detail/<int:id>/", views.ProductDetailView.as_view(), name="detail"),
                                            ###Comment###
    path("detail/comment/<int:id>/",views.CommentView.as_view(), name="comment"),
    path("detail/comment/update/<int:id>/",views.CommentUpdateView.as_view(), name="comment-update"),
                                        ####wishlist#####
    path('wishlist/add/remove/<int:id>/', views.WishlistAddItemView.as_view(), name='wishlist-add-remove'),
    path('wishlist/list/', views.WishlistListItemView.as_view(), name='wishlist-list'),      
    path('wishlist/list/remove/<int:id>/', views.WishlistListRemoveItemView.as_view(), name='wishlist-remove'),      
                                        ####basket####
    path("add/basket/<int:id>/", views.BasketView.as_view(), name="add_basket"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path('update-cart-item/<int:id>/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('remove-cart-item/<int:id>/', views.RemoveCartItemView.as_view(), name='remove_cart_item'),
    path('clear-cart/', views.ClearCartView.as_view(), name='clear_cart'),
    path('order/list/', views.OrderListItemView.as_view(), name='order-list'),  
                                        #####checkout####
    path('shipping-info/', views.ShippingInfoView.as_view(), name='shipping_info'),
    path('shipping-item-remove/<int:id>/',views.ShippingRemoveItemView.as_view(),name='shipping-item-remove'),
    path('billing-info/', views.BillingInfoView.as_view(), name='billing-info'),
    path('billing-item-remove/<int:id>/',views.BillingRemoveItemView.as_view(),name='billing-item-remove'),
    path('payment-info/', views.PaymentInfoView.as_view(), name='payment-info'),
    path('payment-item-remove/<int:id>/',views.PaymentRemoveItemView.as_view(),name='payment-item-remove'),
    path('place/order/', views.PlaceOrderView.as_view(), name='place-order'),

]







