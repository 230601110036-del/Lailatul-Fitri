from django.db import models


class Instagram(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
    ]

    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        default='instagram'
    )

    def __str__(self):
        return f"{self.id}. {self.username} - {self.platform}"