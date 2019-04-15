import requests, json 
  
def buscar(lat,lon, radio):  
	api_key = 'AIzaSyAiGXvWHpeV2QXpNtlyREhnwrW7g_kC770'
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Restaurants"

#location = input("Location: ")
#radio = input('Radio: ') 

	r = requests.get(url + '&location=' + lat+" "+lon +"&radio"+ radio +'&key=' + api_key)
	x = r.json()   
	y = x['results'] 
  
	restaurantes = open('restaurantes.csv','w')
	for restaurante in y:
		try:
			restaurantes.write(str(restaurante['geometry']['location']['lng'])+','+str(restaurante['geometry']['location']['lat'])+" , "+restaurante['name']+'\n')
		except KeyError as e:
			restaurantes.write(str(restaurante['geometry']['location']['lng'])+','+str(restaurante['geometry']['location']['lat'])+" , "+restaurante['name']+'\n')
	restaurantes.close()

	for restaurante in range(len(y)): 
		print(y[i]['name']) 

def llamar():
	buscar("-33.86094732989272","151.2075474201073","1000")
	