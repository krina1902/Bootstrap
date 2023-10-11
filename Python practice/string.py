s="Krina Antala"

print(s.count("a"))
print(s.upper())
print(s.casefold())
print(s.center(20,"*"))
print(s.lower())
print(s.endswith("ala"))
print(s.startswith("kri"))
a=s.find("a A")
print(a)
print(s.index("a",11))
print(s.isalnum()) #false
print("k123".isalnum())
print(s.isalpha()) #false
print("k".isalpha()) 
print("123".isnumeric()) 
print("k123".isnumeric()) #false
print("k 123".isnumeric()) #false
print(s.isspace())#false
print("  ".isspace())
print(s.istitle())
print(s.islower())#false
print(s.isupper())#false
print(s.swapcase())
print(s.replace("a","l"))
print(s.encode())
print(s.expandtabs())
print(s.isascii())
print(s.join("Thumar"))
print(s.ljust(3))
print(s.rstrip("tala"))
print(s.lstrip("Kri"))
mydict = {83 :  80}
txt = "Hello SSm!"
print(txt.translate(mydict))


