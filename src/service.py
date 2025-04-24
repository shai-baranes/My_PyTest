# for new Mock testing
import requests

databse = {
	1: "Alice",
	2: "Bob",
	3: "Charlie",
}



def get_user_from_db(id: int) -> str | None:
	return databse.get(id)


def get_users() -> str: # from URL JSON
	response = requests.get("https://jsonplaceholder.typicode.com/users") # valid web site for testing purpose
	if response.status_code == 200:
		return response.json()

	raise requests.HTTPError








# list of users' data:

# [
# {
# "id": 1,
# "name": "Leanne Graham",
# "username": "Bret",
# "email": "Sincere@april.biz",
# "address": {
# "street": "Kulas Light",
# "suite": "Apt. 556",
# "city": "Gwenborough",
# "zipcode": "92998-3874",
# "geo": {
# "lat": "-37.3159",
# "lng": "81.1496"
# }
# },
# "phone": "1-770-736-8031 x56442",
# "website": "hildegard.org",
# "company": {
# "name": "Romaguera-Crona",
# "catchPhrase": "Multi-layered client-server neural-net",
# "bs": "harness real-time e-markets"
# }
# },
# {
# "id": 2,
# "name": "Ervin Howell",
# "username": "Antonette",
# "email": "Shanna@melissa.tv",
# "address": {
# "street": "Victor Plains",
# "suite": "Suite 879",
# "city": "Wisokyburgh",
# "zipcode": "90566-7771",
# "geo": {
# "lat": "-43.9509",
# "lng": "-34.4618"
# }