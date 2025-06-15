from django.core.management.base import BaseCommand
from onlinecourse.models import Course, Instructor, Lesson, Question, Choice
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create a superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')

        # Create an instructor
        instructor_user = User.objects.create_user(
            username='instructor',
            email='instructor@example.com',
            password='instructor',
            first_name='John',
            last_name='Doe'
        )
        instructor = Instructor.objects.create(
            user=instructor_user,
            full_time=True,
            total_learners=0
        )

        # Create sample courses
        courses_data = [
            {
                'name': 'Python Programming',
                'description': 'Learn Python programming from scratch',
                'image': 'course_images/python.jpg',
            },
            {
                'name': 'Web Development',
                'description': 'Master web development with HTML, CSS, and JavaScript',
                'image': 'course_images/web.jpg',
            },
            {
                'name': 'Data Science',
                'description': 'Introduction to data science and machine learning',
                'image': 'course_images/data.jpg',
            }
        ]

        for course_data in courses_data:
            course = Course.objects.create(
                name=course_data['name'],
                description=course_data['description'],
                pub_date=timezone.now(),
                total_enrollment=0
            )
            course.instructors.add(instructor)

            # Add a lesson to each course
            lesson = Lesson.objects.create(
                course=course,
                title=f'Introduction to {course.name}',
                content=f'This is an introduction to {course.name}.',
                order=1
            )

            # Add a question to each course
            question = Question.objects.create(
                course=course,
                question_text=f'What is {course.name}?',
                grade=10
            )

            # Add choices to the question
            Choice.objects.create(
                question=question,
                choice_text=f'Correct answer for {course.name}',
                is_correct=True
            )
            Choice.objects.create(
                question=question,
                choice_text=f'Incorrect answer 1 for {course.name}',
                is_correct=False
            )
            Choice.objects.create(
                question=question,
                choice_text=f'Incorrect answer 2 for {course.name}',
                is_correct=False
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database')) 