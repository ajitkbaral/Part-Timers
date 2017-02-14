from django.db import models
from django.contrib.auth.models import Permission, User

class Skill(models.Model):
	skill_title = models.CharField(max_length=100)

	def __str__(self):
		return self.skill_title

class UserSkill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
	from_date = models.DateField()

	def __str__(self):
		return self.user.username +" - "+self.skill.skill_title


class Job(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	company_name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	position_description = models.TextField(max_length=100)
	from_date = models.DateField()
	to_date = models.DateField()

	def __str__(self):
		return self.position +" - "+self.company_name


class Work(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	work_title = models.CharField(max_length=100)
	work_description = models.TextField()
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
	amount = models.FloatField()
	from_date = models.DateField()
	to_date = models.DateField()

	def __str__(self):
		return self.user.username +" - "+self.work_title

class RequestedWork(models.Model):
	requested_user = models.ForeignKey(User, on_delete=models.CASCADE) 
	work = models.ForeignKey(Work, on_delete=models.CASCADE)

	def __str__(self):
		return self.requested_user.username +" - "+self.work.work_title

class ApprovedWork(models.Model):
	requested_work = models.ForeignKey(RequestedWork, on_delete=models.CASCADE)
	work_status = models.BooleanField(default=False)

	def __str__(self):
		return self.requested_work.requested_user.username +" - "+self.requested_work.work.work_title