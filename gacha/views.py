from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from .forms import DashboardForm
from random import shuffle
import random

class DashboardView(TemplateView):
	template_name = 'dashboard.html'

	def get(self, request):
		form = DashboardForm()

		return render(
			request, self.template_name, {'form': form})

	def rolling_gacha_fategrand_order(self, type_gacha):
		gacha_list = []

		gacha_pool = []
		for i in range(0,100):
			gacha_pool.append(i)

		#5star servant
		rnd_5_star_servant_list = random.sample(gacha_pool, 1)
		for rnd_pick in rnd_5_star_servant_list:
			gacha_pool.remove(rnd_pick)

		#4star servant
		rnd_4_star_servant_list = random.sample(gacha_pool, 3)
		for rnd_pick in rnd_4_star_servant_list:
			gacha_pool.remove(rnd_pick)

		#3star servant
		rnd_3_star_servant_list = random.sample(gacha_pool, 40)
		for rnd_pick in rnd_3_star_servant_list:
			gacha_pool.remove(rnd_pick)

		#5star craft essense
		rnd_5_star_craftessense_list = random.sample(gacha_pool, 4)
		for rnd_pick in rnd_5_star_craftessense_list:
			gacha_pool.remove(rnd_pick)

		#4star craft essense
		rnd_4_star_craftessense_list = random.sample(gacha_pool, 12)
		for rnd_pick in rnd_4_star_craftessense_list:
			gacha_pool.remove(rnd_pick)

		#3star craft essense
		rnd_3_star_craftessense_list = random.sample(gacha_pool, 40)
		for rnd_pick in rnd_3_star_craftessense_list:
			gacha_pool.remove(rnd_pick)

		#Rolling in the Deep
		#Gurantee Case
		gurantee_gacha_list = []
		gurantee_pool = rnd_5_star_servant_list + rnd_4_star_servant_list + rnd_5_star_craftessense_list + rnd_4_star_craftessense_list
		result_one_gurantee_list = random.sample(gurantee_pool, 1)
		for gacha_list_rnd in result_one_gurantee_list:
			gurantee_gacha_list.append(gacha_list_rnd)

		#Normal Case
		number_gacha_list = []
		normal_gacha_list = []
		for i in range(9):
			rnd_range = range(0,100)
			rnd_each = random.sample(rnd_range, 1)
			normal_gacha_list.append(rnd_each[0])

		number_gacha_list = gurantee_gacha_list + normal_gacha_list
		shuffle(number_gacha_list)

		star_gacha_list = []
		for i in number_gacha_list:
			if i in rnd_5_star_servant_list:
				star_gacha_list.append('5Ser')
			elif i in rnd_4_star_servant_list:
				star_gacha_list.append('4Ser')
			elif i in rnd_3_star_servant_list:
				star_gacha_list.append('3Ser')
			elif i in rnd_5_star_craftessense_list:
				star_gacha_list.append('5CE')
			elif i in rnd_4_star_craftessense_list:
				star_gacha_list.append('4CE')
			elif i in rnd_3_star_craftessense_list:
				star_gacha_list.append('3CE')

		return star_gacha_list

	def classifly_name_gacha(self, star_gacha_list):
		servant_5_list = {
			'Artheria', 'Gilgamesh'
		}

		servant_4_list = {
			'servant 4*'
		}

		servant_3_list = {
			'servant 3*'
		}

		ce_5_list = {
			'CE 5*'
		}

		ce_4_list = {
			'CE 4*'
		}

		ce_3_list = {
			'CE 3'
		}

		name_gacha_list = []

		for gacha in star_gacha_list:
			print gacha
			if gacha == '5Ser':
				name_gacha_list.append(random.sample(servant_5_list, 1))
			elif gacha == '4Ser':
				name_gacha_list.append(random.sample(servant_4_list, 1))
			elif gacha == '3Ser':
				name_gacha_list.append(random.sample(servant_3_list, 1))
			elif gacha == '5CE':
				name_gacha_list.append(random.sample(ce_5_list, 1))
			elif gacha == '4CE':
				name_gacha_list.append(random.sample(ce_4_list, 1))
			elif gacha == '3CE':
				name_gacha_list.append(random.sample(ce_3_list, 1))			
		
		return name_gacha_list


	def post(self, request):
		form = DashboardForm()

		if 'roll_gacha' in request.POST and request.POST['type_game'] == 'fate_grand_order':
			star_gacha_list = self.rolling_gacha_fategrand_order('happy')
			name_gacha_list = self.classifly_name_gacha(star_gacha_list)
			# print gacha_list
		elif 'roll_gacha' in request.POST and request.POST['type_game'] == 'granblue_fantasy':
			gacha_list = []

		return render(
			request, 'dashboard.html', {"form": form, "gacha_list": name_gacha_list})