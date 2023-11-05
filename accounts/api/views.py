from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
from .serializers import LoginSerializer,RegisterSerializer,ActivationSerializer,ResetPasswordSerializer,ResetPasswordCompleteSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from django.urls import reverse_lazy

####
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import smart_str,smart_bytes


User = get_user_model()



class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ActivationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ActivationSerializer
    # lookup_field = "slug"
    lookup_field = "uuid"

    def get_object(self,*args, **kwargs):
        uuid = self.kwargs.get("uuid")
        id = smart_str(urlsafe_base64_decode(uuid))

        return User.objects.get(id=id)


    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={"user":self.get_object()})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



    # def put(self,request,*args,**kwargs):
    #     obj = self.get_object()
    #     data = {}

    #     if obj.activation_code == request.data.get("code"):
    #         obj.is_active = True
    #         obj.activation_code = None
    #         obj.save()
    #         token = RefreshToken.for_user(obj)
    #         data["email"]=obj.email
    #         data["token"] = {"refresh": str(token), "access": str(token.access_token)}
    #         return Response(data, status=201)
    #     else:
    #         return Response({"error": "Wrong code"})
        


class ResetPasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class= ResetPasswordSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_email = serializer.validated_data.get("email")
        user = User.objects.get(email = user_email)


        link = request.build_absolute_uri(reverse_lazy("accounts-api:reset_password_complete", kwargs={"slug": user.slug}))

        subject = 'Reset Password'
        message = f'You can verify your account by clicking the link below: \n {link}'

        send_mail(
            subject,  # subject
            message,  # message
            settings.EMAIL_HOST_USER,  # from mail
            [user.email],  # to mail
            fail_silently=False,
        )

        return Response(serializer.data, status=201)


class ResetPasswordCompleteView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordCompleteSerializer
    lookup_field = "slug"

    def put(self, request, *args, **kwargs):
        user = self.get_object()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data.get('password'))
        user.save()

        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)

        token_data = {"email": user.email}

        token = RefreshToken.for_user(user)
        token_data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}

        return Response({**token_data})