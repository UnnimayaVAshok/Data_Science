def details(name,place,role="dev"):

    print(f"hii {name} u are from {place} n u are a {role}")

details("kochi","dev","arum") # positional arguments

details(place="kochi",role="dev",name="arun" ) # keyword arguments

details(place="kochi",name="arun",role="testing") # default argument