from rest_framework import serializers
from ShopApp.models import Category, Product
from user.models import User
from OrderApp.models import Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    #cart = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #cart = serializers.StringRelatedField(many=True, read_only=True)
    #cart = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="cart-detail")
    #cart = serializers.SlugRelatedField(many=True, read_only=True, slug_field="product")
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'created_at', 'cart_items']

"""
Serializer relations:
Relational fields are used to represent model relationships. They can be applied to ForeignKey, 
ManyToManyField and OneToOneField relationships, as well as to reverse relationships, 
and custom relationships such as GenericForeignKey.

Note: The relational fields are declared in relations.py, but by convention you should import 
them from the serializers module, using from rest_framework import serializers and refer to 
fields as serializers.<FieldName>.


Inspecting relationships.
When using the ModelSerializer class, serializer fields and relationships will be automatically 
generated for you. Inspecting these automatically generated fields can be a useful tool for 
determining how to customize the relationship style.

(.env) vandana@vandana:/media/vandana/data/Desktop/AllDjangoProjects/DRFShopCategoryAPI/ShopProject$ python3 manage.py shell
Python 3.8.6 (default, Sep 25 2020, 09:36:53) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from api.serializers import CartSerializer
>>> serializer = CartSerializer()
>>> print(repr(serializer))
CartSerializer():
    id = IntegerField(label='ID', read_only=True)
    created_at = DateTimeField(required=False)
    order_status = ChoiceField(choices=Choices(('PLACED', 'PLACED', 'Order_PLaced'), ('DRAFTED', 'DRAFTED', 'Order_in_Progress')), required=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
>>> 

"""