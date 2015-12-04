from django.db import models

class Player(models.Model):
	serialno = models.IntegerField(default=1)
	name = models.CharField(max_length=200)
	present = models.BooleanField(default=False)
	points = models.IntegerField(default=0)
	counter = models.IntegerField(default=1) #div tag id till which played
	score = models.IntegerField(default=0)


	def __str__(self):
		return self.name

class Pokemon(models.Model):
	name = models.CharField(max_length=200)
	health = models.IntegerField(default=100)
	unlocked = models.BooleanField(default=False)

	attack1_name = models.CharField(max_length=200, default='attack1')
	attack1_damage = models.IntegerField(default=20)
	attack1 = models.BooleanField(default=False)

	attack2_name = models.CharField(max_length=200, default='attack2')
	attack2_damage = models.IntegerField(default=30)
	attack2 = models.BooleanField(default=False)

	attack3_name = models.CharField(max_length=200, default='attack3')
	attack3_damage = models.IntegerField(default=40)
	attack3 = models.BooleanField(default=False)

	player = models.ForeignKey(Player)
	def __str__(self):
		return self.name


#class Attack(models.Model):
#	name = models.CharField(max_length=200)
#	damage = models.IntegerField(default=0)#to be used to reduce else's power if attack is not defensive, contrary otherwise
#	defensive = models.BooleanField(default=False)#to be true if the attack is defensive
#	def __str__(self):
#		return self.name