from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework import permissions
from ShopApp.models import Category, Product
from OrderApp.models import Cart, CartItem
from user.models import User
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

"""User APIs"""
class UserListAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [IsAdminUser]

    """queryset - The queryset that should be used for returning objects from this view. 
    Typically, you must either set this attribute, or override the get_queryset() method. 
    If you are overriding a view method, it is important that you call get_queryset() 
    instead of accessing this property directly, as queryset will get evaluated once, 
    and those results will be cached for all subsequent requests."""

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # """get_queryset(self) returns the queryset that should be used for list views, 
    # and that should be used as the base for lookups in detail views. """
    # def get_queryset(self):
    #     user = self.request.user
    #     return user.accounts.all()


class SingleUserAPI(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]


"""Category APIs"""
class CreateCategoryAPIView(CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def create_category(self, serializer):
    #     category = get_object_or_404(Category, id=self.request.data.get('category_id'))
    #     return serializer.save(category=category)


class SingleCategoryRetrieveAPIView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #def get(self, request, *args, **kwargs):
    #    category = Category.objects
    #    serializer = CategorySerializer(category, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdateAPIView(UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategoryAPIView(DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


"""Product APIs"""
class CreateProductAPIView(CreateAPIView):
    # permission_class = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SingleProductRetrieveAPIView(RetrieveAPIView):
    # permission_class = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    # def get(self, request, *args, **kwargs):
    #     product = Product.objects
    #     serializer = ProductSerializer(product, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class ProductUpdateAPIView(UpdateAPIView):
    # permission_class = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductAPIView(DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


"""Cart APIs"""
class CreateCartAPI(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class SingleCartAPI(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    

class ViewCartAPI(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class UpdateCartAPI(UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DeleteCartAPI(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


"""CartItem APIs"""
class CreateCartItemAPI(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ViewCartItemAPI(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class UpdateCartItemAPI(UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class DeleteCartItemAPI(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer