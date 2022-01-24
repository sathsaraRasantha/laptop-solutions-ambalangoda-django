from category.models import Category


def menu_links(request):
    links = Category.objects.all().exclude(category_name='Laptop Repairing')
    return dict(links=links)
