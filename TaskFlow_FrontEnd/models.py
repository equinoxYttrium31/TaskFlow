from django.db import models
import datetime

class UserRole(models.TextChoices):
    TEAM_MEMBER = 'team_member', 'Team Member'
    PROJECT_LEADER = 'project_leader', 'Project Leader'

# Create your models here.
class User(models.Model):
    UserID = models.CharField(max_length=20, unique=True, blank=True, null=True)
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=200)
    Role = models.CharField(
        max_length=50,
        choices=UserRole.choices,  # Use the choices for validation
        default=UserRole.TEAM_MEMBER  # Set a default role
    )

    def generate_userid(self):
        """Generate a unique UserID based on the current year and creation order."""
        year = datetime.datetime.now().year  # Get current year
        # Get the number of users created in the current year
        user_count = User.objects.filter(UserID__startswith=str(year)).count() + 1
        # Format the UserID as yyyy-### (e.g., 2024-001, 2024-002, ...)
        return f"{year}-{user_count:09}"

    def save(self, *args, **kwargs):
        # Generate UserID only if it's not already set
        if not self.UserID:
            self.UserID = self.generate_userid()  # Generate the UserID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Username
