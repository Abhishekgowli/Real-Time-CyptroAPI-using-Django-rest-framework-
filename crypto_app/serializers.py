from . models import Cryptocurrency
from rest_framework import serializers

class CryptocurrencySerilizers(serializers.ModelSerializer):
    class Meta:
        model=Cryptocurrency
        fields = ['cryptocurrency', 'price', 'market_cap', 'change']