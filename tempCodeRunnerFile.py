import requests

search= input("Enter your Git hub Link:")

response = requests.get(f"https://api.github.com/users/{search}")

data = response.json()

print(f"Name: {data['name']}, Bio : {data['bio']},Followers:{data['followers']}")
