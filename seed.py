from django.contrib.auth.models import User
from django.utils.text import slugify

from courses.models import Course, Module, Subject

# Create a user if not exists
user, created = User.objects.get_or_create(
    username="admin", defaults={"email": "admin@example.com", "password": "adminpass"}
)


# 5 subjects
subject_titles = ["Mathematics", "Physics", "Chemistry", "History", "Literature"]

for title in subject_titles:
    subject, _ = Subject.objects.get_or_create(title=title, slug=slugify(title))

    # 5 courses per subject
    for i in range(1, 6):
        course_title = f"{title} Course {i}"
        course, _ = Course.objects.get_or_create(
            owner=user,
            subject=subject,
            title=course_title,
            slug=slugify(course_title),
            defaults={"overview": f"Overview of {course_title}"},
        )

        # Add 3 modules per course
        for j in range(1, 4):
            Module.objects.get_or_create(
                course=course,
                title=f"Module {j} - {course_title}",
                description=f"This is the description for Module {j} in {course_title}",
            )

print("✅ Seeding complete.")
