from rest_framework import serializers

from calc.models import Item  #, TouristStay


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "date",
            "country",
            "status",
            "is_schengen",
            # "remaining_days",
        ]


class ItemListSerializer(serializers.Serializer):
    stays = ItemSerializer()

    class Meta:
        model = Item
        fields = [
            "stays",
        ]
