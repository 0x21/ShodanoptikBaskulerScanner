import requests
import json

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

def shodanapi(api_key,query):


    api_url = "https://api.shodan.io/shodan/host/search?key="+api_key+"&query="+query
    liste = []
    req = requests.get(api_url)
    if req.status_code == 200:
        x = json.loads(req.text)
        j=x['total']
        page = int(j/100)+2
        for i in range(1,page):
            pageurl = api_url+"&page="+str(i)
            req = requests.get(pageurl)
            x = json.loads(req.text)
            try:
                for k in range(0,99):
                    liste.append(x['matches'][k]['ip_str'])
            
            
            except:
                pass
    
        liste1 = Remove(liste)
        print(str(len(Remove(liste)))+" ip addresses found")
        return liste1
    else:
        print('Please check your Api Key')
