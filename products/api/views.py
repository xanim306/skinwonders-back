from ..models import Category,Product,Basket,OrderItem,Order,ProductComment
from django.shortcuts import get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CategorySerializer,ProductSerializer,WishlistSerializer,ProductListSerializer,NewsletterSubscribeSerializer,BasketSerializer,RemoveCartItemSerializer,BillingInfoSerializer,ShippingInfoSerializer,PaymentInfoSerializer,BasketItemSerializer,PlaceOrderSerializer,OrderListSerializer,CommentSerializer,CommentUpdateSerializer
from .paginations import CustomPagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import CustomPermission
from django.db.models import F,FloatField,DecimalField,Sum,ExpressionWrapper,Value
from django.db.models.functions import Coalesce
from django.contrib.auth import login
from rest_framework import filters
from .filters import ProductFilter
from django_filters.rest_framework.backends import DjangoFilterBackend

from ..models import Wishlist

from .serializers import WishlistSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')
    
    # def get_serializer_class(self):
    #     if self.request.method=='POST':
    #         return NewsletterSubscribeSerializer
    #     return self.serializer_class
    
    # def post(self, request, *args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     serializer = serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'message': 'Subscription successful.'}, status=201)

class EyeCareListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Eye Care").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')
    
class FeaturedListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Featured").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')
    

class MasksListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Masks").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')
    


class MoisturizersListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Moisturizers").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')
    


class NightCareListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Night Care").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')



class OnSaleListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="On Sale").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')



class SunCareListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Sun Care").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')


class TreatmentsListView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields = ('created_at','name','total_price')
    filterset_class = ProductFilter
    # filterset_fields = ['status','skintype']

    pagination_class = CustomPagination
    queryset = Product.objects.filter(category__name="Treatments").annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')



# class StatusFilterView(generics.ListAPIView):
#     serializer_class = ProductListFilterSerializer
#     # filter_backends = (DjangoFilterBackend,)
#     # filterset_class = ProductFilter

#     def get_queryset(self):
    
#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         status = self.kwargs['status']

#         return queryset.filter(status=status)




# class SkinTypeFilterView(generics.ListAPIView):
#     serializer_class = ProductListFilterSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = ProductFilter

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # skintype = self.kwargs['skintype']

#         # return queryset.filter(skintype=skintype)
#         return queryset



# class ProductNameFilterView(generics.ListAPIView):
#     serializer_class = ProductListSerializer
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     ordering_fields = ('created_at', 'name', 'total_price')
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply name filter
#         name_filter = self.kwargs.get('name', None)
#         if name_filter:
#             queryset = queryset.filter(name__icontains=name_filter)

#         return queryset
    


# class ProductPriceFilterView(generics.ListAPIView):
#     serializer_class = ProductListSerializer
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     ordering_fields = ('created_at', 'name', 'total_price')
#     # filterset_class = ProductFilter
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply price filter
#         max_price = self.kwargs.get('max_price', None)
#         min_price = self.kwargs.get('min_price', None)

#         if min_price:
#             queryset=queryset.filter(price__gte=min_price)
#         if max_price:
#             queryset=queryset.filter(price__lte=max_price)

#         return queryset
    

# class PriceAscendingFilter(generics.ListAPIView):
#     serializer_class = ProductListSerializer
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     ordering_fields = ('created_at', 'name', 'total_price')
#     # filterset_class = ProductFilter
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply price filter
#         queryset=queryset.order_by("total_price")
        
#         return queryset


# class PriceDescendingFilter(generics.ListAPIView):
#     serializer_class = ProductListSerializer
#     # filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     # ordering_fields = ('created_at', 'name', 'total_price')
#     # # filterset_class = ProductFilter
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply price filter
#         queryset=queryset.order_by("-total_price")
        
#         return queryset


# class NameAscendingFilter(generics.ListAPIView):
#     serializer_class = ProductListSerializer
#     # filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     # ordering_fields = ('created_at', 'name', 'total_price')
#     # filterset_class = ProductFilter
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply price filter
#         queryset=queryset.order_by("name")
        
#         return queryset




# class NameDescendingFilter(generics.ListAPIView):
#     serializer_class= ProductListSerializer
#     # filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     # ordering_fields = ('created_at', 'name', 'total_price')
#     # filterset_class = ProductFilter
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply price filter
#         queryset=queryset.order_by("-name")
        
