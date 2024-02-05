# merge two dictionary into one

d1 ={'ten':10,"twenty":20,"thirty":30}
d2 ={'thirty':30,"forty":40,'fifty':50}

d1.update(d2)
print(d1)

# single line approach
d3 = {**d1, **d2}
print(d3)