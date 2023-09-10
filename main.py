# write your code here
person ={
    "name":"manar" ,
    "age":17 ,
    "hobbies":['basketball','shooting','badminton']
}
print(person.get["name"])
print(person.get["age"])

print(person["name"])
print(person["age"])

person["age"]="20"
person["country"]="kuwait"

print(f"my name is{person['name']},I am from{person['country']}and I am {person['age']} years old,I really like playing {person['hobbies']} ")
print(f"{person}")
 
person.get("bowling")
def check_hobbies(person):
    if person["hobbies"]>=3:
        print("WOW YOU ARE AMAZING")



