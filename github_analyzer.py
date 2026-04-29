import requests

search= input("Enter your Github username:")

response = requests.get(f"https://api.github.com/users/{search}")
data = response.json()

response1 = requests.get(f"https://api.github.com/users/{search}/repos")
data1 = response1.json()

print(f"Name: {data['name']}, Bio : {data['bio']},Followers:{data['followers']}")

output = sorted(data1, key=lambda x :x["stargazers_count"], reverse=True)
lang_filter = input("Filter by language? (press Enter to skip):")

if lang_filter:
    output=[n for n in output if lang_filter in n['language'].lower()]

for result in output[:5] :
    print(f"Name : {result['name']}, Language : {result.get('language', 'Unknown')}, star: {result['stargazers_count']}")