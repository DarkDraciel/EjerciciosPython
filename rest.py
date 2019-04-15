import requests, json 
 
class Rest():
	def __init__(self, lat,lon, radio):
		api_key = 'AIzaSyAiGXvWHpeV2QXpNtlyREhnwrW7g_kC770'
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Restaurants"
		r = requests.get(url + '&location=' + lat+" "+lon +"&radio"+ radio +'&key=' + api_key)
		x = r.json()   
		y = x['results']
		Csv(y) 
	 
class Csv():
	def __init__(self, y):
		restaurantes = open('restaurantes.csv','w')
		for restaurante in y:
			try:
				restaurantes.write(str(restaurante['geometry']['location']['lng'])+','+str(restaurante['geometry']['location']['lat'])+" , "+restaurante['name']+'\n')
			except KeyError as e:
				restaurantes.write(str(restaurante['geometry']['location']['lng'])+','+str(restaurante['geometry']['location']['lat'])+" , "+restaurante['name']+'\n')
		restaurantes.close()


Rest("-33.86094732989272","151.2075474201073","1000")
		


		
		
