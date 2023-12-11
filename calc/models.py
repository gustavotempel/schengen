from datetime import date, datetime, timedelta

from django.db import models

TOURIST_DAYS = 90
TIMEFRAME = 180

SCHENGEN_COUNTRIES = [
    "Austria",
    "Belgium",
    "Czech Republic",
    "Croatia",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Italy",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
]


class Item(models.Model):
    date = models.DateField()
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=25)

    class Meta:
        pass

    @property
    def is_schengen(self):
        return self.country in SCHENGEN_COUNTRIES

    def __str__(self):
        return f"{self.date}, {self.country}, {self.status}"


# class TouristStay(models.Model):
#     last_items = Item.objects.filter(date__gt=(datetime.today() - timedelta(days=TIMEFRAME))).order_by("date")
#     remaining_days = []
#
#     for item in last_items:
#         remaining_days.append(date.today() - item.date)
#
#     @property
#     def remaining_days(self):
#         return self.remaining_days


