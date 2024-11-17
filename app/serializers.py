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
        # Burada instance ile gelen kullanıcıyı güncelleyebiliriz
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance



class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer()  # Eğitmen bilgisi, many=True kullanılmaz.
    sections = SectionSerializer()  # Bölüm listesi tek bir bölüm için kullanılacak.

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        course = Course.objects.create(**validated_data)
        return course

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.url_source = validated_data.get('url_sorce', instance.url_source)
        instance.save()
        return instance


class SectionSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Kurs detayları

    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        section = Section.objects.create(**validated_data)
        return section

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance


class ContentSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)  # Bölüm bilgisi

    class Meta:
        model = Content
        fields = '__all__'

    def create(self, validated_data):
        content = Content.objects.create(**validated_data)
        return content

    def update(self, instance, validated_data):
        instance.content_type = validated_data.get('content_type', instance.content_type)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

    def create(self, validated_data):
        enrollment = Enrollment.objects.create(**validated_data)
        return enrollment


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        return review

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance
    

class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        question = Question.objects.create(**validated_data)
        return question

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.correct_answer = validated_data.get('correct_answer', instance.correct_answer)
        instance.save()
        return instance


class QuizSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def create(self, validated_data):
        quiz = Quiz.objects.create(**validated_data)
        return quiz

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

