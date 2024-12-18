#remove spaceing using .strip()

name="        PRAJYOT       "
newname=name.strip()
print("The Name without any space will be:",newname)


#remove space from left using .lstrip()
lspace=name.lstrip()
print("The Name without any space will be:",lspace)

#remove space from right using .rstrip()
rspace=name.rstrip()
print("The Name without any space will be:",rspace)
