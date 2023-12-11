from datetime import date, datetime, timedelta

from rest_framework import views, viewsets
from rest_framework.response import Response

from calc.models import Item
from calc.serializers import ItemSerializer, ItemListSerializer


SCHENGEN_DAYS = 90
TIMEFRAME = 180


class StayView(views.APIView):
    """
    A viewset for listing Stay instances.
    """
    def get(self, request, current_date=date.today()):

        # current_date = request.query_params["current_date"]

        stays = Item.objects.all().order_by("date")
        serializer = ItemSerializer(stays, many=True)
        tourist_days = 0
        begin_date = date.today() - timedelta(days=TIMEFRAME - 1)

        for stay in stays.reverse():
            if stay.date > begin_date:
                if stay.status == "Tourist" and stay.is_schengen:
                    tourist_days += (current_date - stay.date).days
                current_date = stay.date
            else:
                if stay.status == "Tourist" and stay.is_schengen:
                    tourist_days += (current_date - begin_date).days
                break
        remaining_days = max(SCHENGEN_DAYS - tourist_days, 0)
        overstay_days = -min(SCHENGEN_DAYS - tourist_days, 0)

        return Response(
            status=200,
            data={
                "stays": serializer.data,
                "begin_date": begin_date,
                "tourist_days": tourist_days,
                "remaining_days": remaining_days,
                "overstay_days": overstay_days
            }
        )
