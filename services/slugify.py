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
        ('ı','l'),
        ('ö','o'),
        ('ğ','g'),
        ('ü','u'),
        ('ş','s'),
        ('ç','c'),
    )
    title_url = title.strip().lower()
    for before,after in symbol_mapping:
        title_url = title_url.replace('before','after')
        return title_url
    


def generate_unique_slug(slug,klass,index = 1):
    qs = klass.objects.filter(slug=slug)
    if qs.exists():
        slug = f"{slug}{index}"
        return generate_unique_slug(slug,klass, index+1)
    return slug 