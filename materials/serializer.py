from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkToVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    link_to_video_lesson = serializers.URLField(validators=[LinkToVideoValidator()])

    class Meta:
        model = Lesson
        exclude = ("created_at_lesson",)


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    link_to_video_course = serializers.URLField(validators=[LinkToVideoValidator()])
    is_subscribed = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        exclude = ("created_at_course",)


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("user", "course", "created_at")
