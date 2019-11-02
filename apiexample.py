import api

api_key = ":D"
query = "your Shodan search Query"
    
try:
    liste = api.shodanapi(api_key,query)

    j = 0 
    for i in liste:
        print(i)
        j = j+1
    print(j)

except:
    pass