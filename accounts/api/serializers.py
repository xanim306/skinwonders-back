
from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from services.generators import CodeGenerator
from ..models import Profile
from ..generators import get_unique_code
User = get_user_model()

#registerde actvationu uuid ile yoxlamaq ucun 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import smart_str,smart_bytes



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={"input_type":"password"})

    class Meta:
        model = User
        fields = ('email','password')
    

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")

        return authenticate(email=email,password=password)
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_['tokens'] = { "refresh":str(token),"access":str(token.access_token)}
        return repr_
    

    def validate(self,attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email,password=password)
        
        if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError({"error":"This email does not exist"})
        
        if not User.objects.get(email=email).is_active:
            raise serializers.ValidationError({"error":"Account is not activated.Please activate your account to log in"})
        
        if not user:
            raise serializers.ValidationError({"error":"Email or password is wrong"})                
        
        return super().validate(attrs)
    




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    password_confirm = serializers.CharField(write_only=True, style={"input_type": "password"})
    email_confirm = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ("email","email_confirm", "name","surname", "password", "password_confirm","age","country",)


    def validate(self, attrs):
        email = attrs.get("email").strip()
        email_confirm = attrs.get("email_confirm").strip()
        password = attrs.get("password").strip()
        password_confirm = attrs.get("password_confirm").strip()

        if len(password)<6:
            raise serializers.ValidationError({"error":"length must be bigger than 6"})
        
        if not any(i.isdigit()for i in password):
            raise serializers.ValidationError({"error":"At least a character has to be involved"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "This email already exists"})

        if email != email_confirm:
            raise serializers.ValidationError({"error": "Emails don't match"})

        if password != password_confirm:
            raise serializers.ValidationError({"error": "Passwords don't match"})
        
        return attrs

    def create(self, validated_data):
        password_confirm =validated_data.pop("password_confirm")
        email_confirm = validated_data.pop("email_confirm") 
        # email = validated_data.get("email", None)
        # name = validated_data.get("name", None)
        # surname = validated_data.get("surname", None)
        password = validated_data.get("password")

        user = User.objects.create(
            **validated_data, is_active=False,
        )
        user.set_password(password)
        user.save()

        user.profile.activation_code = get_unique_code(size=6,model_=Profile)
        user.profile.save()

        # sending mail
        message = f"Please write code below: \n{user.profile.activation_code}"
        send_mail(
            'Activate email', # subject
            message, # message
            settings.EMAIL_HOST_USER, # from email
            [user.email], # to mail list
            fail_silently=False,
        )

        return user


    # def to_representation(self, instance):
    #     repr_ = super().to_representation(instance)
    #     repr_["slug"] = instance.slug
    #     return repr_
    
#registerde actvationu uuid ile yoxlamaq ucun 
    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["slug"] = instance.slug
        repr_["uuid"] = urlsafe_base64_encode(smart_bytes(instance.id))
        return repr_
    
    


class ActivationSerializer(serializers.Serializer):
    code = serializers.CharField(write_only = True)


    class Meta:
        model = User
        fields = ("code",)

    def validate(self, attrs):
        user = self.context.get("user")
        code = attrs.get("code").strip()

        if str(code)!=str(user.profile.activation_code):
            raise serializers.ValidationError({"error":"code is wrong"})
        return attrs

    def create(self, validated_data):
        user = self.context.get("user")
        user.is_active = True
        user.save()

        user.profile.activation_code = None
        user.profile.save()

        return user


    def to_representation(self, instance):    
        repr_ = super().to_representation(instance)
        repr_['email'] = instance.email
        token = RefreshToken.for_user(instance)
        repr_['tokens'] = { "refresh":str(token),"access":str(token.access_token)}
        return repr_




class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", )

    def validate(self, attrs):
        email = attrs.get("email")

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "There is no user with this e-mail address"})

        return attrs


class ResetPasswordCompleteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ('password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"error": "Password fields didn't match"})

        return attrs
    


class ResetActivationSerializer(serializers.ModelSerializer):
    res_code=serializers.CharField()




class ProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name")
    user_surname = serializers.CharField(source="user.surname")
    user_age = serializers.IntegerField(source="user.age")
    user_country = serializers.CharField(source="user.country")
    user_image = serializers.ImageField(source="user.image")
    user_id = serializers.SlugField(source="user.id")

    class Meta:
        model = Profile
        fields = ("user_name","user_surname","user_age","user_country","user_image","user_id")




class ProfileUpdateSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source="user.name", required=False)
    user_surname = serializers.CharField(source="user.surname", required=False)
    user_age = serializers.IntegerField(source="user.age", required=False)
    user_country = serializers.CharField(source="user.country", required=False)
    user_image = serializers.ImageField(source="user.image",required=False)

    class Meta:
        model = Profile
        fields = ("user_name","user_surname","user_age","user_country","user_image")


    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class PasswordChangeSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})    
    password_confirm = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})    
    class Meta:
        model = User
        fields = ("password","password_confirm","current_password")

    def validate(self, attrs):
        current_password = attrs.get("current_password").strip()
        password = attrs.get("password").strip()
        password_confirm = attrs.get("password_confirm").strip()
        email = self.context.get("email")

        user = authenticate(email=email,password=current_password)
        
        if len(password)<6:
            raise serializers.ValidationError({"error":"length must be bigger than 6"})
        
        if not any(i.isdigit()for i in password):
            raise serializers.ValidationError({"error":"At least a character has to be involved"})

        if password==current_password:
            raise serializers.ValidationError({"error":"current and new password can't be same"})

        if password != password_confirm:
            raise serializers.ValidationError({"error": "Passwords don't match"})
        
        if not user:
            raise serializers.ValidationError({"error":"Old password is wrong"})
        
        return attrs
    

    def create(self, validated_data):
        password_confirm =validated_data.pop("password_confirm")
        current_password = validated_data.pop("current_password")
        password = validated_data.get("password")

        user = User.objects.create(
            **validated_data,
        )
        user.set_password(password)
        user.save()

        return user
    


