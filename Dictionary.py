student_data = {
    "id1": {"name": "adyant",  "class":"VII", "subjects":"maths, computer, physics"},
    "id2": {"name": "nairit",  "class":"VII", "subjects":"maths, computer, physics"},
    "id3": {"name": "donald",  "class":"VII","subjects":"maths, computer, physics"},
    "id4": {"name": "donald", "class":"VII","subjects":"maths, computer, physics"}  
    }

result = {}
keys = []
for student_id, details in student_data.items(): 
    uni = (details["name"],details["class"]) 
details["subjects"]

if uni not in keys: 
    keys.append(uni)
    result [student_id] = details

for k, v in result.items(): 
    print(k,":",v)