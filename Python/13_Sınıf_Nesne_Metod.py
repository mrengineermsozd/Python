# x=12
# y="Merhaba"
# z=[1,2,"Hello"]
# print(type(x),type(y),type(z))

x="Merhaba"
print(x[0])
print(x.find("a"))
print(dir(list))
#liste ait metotları gösterir 
x = "Merhaba"
indices = [i for i, char in enumerate(x) if char == 'a']
print(indices)