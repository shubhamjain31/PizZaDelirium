from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def model_dict(model, cat=None):
    """
        Returns a dictionary based on cat (category) on a model where keys are 
        field names (minus 'id') with all possible, distinct values. If no 
        cat value passed, all categories and values are returned.
    """

    keys = [field.name for field in model._meta.get_fields()]
    new = {}
    if 'id' in keys:
        keys.remove('id')

    if cat is None:
        for k in keys:
            new[k] = model.objects.values_list(k, flat=True).distinct()
    # Remove extras from subs
    elif cat is 'Subs':
        for k in keys:
            new[k] = model.objects.filter(category=cat).exclude(
                extra=True
            ).values_list(k, flat=True).distinct()
    else:
        for k in keys:
            new[k] = model.objects.filter(category=cat).values_list(
                k, 
                flat=True
            ).distinct()

    return new;

def cart_count(customer):
    """ 
        Return number of items in cart.
    """
    # try:
    #     cart = Order.objects.get(customer=customer, in_cart=True)
    # except Order.MultipleObjectsReturned:
    #     raise Http404("More than one cart found.")
    # except Order.DoesNotExist:
    #     return 0 
    # else:
    #     # Exclude sub extras in count
    #     return cart.items.exclude(category='Subs', extra=True).count() 
    return '6'