#         return queryset




# class CreatedAscendingFilter(generics.ListAPIView):
#     serializer_class = ProductListSerializer
#     # filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     # ordering_fields = ('created_at', 'name', 'total_price')
#     # filterset_class = ProductFilter
#     pagination_class = CustomPagination

#     def get_queryset(self):

#         queryset = Product.objects.annotate(
#             discount_price=Coalesce('discount', 0, output_field=FloatField()),
#             total_price=F("price") - F("discount_price"),
#             discount_percent=F("discount_price") * 100 / F("price")
#         ).order_by('-created_at')

#         # Apply price filter
#         queryset=queryset.order_by("created_at")
        
#         return queryset


# class CreatedDescendingFilter(generics.ListAPIView):
    # serializer_class = ProductListSerializer
    # # filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    # # ordering_fields = ('created_at', 'name', 'total_price')
    # # # filterset_class = ProductFilter
    # pagination_class = CustomPagination

    # def get_queryset(self):

    #     queryset = Product.objects.annotate(
    #         discount_price=Coalesce('discount', 0, output_field=FloatField()),
    #         total_price=F("price") - F("discount_price"),
    #         discount_percent=F("discount_price") * 100 / F("price")
    #     ).order_by('-created_at')

    #     # Apply price filter
    #     queryset=queryset.order_by("-created_at")
        
    #     return queryset
    


class NewsletterView(generics.CreateAPIView):
    serializer_class= NewsletterSubscribeSerializer
    def post(self,request,*args,**kwargs):
            serializer = NewsletterSubscribeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message":"Subscription Successfully"},status=201)



