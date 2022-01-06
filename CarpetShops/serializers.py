from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from CarpetShops.models import Review
from utils.string_utils import convert_datetime_to_persian_date


class ReviewSerializer(serializers.ModelSerializer):
    date_format = '%-d %B %Y'
    create_at_iso = serializers.DateTimeField(read_only=True, source='created_at')

    class Meta:
        model = Review
        read_only_fields = ['id', 'user', 'carpet_cleaning', 'create_at_iso']
        fields = [*read_only_fields, 'rate', 'comment']
        extra_kwargs = {
            'comment': {'required': False}
        }

    @staticmethod
    def validate_rate(value):
        if value not in list(x / 2 for x in range(0, 11)):
            raise ValidationError('عدد امتیاز باید بین ۱ تا ۵ باشد')
        return value

    def to_representation(self, review: Review):
        review_data = super().to_representation(review)
        is_owner = review.user.pk == self.context['request'].user.pk
        review_data['created_at'] = convert_datetime_to_persian_date(review.created_at)
        review_data['writer'] = is_owner
        return review_data
