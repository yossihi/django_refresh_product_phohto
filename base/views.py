from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status



class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=ProductSerializer(data=request.data)
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        return Product.objects.create(**validated_data, user=user)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        # ...


        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myProducts(req):
    user = req.user
    all_products = ProductSerializer(user.product_set.all(), many=True).data
    return Response(all_products)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProducts(req):
    print(req.data)
    prod_seri = ProductSerializer(data=req.data, context= {'user': req.user})
    if prod_seri.is_valid():
        prod_seri.save()
        return Response('added succefuly')
    else:
        return Response('faild')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProd(req, id):
    try:
            temp_task=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response ("not found")    
    
    temp_task.delete()
    return Response ("del...")