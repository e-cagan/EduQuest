from rest_framework import serializers
from .models import User, Course, Section, Content, Enrollment, Review, Quiz, Question


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    instructor_id = serializers.IntegerField(write_only=True)
    instructor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        instructor_id = validated_data.pop('instructor_id')
        validated_data['instructor'] = User.objects.get(id=instructor_id)
        course = Course.objects.create(**validated_data)
        return course

    def update(self, instance, validated_data):
        if 'instructor_id' in validated_data:
            instructor_id = validated_data.pop('instructor_id')
            validated_data['instructor'] = User.objects.get(id=instructor_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class SectionSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        course_id = validated_data.pop('course_id')
        validated_data['course'] = Course.objects.get(id=course_id)
        section = Section.objects.create(**validated_data)
        return section

    def update(self, instance, validated_data):
        if 'course_id' in validated_data:
            course_id = validated_data.pop('course_id')
            validated_data['course'] = Course.objects.get(id=course_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ContentSerializer(serializers.ModelSerializer):
    section_id = serializers.IntegerField(write_only=True)
    section = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'

    def create(self, validated_data):
        section_id = validated_data.pop('section_id')
        validated_data['section'] = Section.objects.get(id=section_id)
        content = Content.objects.create(**validated_data)
        return content

    def update(self, instance, validated_data):
        if 'section_id' in validated_data:
            section_id = validated_data.pop('section_id')
            validated_data['section'] = Section.objects.get(id=section_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class EnrollmentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    course_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        course_id = validated_data.pop('course_id')
        validated_data['user'] = User.objects.get(id=user_id)
        validated_data['course'] = Course.objects.get(id=course_id)
        enrollment = Enrollment.objects.create(**validated_data)
        return enrollment


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    course_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        course_id = validated_data.pop('course_id')
        validated_data['user'] = User.objects.get(id=user_id)
        validated_data['course'] = Course.objects.get(id=course_id)
        review = Review.objects.create(**validated_data)
        return review

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class QuizSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def create(self, validated_data):
        course_id = validated_data.pop('course_id')
        validated_data['course'] = Course.objects.get(id=course_id)
        quiz = Quiz.objects.create(**validated_data)
        return quiz

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    quiz_id = serializers.IntegerField(write_only=True)
    quiz = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        quiz_id = validated_data.pop('quiz_id')
        validated_data['quiz'] = Quiz.objects.get(id=quiz_id)
        question = Question.objects.create(**validated_data)
        return question

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
