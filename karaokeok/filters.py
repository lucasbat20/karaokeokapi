from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models.functions import Lower


class CaseInsensitiveOrderingFilter(OrderingFilter):
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        if ordering:
            new_ordering = []
            for field in ordering:
                if field.startswith('-'):
                    new_ordering.append(Lower(field[1:]).desc())
                else:
                    new_ordering.append(Lower(field).asc())
            return queryset.order_by(*new_ordering)

        return queryset
