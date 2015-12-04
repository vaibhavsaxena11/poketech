from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from .models import Player, Pokemon

def event(request):
	players_list = Player.objects.all()
	for player in players_list:
		if player.name == request.session['name']:
			count = player.counter
			invalidity = request.session['invalidity']
			invalidity_answer = request.session['invalidity_answer']
			request.session['invalidity'] = 0
			request.session['invalidity_answer'] = 0
			context = {'player':player, 'count':count, 'invalidity':invalidity, 'invalidity_answer':invalidity_answer}

	return render(request, 'pokequest/eventpage.html', context)

def event_submit(request):
	text = request.POST.get('input')
	players_list = Player.objects.all()
	pokemons_list = Pokemon.objects.all()

	for player in players_list:
		if player.name == request.session['name']:
			count = player.counter

			if count!=17 and count!=22 and count!=23 and count!=26 and count!=33 and count!=34 and count!=37 and count!=38 and count!=42 and count!=43 and count!=44 and count!=49 and count!=54 and count!=57 and count!=59 and count!=62 and count!=66 and count!=70 and count!=75 and count!=77 and count!=80 and count!=81 and count!=82 and count!=89 and count!=91 and count!=93 and count!=98 and count!=99 and count!=101 and count!=102 and count!=104 and count!=106:	#'next' case
				if text == 'NEXT':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0

			if count==17:	#tickle his tail
				if text == 'TICKLE HIS TAIL':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()

			if count==22:	#pikachu attack2 (WILD CHARM) unlocks
				if text == 'WILD CHARM':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					
					for poke in pokemons_list:	#setting pikachu's attack1 unlocked true
						if poke.name == 'Pikachu':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.save()
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()

					for poke in pokemons_list:	#setting pikachu's attack1 unlocked true
						if poke.name == 'Pikachu':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.save()

					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0

					for poke in pokemons_list:	#setting pikachu's attack1 unlocked true
						if poke.name == 'Pikachu':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.save()

					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==23:	#wild charm foreplay
				if text == 'WILD CHARM':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
					player.save()

				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
					player.points = player.points - 2
					player.save()

			if count==26:	#puzzle - pikachu attack3 (DEFENSE CURL) unlocks
				if text == 'NO EXCUSE':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					
					for poke in pokemons_list:	#setting pikachu's attack3 unlocked true
						if poke.name == 'Pikachu':
							if poke.player.name == player.name:
								poke.attack3 = True
								poke.save()
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()

					for poke in pokemons_list:	#setting pikachu's attack3 unlocked true
						if poke.name == 'Pikachu':
							if poke.player.name == player.name:
								poke.attack3 = True
								poke.save()

					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0

					for poke in pokemons_list:	#setting pikachu's attack3 unlocked true
						if poke.name == 'Pikachu':
							if poke.player.name == player.name:
								poke.attack3 = True
								poke.save()

					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()				


			if count==33 or count==34:	#first attack on squirtle, similar to gym battle
				if text == 'THUNDERBOLT':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								health_decrement = 0-poke.attack1_damage	#thunderbolt is pikachu's attack1
								poke.health -= poke.attack1_damage/10
								poke.save()
							if poke.name == 'Squirtle':
								health_decrement += poke.attack1_damage		#skull bash is squirtle's attack3
								if health_decrement<0:
									poke.health = poke.health - health_decrement
									poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0

				elif text =='WILD CHARM':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								health_decrement = 0-poke.attack2_damage	#wild charm is pikachu's attack2
								poke.health -= poke.attack2_damage/10
								poke.save()
							if poke.name == 'Squirtle':
								health_decrement += poke.attack2_damage	#skull bash is squirtle's attack1
								if health_decrement<0:
									poke.health = poke.health - health_decrement
									poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0

				elif text =='DEFENSE CURL':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								health_decrement = 0-poke.attack3_damage	#wild charm is pikachu's attack2
								poke.health -= poke.attack3_damage/10
								poke.save()
							if poke.name == 'Squirtle':
								health_decrement += poke.attack3_damage	#skull bash is squirtle's attack1
								if health_decrement<0:
									poke.health = poke.health - health_decrement
									poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0

				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
					player.points = player.points - 2
					player.save()


			if count==37:	#squirtle attack1 (IRON DEFENSE) unlocks here #first unlock
				if text == 'IRON DEFENSE':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					for poke in pokemons_list:	#setting squirtle's attack1 (IRON DEFENSE) unlocked true
						if poke.name == 'Squirtle':
							if poke.player.name == player.name:
								poke.attack1 = True
								poke.unlocked = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:	#setting squirtle's attack1 (IRON DEFENSE) unlocked true
						if poke.name == 'Squirtle':
							if poke.player.name == player.name:
								poke.attack1 = True
								poke.unlocked = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()
					for poke in pokemons_list:	#setting squirtle's attack1 (IRON DEFENSE) unlocked true
						if poke.name == 'Squirtle':
							if poke.player.name == player.name:
								poke.attack1 = True
								poke.unlocked = True
								poke.save()


			if count==38:	#squirtle attack2 (POWER UP PUNCH) unlocks here
				if text == 'POWER UP PUNCH':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					for poke in pokemons_list:	#setting squirtle's attack2 (POWER UP PUNCH) unlocked true
						if poke.name == 'Squirtle':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.unlocked = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:	#setting squirtle's attack1 (IRON DEFENSE) unlocked true
						if poke.name == 'Squirtle':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.unlocked = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()
					for poke in pokemons_list:	#setting squirtle's attack1 (IRON DEFENSE) unlocked true
						if poke.name == 'Squirtle':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.unlocked = True
								poke.save()


			if count==42 or count==43:	#counts also used inside the code - gym battle Squirtle vs Starmie
				if text == 'IRON DEFENSE':	#attack1 of squirtle
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								if count==41:
									health_decrement = 40 - poke.attack1_damage	#Starmie's hyper beam attack = 40
								if count==42:
									health_decrement = 20 - poke.attack1_damage	#Starmie's water pulse attack = 20

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack1_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='POWER UP PUNCH':	#attack2 of squirtle
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								if count==41:
									health_decrement = 40 - poke.attack2_damage	#Starmie's hyper beam attack = 40
								if count==42:
									health_decrement = 20 - poke.attack2_damage	#Starmie's water pulse attack = 20

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack2_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
					player.points = player.points - 2
					player.save()


			if count==44:	#gym battle Squirtle vs Starmie
				if text =='SKULL BASH':	#attack3 of squirtle
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 5
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								health_decrement = 30 - poke.attack3_damage	#Starmie's take down attack = 30
								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack3_damage/10
								poke.attack3 = True
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								health_decrement = 30 - poke.attack3_damage	#Starmie's take down attack = 30
								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack3_damage/10
								poke.attack3 = True
								poke.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								health_decrement = 30 - poke.attack3_damage	#Starmie's Take down attack = 30
								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack3_damage/10
								poke.attack3 = True
								poke.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 1
					player.points = player.points - 3
					player.save()


			if count==49 or count==54:
				if text=='THUNDERBOLT' or text=='WILD CHARM' or text=='DEFENSE CURL':	#attacks of pikachu
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 3
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					player.points = player.points -1
					player.save()
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0


			if count==57:	#puzzle
				if text == 'POKEMON MASTER':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()

					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==59:
				if text=='NEXT':
					player.counter = player.counter + 1
					request.session['counter'] += 1
					for poke in pokemons_list:	#setting Charmander unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.unlocked = True
								poke.save()
				player.save()


			if count==62:	#puzzle
				if text=='KUNGFU' or text=='KUNG FU':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==66:	#puzzle image
				if text=='MISSISSIPPI':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==70:	#puzzle, unlocks charmander's attack1 FLAME THROW
				if text=='SQUARE':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					for poke in pokemons_list:	#setting charmander's attack1 (FLAME THROW) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack1 = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:	#setting charmander's attack1 (FLAME THROW) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack1 = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					for poke in pokemons_list:	#setting charmander's attack1 (FLAME THROW) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack1 = True
								poke.save()
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==75:	#puzzle to unlock Charmander's attack2 DOUBLE TEAM
				if text=='SEVEN' or text=='7':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					for poke in pokemons_list:	#setting charmander's attack2 (DOUBLE TEAM) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:	#setting charmander's attack2 (DOUBLE TEAM) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					for poke in pokemons_list:	#setting charmander's attack2 (DOUBLE TEAM) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack2 = True
								poke.save()
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==77:	#puzzle to unlock Charmander's attack3 DRAGON CLAW
				if text=='ONE' or text=='1':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 20
					player.save()
					for poke in pokemons_list:	#setting charmander's attack3 (DRAGON CLAW) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack3 = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:	#setting charmander's attack3 (DRAGON CLAW) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack3 = True
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					for poke in pokemons_list:	#setting charmander's attack3 (DRAGON CLAW) unlocked true
						if poke.name == 'Charmander':
							if poke.player.name == player.name:
								poke.attack3 = True
								poke.save()
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==80 or count==81 or count==82:	#counts also used inside the code - gym battle vs Sabrina
				if text == 'FLAME THROW':	#attack1 of charmander
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								if count==80:
									health_decrement = 20 - poke.attack1_damage	#Abra's teleport = 20
								if count==81:
									health_decrement = 40 - poke.attack1_damage	#Kadabra's psychic attack = 40
								if count==82:
									health_decrement = 30 - poke.attack1_damage	#Kadabra's toxic attack = 30

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack1_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='DOUBLE TEAM':	#attack2 of charmander
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								if count==80:
									health_decrement = 20 - poke.attack2_damage	#Abra's teleport = 20
								if count==81:
									health_decrement = 40 - poke.attack2_damage	#Kadabra's psychic attack = 40
								if count==82:
									health_decrement = 30 - poke.attack2_damage	#Kadabra's toxic attack = 30

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack2_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='DRAGON CLAW':	#attack3 of charmander
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								if count==80:
									health_decrement = 20 - poke.attack3_damage	#Abra's teleport = 20
								if count==81:
									health_decrement = 40 - poke.attack3_damage	#Kadabra's psychic attack = 40
								if count==82:
									health_decrement = 30 - poke.attack3_damage	#Kadabra's toxic attack = 30

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack3_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					player.points = player.points - 2
					player.save()
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
						


			if count==89:	#nurse joy puzzle 1
				if text=='SARTHAK':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 10
					player.save()
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								poke.health += 25
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								poke.health += 10
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==91:	#nurse joy puzzle 2
				if text=='1L':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 10
					player.save()
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								poke.health += 25
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								poke.health += 10
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==93:	#nurse joy puzzle 3
				if text=='ZACH ZEBRA':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 10
					player.save()
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								poke.health += 25
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				elif text == 'I AM DUMB':
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.save()
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								poke.health += 10
								poke.save()
					request.session['invalidity_answer'] = 0
					request.session['invalidity'] = 0
				else:
					request.session['invalidity_answer'] = 1
					request.session['invalidity'] = 0
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points - 5
					player.save()


			if count==98 or count==99:	#battle vs Jessie (1.1 and 1.2)
				if text == 'IRON DEFENSE':	#attack1 of squirtle
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								if count==98:
									health_decrement = 20 - poke.attack1_damage	#Arbok's Headbutt = 20
								if count==99:
									health_decrement = 30 - poke.attack1_damage	#Arbok's Poison Sting = 30

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack1_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='POWER UP PUNCH':	#attack2 of squirtle
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								if count==98:
									health_decrement = 20 - poke.attack2_damage	#Arbok's Headbutt = 20
								if count==99:
									health_decrement = 30 - poke.attack2_damage	#Arbok's Poison Sting = 30

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack2_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='SKULL BASH':	#attack3 of squirtle
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Squirtle':
								if count==98:
									health_decrement = 20 - poke.attack3_damage	#Arbok's Headbutt = 20
								if count==99:
									health_decrement = 30 - poke.attack3_damage	#Arbok's Poison Sting = 30

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack3_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
					player.points = player.points - 2
					player.save()


			if count==101 or count==102:	#battle vs Jessie (2.1 and 2.2)
				if text == 'FLAME THROW':	#attack1 of charmander
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								if count==101:
									health_decrement = 20 - poke.attack1_damage	#Wezing's Smokescreen = 20
								if count==102:
									health_decrement = 40 - poke.attack1_damage	#Wezing's Poison gas = 40

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack1_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='DOUBLE TEAM':	#attack2 of charmander
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								if count==98:
									health_decrement = 20 - poke.attack2_damage	#Wezing's Smokescreen = 20
								if count==99:
									health_decrement = 40 - poke.attack2_damage	#Wezing's Poison gas = 40

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack2_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='DRAGON CLAW':	#attack3 of charmander
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Charmander':
								if count==98:
									health_decrement = 20 - poke.attack3_damage	#Wezing's Smokescreen = 20
								if count==99:
									health_decrement = 40 - poke.attack3_damage	#Wezing's Poison gas = 40

								if health_decrement>0:
									poke.health -= health_decrement
								poke.health -= poke.attack3_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
					player.points = player.points - 2
					player.save()


			if count==104 or count==106:	#battle vs Jessie (2.1 and 2.2)
				if text == 'THUNDERBOLT':	#attack1 of pikachu
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								poke.health -= poke.attack1_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='WILD CHARM':	#attack2 of pikachu
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								poke.health -= poke.attack2_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				elif text =='DRAGON CLAW':	#attack3 of pikachu
					player.counter = player.counter + 1
					request.session['counter'] = request.session['counter'] + 1
					player.points = player.points + 4
					health_decrement = 0
					for poke in pokemons_list:
						if poke.player.name == player.name:
							if poke.name == 'Pikachu':
								poke.health -= poke.attack3_damage/10
								poke.save()
					player.save()
					request.session['invalidity'] = 0
					request.session['invalidity_answer'] = 0
				else:
					request.session['invalidity'] = 1
					request.session['invalidity_answer'] = 0
					player.points = player.points - 2
					player.save()


	return HttpResponseRedirect('/pokequest/event')

def profile(request):
	players_list = Player.objects.order_by('-points')
	pokemons_list = Pokemon.objects.all()

	poke_list = []

	for player in players_list:
		if player.name == request.session['name']:
			for poke in pokemons_list:
				if poke.player.name == player.name:
					poke_list.append(poke)

			context = {'players_list':players_list, 'player':player, 'poke_list':poke_list}

	return render(request, 'pokequest/profilepage.html', context)

def scorepage(request):
	players_list = Player.objects.order_by('-score')
	pokemons_list = Pokemon.objects.all()
	score = 0
	context={}

	for player in players_list:
		if player.name == request.session['name']:
			score += 3*player.points
			for poke in pokemons_list:
				if poke.player.name == player.name:
					score += 2*poke.health
			player.score = score
			player.save()
			players_list_score = Player.objects.order_by('-score')
			context = {'players_list':players_list_score, 'player':player}

	return render(request, 'pokequest/scorepage.html', context)


def instructions(request):
	context={}
	return render(request, 'pokequest/instructions.html', context)

def pokedex(request):
	context={}
	return render(request, 'pokequest/pokedex.html', context)
