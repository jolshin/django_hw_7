from django_filters import rest_framework as filters, DateFromToRangeFilter

from .models import Advertisement

class AdvertisementFilter(filters.FilterSet):
	"""Фильтры для объявлений."""

	created_at = DateFromToRangeFilter(field_name='created_at')

	class Meta:
		model = Advertisement
		fields = ['created_at']
