from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    leaderboard_id = models.AutoField(primary_key=True)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return self.team

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    user = models.EmailField()
    description = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.user} - {self.description}"
