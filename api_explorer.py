import requests

# --- GET all users and print each user's name and email---
response = requests.get("https://jsonplaceholder.typicode.com/users/")
users = response.json()

for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}")
    #why: the /users/ endpoint returns a list of user objects, each containing details like name and email. The code iterates through this list and prints the name and email of each user. and because theres not a specific user ID provided, it retrieves all users.
    #design: The design of this code is straightforward and efficient for retrieving and displaying user information. It uses the requests library to make a GET request to the API endpoint, processes the JSON response, and iterates through the list of users to print their names and emails. This approach is simple and effective for quickly accessing and displaying user data from the API.


 #GET all posts by user #3 (use query parameters)
response = requests.get(   
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3}
)
posts = response.json()

print(f"\nUser 3 has {len(posts)} posts:")
for post in posts:
    print(f"  [{post['id']}] {post['title'][:50]}...")

    #why: The /posts endpoint with the query parameter userId=3 retrieves all posts made by the user with ID 3. The code processes the JSON response and prints the number of posts along with their IDs and titles. This allows for filtering posts based on a specific user.
    #design: The design of this code is efficient for filtering and displaying posts by a specific user. It uses query parameters to specify the user ID, making the request more targeted. The code then processes the response and iterates through the list of posts to print relevant information, providing a clear view of the user's contributions.

#GET all comments on post #1 (endpoint: /posts/1/comments)
response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
comments = response.json()

print(f"\nPost 1 has {len(comments)} comments:")
for comment in comments:
    print(f"  [{comment['id']}] {comment['name']} - {comment['email']}")
    #why: The /posts/1/comments endpoint returns all comments associated with post ID 1.
    #     No query parameters are needed because the endpoint already filters by post.
    #     Each comment object contains fields like id, name, email, and body.
    #
    #design: The design is simple and effective: make a GET request to the specific
    #        comments endpoint, parse the JSON response, and iterate through the list.
    #        Printing the comment ID, name, and email provides clear, readable output.



#POST a new post (simulated) and print the response
new_post ={
    "title": "Ad hoc carpe diem",
    "body": "He who lives",
    "userId": 1,
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

print(f"\nCreate new post: {response.status_code}")
created = response.json()
print(f"Created new post with id: {created['id']}")
print(f"Title: {created['title']}")
#why:The JSON object includes the required fields (title, body, and userId), which represent the content of the post and the user who created it. Sending the data using json=new_post ensures the request body is properly encoded as JSON. The response is then parsed and printed to confirm that the simulated creation succeeded.

#design:Using json=new_post keeps the code readable and avoids manual serialization. Printing the status code and the returned fields provides immediate feedback about the operation, making it easy to verify that the API accepted the request