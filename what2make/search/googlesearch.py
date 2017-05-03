from googleapiclient.discovery import build

def search_links(search_term, cse_id):
    service = build("customsearch", "v1", developerKey="AIzaSyATAPIGxR0mMdd6XM7QAjg5zfFcONRBNGU")
    results = service.cse().list(q=search_term, cx=cse_id).execute()
    url = results.get('items',[])
    
    return url

