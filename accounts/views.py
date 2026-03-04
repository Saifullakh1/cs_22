from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account


class AccountAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
