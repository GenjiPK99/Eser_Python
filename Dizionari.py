d1 = {10 : "a",
      20 : "b",
      }
d2 = {30 : "c"}
l1 = d1.items()
l2 = d2.items()
print (l1)
print (l2)
d3 = dict(l1)
print (d3)
d3.update(dict(l2))
print (d3)