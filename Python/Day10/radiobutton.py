import requests
def get_method(url):
    resp = requests.get(url,False)
    if resp.status_code in [200, '200']:
        return resp.content
    print(resp)
def file_write(filename, data):
    with open(filename, 'wb') as w_obj:
        w_obj.write(data)
        return True
    print(w_obj)
data = get_method("https://en.wikipedia.org/wiki/Python_(programming_language)")
status = file_write("C:\\Users\\vinit\\Desktop\\Python Training\\py.html", data)
def fetch_method():
    with open("C:\\Users\\vinit\\Desktop\\Python Training\\py.html","r") as r_obj:
        out = r_obj.readlines()
        for i in out:
            if i.startswith("<ul><li>Beautiful"):
                print(i)
            elif i.startswith("<li>E"):
                print(i)
            elif i.startswith("<li>S"):
                print(i)
            elif i.startswith("<li>Complex"):
                print(i)
            elif i.startswith("<li>R"):
                print(i)
fetch_method()