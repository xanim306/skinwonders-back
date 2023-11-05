#Azerice slugify function 

def slugify(title):
    symbol_mapping = (
        (' ','-'),
        ('.','-'),
        (',','-'),
        ('!','-'),
        ('?','-'),
        ("'",'-'),
        ('"','-'),
        ('ə','e'),
        ('ı','i'),
        ('ö','o'),
        ('ğ','g'),
        ('ü','u'),
        ('ş','s'),
        ('ç','c'),

    )

    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before,after)

        return title_url
    

def generate_unique_slug(slug, klass):
    original_slug = slug
    index = 1

    while klass.objects.filter(slug=slug).exists():
        slug = f"{original_slug}-{index}"
        index += 1

    return slug


    
