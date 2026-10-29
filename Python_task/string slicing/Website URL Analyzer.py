# Website URL Analyzer 
# Requirements 
# • Print protocol.  
# • Print website name.  
# • Print extension. 

url="https://www.google.com"
i=0
while url[i]!=":":
    i+=1
print(url[:i])
j=i
while url[j]!=".":
    j+=1
k=j+1
while url[k]!=".":
    k+=1
print(url[j+1:k])

print(url[k:])