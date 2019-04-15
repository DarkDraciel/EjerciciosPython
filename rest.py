import requests, json 
  
api_key = 'AIzaSyAiGXvWHpeV2QXpNtlyREhnwrW7g_kC770'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Restaurants"

location = input("Location: ")
radio = input('Radio: ') 

r = requests.get(url + '&location=' + location +"&radio"+ radio +'&key=' + api_key) 
x = r.json()   
y = x['results'] 
  
restaurantes = open('restaurantes.csv','w')
for restaurante in y:
	try:
		restaurantes.write(restaurante['name']+'\n')
	except KeyError as e:
		restaurantes.write(restaurante['name']+'\n')
restaurantes.close()
#for i in range(len(y)): 
#   print(y[i]['name']) 
