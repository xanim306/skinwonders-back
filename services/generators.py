import string
import random


chars = string.digits + string.ascii_letters

chars2 = string.digits + string.ascii_uppercase


class CodeGenerator:
    @staticmethod
    def code_slug_generator(size):
        return "".join(random.choice(string.digits) for _ in range(size))

    @staticmethod
    def product_code_generator(size,chars=chars2):
        return "".join(random.choice(chars) for _ in range(size))
    
    @staticmethod
    def activation_slug_generator(size,chars=chars):
        return "".join(random.choice(chars) for _ in range(size))
    
    
    @classmethod
    def create_slug_shortcode(cls, size, model_):
        new_code = cls.code_slug_generator(size=size)
        qs_exists = model_.objects.filter(code=new_code).exists()
        return cls.create_slug_shortcode(size, model_) if qs_exists else new_code

    @classmethod
    def create_products_shortcode(cls, size, model_):
        new_sku = cls.code_slug_generator(size=size)
        qs_exists = model_.objects.filter(sku=new_sku).exists()
        return cls.create_slug_shortcode(size, model_) if qs_exists else new_sku


    @classmethod
    def create_slug_shortcode_profile(cls, size, model_):
        new_code = cls.code_slug_generator(size=size)
        qs_exists = model_.objects.filter(slug=new_code).exists()
        return cls.create_slug_shortcode(size, model_) if qs_exists else new_code

    @classmethod
    def product_code(cls, model_):
        new_code = cls.product_code_generator()
        qs_exists = model_.objects.filter(code=new_code).exists()
        return cls.create_products_shortcode(10, model_) if qs_exists else new_code

    @classmethod
    def create_activation_link_code(cls, size, model_):
        new_code = cls.code_slug_generator(size=size)
        qs_exists = model_.objects.filter(activation_code=new_code).exists()
        return cls.create_slug_shortcode(size, model_) if qs_exists else new_code
    
    @classmethod
    def create_user_slug_code(cls, size, model_):
        new_slug = cls.activation_slug_generator(size=size)
        qs_exists = model_.objects.filter(slug=new_slug).exists()
        return cls.create_slug_shortcode(size, model_) if qs_exists else new_slug