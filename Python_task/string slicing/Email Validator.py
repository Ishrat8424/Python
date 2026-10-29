email=input("Enter the Email:")
# Requirements
# • Print the username.  
# • Print the domain name.  
# • Print the extension.  
# • Reverse the email. 
# email="ijkhazi4@gmail.com"
print(email)
i=1
while email[i]!="@": 
    i+=1
print(email[0:i])

j=i
while email[j]!=".":
    j+=1
print(email[i+1:j])
k=j+1
print(email[k:])