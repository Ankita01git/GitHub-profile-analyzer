import requests
import matplotlib.pyplot as plt

search= input("Enter your Github username:")

response = requests.get(f"https://api.github.com/users/{search}")
data = response.json()

response1 = requests.get(f"https://api.github.com/users/{search}/repos")
data1 = response1.json()

print(f"Name: {data['name']}, Bio : {data['bio']},Followers:{data['followers']}")

output = sorted(data1, key=lambda x :x["stargazers_count"], reverse=True)
lang_filter = input("Filter by language? (press Enter to skip):")

if lang_filter:
     output = [n for n in output if lang_filter.lower() in (n['language'] or "").lower()]

# printing top 5 respo by star
top_repos = output[:5]
names = [result['name'] for result in top_repos]
stars = [result['stargazers_count'] for result in top_repos]
for result in top_repos :
    print(f"Name : {result['name']}, Language : {result.get('language', 'Unknown')}, star: {result['stargazers_count']}")

# printing a chart of rating by star
plt.bar(names, stars)
plt.title("Top Repos by Stars")
plt.xlabel("Repository")
plt.ylabel("Stars")
plt.tight_layout()
plt.show()