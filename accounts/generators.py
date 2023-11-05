import random
import string

# from django.contrib.auth import get_user_model

# User = get_user_model()

# #to try this code open shell and import Generator from accounts.generator  and to run it type
# #Generator.generate_code(whatever size you want of the code)
# class Generator:

#     @staticmethod
#     def generate_code(size):
#         return "".join(random.choice(string.digits) for _ in range(size))
    
#     @staticmethod
#     def generate_activation_code(size):
#         code = Generator.generate_code(size)
#         qs = User.objects.filter(activation_code = code).exists()

#         return code if not qs else Generator.generate_activation_code(size)
     
    


def code_generator(size,chars=string.digits):
    return "".join(random.choice(chars)for _ in range(size))


def get_unique_code(size,model_):
    code = code_generator(size)
    qs = model_.objects.filter(activation_code = code)

    return get_unique_code(size,model_) if qs.exists() else code 

