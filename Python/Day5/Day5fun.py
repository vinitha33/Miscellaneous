def calavg(dict1):
    for i, j in dict1.items():
        for a, b in j.items():
            if isinstance(b, dict):
                print(i, "=", str(sum(b.values())/3))

# calavg({'Sakthi':{'class':11,'subject':{'science':99,'maths':70,'social':80}},
#      'Vinitha':{'class':9,'subject':{'science':80,'maths':90,'social':100}},
#      'Arghyaa':{'class':8,'subject':{'science':100,'maths':20, 'social':80}},
#      'Shubham':{'class':10,'subject':{'science':90,'maths':10,'social':100}},
#      'Sahil':{'class':8, 'subject':{'science':10,'maths':90,'social':100}}})