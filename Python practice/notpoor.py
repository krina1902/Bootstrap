s= "the book is not so poor really"
no=s.find("not")
po=s.find("poor")

if no<po and no!= -1:
    print(s[:no] + "good" + s[po+4:])