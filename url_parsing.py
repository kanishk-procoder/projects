url = input("enter the url : ")
protocol = url[:url.find(":")]
dot1 = url.find(".")
dot2 = url.find(".",dot1+1)
domain = url[dot1+1 : dot2]
webpage_st_slash = url.find("/", dot2)
webpage = url[webpage_st_slash+1:]

print(f"Protocol : {protocol}")
print(f"domain : {domain}")
print(f"webpage : {webpage}")