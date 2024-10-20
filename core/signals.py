from django.db.models.signals import post_save
from django.dispatch import receiver
from Students.models import StudentProfile
from core.models import User

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'student':
        StudentProfile.objects.create(user=instance)

