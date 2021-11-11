from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Order



def startdate(value):
    print(value)
    print(Order.objects.filter(start_date__lte= value, date_of_daparture__gte = value))
    if str(Order.objects.filter(start_date__lte= value, date_of_daparture__gte = value)) != '<QuerySet []>' :
        print("СОВПАДЕНИЕ 1")
        raise ValidationError(
            _('На цю дату вже заброньовано номер'),

        )

def enddate(value):
    print(value)
    if str(Order.objects.filter(start_date__lte= value, date_of_daparture__gte=value)) != '<QuerySet []>' :
        print("СОВПАДЕНИЕ 2")
        raise ValidationError(
            _('На цю дату вже заброньовано номер'),

        )