class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (CustomPermission,)
    lookup_field="id"

    queryset = Product.objects.annotate(
            discount_price = Coalesce('discount',0,output_field = FloatField()),
            total_price=F("price")-F("discount_price"),discount_percent=F("discount_price")*100/F("price")
        ).order_by('-created_at')


    # def get_serializer_class(self):
    #     if self.request.method in ["PUT","PATCH"]:
    #         return WishlistSerializer
    #     elif self.request.method=='POST':
    #         return OrderItemSerializer
    #     return self.serializer_class
    

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def put(self,request,*args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     serializer = serializer_class(data=request.data,instance=self.get_object(), context = {"user":request.user})
    #     serializer.is_valid(raise_exception = True)
    #     serializer.save()
		
    #     return Response(serializer.data,status=200)
    


    # def post(self, request, *args, **kwargs):
    #     # Get the product instance
    #     instance = self.get_object()

    #     # Get the quantity from the request data
    #     quantity = request.data.get("quantity")
    #     serializer_class = self.get_serializer_class()
    #     serializer = serializer_class(data=request.data,instance=self.get_object())
    #     serializer.is_valid(raise_exception = True)
    #     serializer.save()


    #         # Add the product to the cart
    #     customer = request.user.profile
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     order.quantity = quantity
    #     order.save()

    #     return Response(serializer.data, status=201)
    # else:
    #     return Response({"error": "Quantity is required."}, status=400)






class BasketView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def post(self, request, id, *args, **kwargs):

        if request.user.is_authenticated:

            product = get_object_or_404(Product, id=id)

            quantity = request.data.get("quantity", 1)
            quantity=int(quantity) 

            basket_item, created = Basket.objects.get_or_create(
                user=request.user,
                product=product,
            )
        else:

            product = get_object_or_404(Product, id=id)

            quantity = request.data.get("quantity", 1)
            quantity=int(quantity) 

            basket_item, created = Basket.objects.get_or_create(
                user=None,
                session_key=request.session.session_key,
                product=product,
            )


        if not created:
            # If the basket item already exists, update the quantity
            basket_item.quantity += quantity
        else:
            # If the basket item is created for the first time, set the quantity
            basket_item.quantity = quantity

        basket_item.save()

        serializer = self.get_serializer(basket_item)
        return Response(serializer.data, status=201)
    
    # def perform_create(self, serializer):
    #     # After a user registers and logs in, you can transfer cart items associated with the session key to the user.
    #     if self.request.user.is_authenticated:
    #         session_key = self.request.session.session_key
    #         if session_key:
    #             # Transfer cart items associated with the session key to the authenticated user
    #             Basket.objects.filter(user=None, session_key=session_key).update(user=self.request.user)

    #             # Log in the user (if not already logged in)
    #             login(self.request, self.request.user)



class CartView(generics.ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user=None
        return Basket.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        subtotal_price_expr = Coalesce(Sum(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))

        total_discount_expr = Coalesce(Sum(ExpressionWrapper(F('product__discount') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))

        total_price_expr = subtotal_price_expr - total_discount_expr + Value(15, output_field=DecimalField())  # Assuming a fixed shipping price of $15

        # Evaluate the expressions to get Decimal values
        subtotal_price = queryset.aggregate(subtotal_price=subtotal_price_expr)['subtotal_price']
        total_discount_price = queryset.aggregate(total_discount_price=total_discount_expr)['total_discount_price']
        total_price = queryset.aggregate(total_price=total_price_expr)['total_price']

        serializer = BasketSerializer(queryset, many=True)

        cart_data = {
            'items': serializer.data,
            'subtotal_price': float(subtotal_price),
            'total_discount_price': float(total_discount_price),
            'shipping_price': 15.00,
            'total_price': float(total_price),
        }

        return Response(cart_data, status=200)
    



class UpdateCartItemView(generics.UpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    lookup_field = "id"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user=None
        return Basket.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user 
        else:
            user = None

        product_id = kwargs.get('id')  
        try:
            instance = Basket.objects.get(user=user, product__id=product_id)
        except Basket.DoesNotExist:
            return Response({'message': 'Item not found in the basket'}, status=404)

        quantity = request.data.get('quantity', instance.quantity)
        instance.quantity = quantity
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=200)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        subtotal_price_expr = Coalesce(Sum(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))

        total_discount_expr = Coalesce(Sum(ExpressionWrapper(F('product__discount') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))

        total_price_expr = subtotal_price_expr - total_discount_expr + Value(15, output_field=DecimalField())  # Assuming a fixed shipping price of $15
        total_price = queryset.aggregate(total_price=total_price_expr)['total_price']

        serializer = BasketItemSerializer(queryset, many=True)

        cart_data = {
            'items': serializer.data,
            'total_price': float(total_price),
        }

        return Response(cart_data, status=200)
    
      

class RemoveCartItemView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = RemoveCartItemSerializer

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user=None
        product = get_object_or_404(Product, id=id)

        
        item_exists = Basket.objects.filter(user=user, product=product).exists()
        
        if item_exists:
            Basket.objects.filter(user=user, product=product).delete()

        serializer = self.get_serializer()
        return Response(serializer.data, status=201)




class ClearCartView(generics.GenericAPIView):
    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user=None

        Basket.objects.filter(user=user).delete()
        return Response({'message': 'Cart cleared successfully'}, status=204)



class ShippingInfoView(generics.CreateAPIView):
    serializer_class = ShippingInfoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None
        return Basket.objects.filter(user=user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user=None
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = self.request.user
            request.session['shipping_details'] = serializer.data
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        subtotal_price_expr = Coalesce(Sum(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))
        total_discount_expr = Coalesce(Sum(ExpressionWrapper(F('product__discount') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))
        total_price_expr = subtotal_price_expr - total_discount_expr + Value(15, output_field=DecimalField())  

        total_price = queryset.aggregate(total_price=total_price_expr)['total_price']

        # Serialize the basket items
        serializer = BasketItemSerializer(queryset, many=True)

        cart_data = {
            'items': serializer.data,  
            'total_price': float(total_price),
        }

        return Response(cart_data, status=200)





class ShippingRemoveItemView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = RemoveCartItemSerializer

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user=None
        product = get_object_or_404(Product, id=id)

        
        item_exists = Basket.objects.filter(user=user, product=product).exists()
        
        if item_exists:
            Basket.objects.filter(user=user, product=product).delete()

        serializer = self.get_serializer()
        return Response(serializer.data, status=201)





class BillingInfoView(generics.ListAPIView):
    serializer_class = BillingInfoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None
        return Basket.objects.filter(user=user)


    # def perform_create(self, serializer):
    #     # Set the user field based on the authenticated user
    #     serializer.save(user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     # Serialize and store billing details data in the session
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         request.session['billing_details'] = serializer.data
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        subtotal_price_expr = Coalesce(Sum(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))
        total_discount_expr = Coalesce(Sum(ExpressionWrapper(F('product__discount') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))
        total_price_expr = subtotal_price_expr - total_discount_expr + Value(15, output_field=DecimalField())  

        total_price = queryset.aggregate(total_price=total_price_expr)['total_price']

        # Serialize the basket items
        serializer = BasketItemSerializer(queryset, many=True)

        cart_data = {
            'items': serializer.data,  
            'total_price': float(total_price),
        }

        return Response(cart_data, status=200)



class BillingRemoveItemView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = RemoveCartItemSerializer

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user=None
        product = get_object_or_404(Product, id=id)

        
        item_exists = Basket.objects.filter(user=user, product=product).exists()
        
        if item_exists:
            Basket.objects.filter(user=user, product=product).delete()

        serializer = self.get_serializer()
        return Response(serializer.data, status=201)



    


class PaymentInfoView(generics.CreateAPIView):
    serializer_class = PaymentInfoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None
        return Basket.objects.filter(user=user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user=None
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = self.request.user
            request.session['payment_details'] = serializer.data
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        subtotal_price_expr = Coalesce(Sum(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))
        total_discount_expr = Coalesce(Sum(ExpressionWrapper(F('product__discount') * F('quantity'), output_field=DecimalField()), output_field=DecimalField()), Value(0, output_field=DecimalField()))
        total_price_expr = subtotal_price_expr - total_discount_expr + Value(15, output_field=DecimalField())  

        total_price = queryset.aggregate(total_price=total_price_expr)['total_price']

        serializer = BasketItemSerializer(queryset, many=True)

        cart_data = {
            'items': serializer.data,  
            'total_price': float(total_price),
        }

        return Response(cart_data, status=200)





class PaymentRemoveItemView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = RemoveCartItemSerializer

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user=None
        product = get_object_or_404(Product, id=id)

        
        item_exists = Basket.objects.filter(user=user, product=product).exists()
        
        if item_exists:
            Basket.objects.filter(user=user, product=product).delete()

        serializer = self.get_serializer()
        return Response(serializer.data, status=201)


    
    

class PlaceOrderView(generics.CreateAPIView):
    serializer_class=PlaceOrderSerializer

    def create(self, request, *args, **kwargs):
        shipping_details = request.session.get('shipping_details')
        # billing_details = request.session.get('billing_details')
        payment_details = request.session.get('payment_details')
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        basket_items = Basket.objects.filter(user=user)
        if not basket_items.exists():
            return Response({'message': 'Your basket is empty'}, status=400)
        
        order = None
        if request.user.is_authenticated:
            if shipping_details and payment_details:
                order = Order.objects.create(
                    user=request.user,  
                    complete=True,
                )

                shipping_serializer = ShippingInfoSerializer(data=shipping_details)
                if shipping_serializer.is_valid():
                    shipping = shipping_serializer.save(user=user)
                    order.shipping_info = shipping
                    billing_serializer = BillingInfoSerializer(data=shipping_details)
                    if billing_serializer.is_valid():
                        billing = billing_serializer.save(user=user)
                        order.billing_info = billing

                else:
                    return Response(
                        {'message': 'Invalid shipping details data'},
                        status=400,
                    )
    
                payment_serializer = PaymentInfoSerializer(data=payment_details)
                if payment_serializer.is_valid():
                    payment = payment_serializer.save(user=user)
                    order.payment_info = payment
                else:
                    return Response(
                        {'message': 'Invalid payment details data'},
                        status=400,
                    )

            else:
                return Response({"message":"You have to fill shipping and payment details"},status=400)


            if order is not None:
                total_quantity = sum([item.quantity for item in basket_items])
                order.quantity = total_quantity
                order.save()
                for basket_item in basket_items:
                    order_item = OrderItem.objects.create(
                        order=order,
                        product=basket_item.product,
                        quantity=basket_item.quantity,
                    )
                    order_item.save()

                order.items.add(*OrderItem.objects.filter(order=order))
                basket_items.delete()

                request.session.pop('shipping_details', None)
                request.session.pop('payment_details', None)

                return Response({'message': 'Order placed successfully'})

        else:
            if shipping_details and payment_details:
                order = Order.objects.create(
                    user=None, 
                    complete=True,
                    session_key=request.session.session_key,
                )

                shipping_serializer = ShippingInfoSerializer(data=shipping_details)
                if shipping_serializer.is_valid():
                    shipping = shipping_serializer.save(user=None)
                    order.shipping_info = shipping
                    billing_serializer = BillingInfoSerializer(data=shipping_details)
                    if billing_serializer.is_valid():
                        billing = billing_serializer.save(user=None)
                        order.billing_info = billing

                else:
                    return Response(
                        {'message': 'Invalid shipping details data'},
                        status=400,
                    )
    
                payment_serializer = PaymentInfoSerializer(data=payment_details)
                if payment_serializer.is_valid():
                    payment = payment_serializer.save(user=None)
                    order.payment_info = payment
                else:
                    return Response(
                        {'message': 'Invalid payment details data'},
                        status=400,
                    )
            else:
                return Response({"message":"You have to fill shipping and payment details"},status=400)

            if order is not None:
                total_quantity = sum([item.quantity for item in basket_items])
                order.quantity = total_quantity
                order.save()
                for basket_item in basket_items:
                    order_item = OrderItem.objects.create(
                        order=order,
                        product=basket_item.product,
                        quantity=basket_item.quantity,
                    )
                    order_item.save()

                order.items.add(*OrderItem.objects.filter(order=order))
                basket_items.delete()

                request.session.pop('shipping_details', None)
                request.session.pop('payment_details', None)

                return Response({'message': 'Order placed successfully'})
        
        return Response({'message': 'Invalid request'}, status=400)
    



class OrderListItemView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_queryset(self):
            if self.request.user.is_authenticated:
                user = self.request.user
            else:
                user = None
            
            return Order.objects.filter(user=user)
         


    



class WishlistAddItemView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, id=id)

            wishlist_item = None
            
            item_exists = Wishlist.objects.filter(user=request.user, products=product).exists()
            
            if not item_exists:
                wishlist_item, created = Wishlist.objects.get_or_create(
                    user=request.user,
                    products=product,
                )
            else:
                Wishlist.objects.filter(user=request.user, products=product).delete()
        else:
            product = get_object_or_404(Product, id=id)
            wishlist_item = None

            item_exists = Wishlist.objects.filter(user=None, products=product,session_key=request.session.session_key).exists()

            if not item_exists:
                wishlist_item, created = Wishlist.objects.get_or_create(
                    user=None,
                    products=product,
                    session_key=request.session.session_key,
                )
            else:
                Wishlist.objects.filter(user=None, products=product,session_key=request.session.session_key).delete()


        serializer = self.get_serializer(wishlist_item)
        return Response(serializer.data, status=201)



class WishlistListItemView(generics.ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
            if self.request.user.is_authenticated:
                user = self.request.user
            else:
                user = None
            
            return Wishlist.objects.filter(user=user)
         

    

class WishlistListRemoveItemView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def post(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, id=id)

            wishlist_item = None
            
            item_exists = Wishlist.objects.filter(user=request.user, products=product).exists()
            
            if  item_exists:
                Wishlist.objects.filter(user=request.user, products=product).delete()

        else:
            product = get_object_or_404(Product, id=id)
            wishlist_item = None

            item_exists = Wishlist.objects.filter(user=None, products=product,session_key=request.session.session_key).exists()

            if  item_exists:
                Wishlist.objects.filter(user=None, products=product,session_key=request.session.session_key).delete()


        serializer = self.get_serializer(wishlist_item)
        return Response(serializer.data, status=201)



class CommentView(generics.CreateAPIView):
    queryset = ProductComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=(IsAuthenticated,)


    def post(self, request, id, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Product, id=id)

        user = self.request.user
        email = self.request.user.email
        session_key=None

        # Pass the product to the serializer's create method
        comment = serializer.save(product=product,user=user,session_key=session_key,email=email)

        return Response(CommentSerializer(comment).data, status=200)




class CommentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductComment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return ProductComment.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        user = request.user
        comment_id = kwargs.get('id')

        try:
            instance = ProductComment.objects.get(user=user, id=comment_id)  
        except ProductComment.DoesNotExist:
            return Response({'message': 'You cannot edit someone else comment'}, status=404)

        instance.comment = request.data.get('comment')
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=200)