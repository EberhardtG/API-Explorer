

# 🌐 JSONPlaceholder API Exploration  
A Python project demonstrating how to interact with a public REST API using the `requests` library. This script performs multiple HTTP operations — GET, POST — and prints structured results along with clear explanations of *why* each request is made and the *design* behind it.

---

## 🚀 Features  
- Retrieve all users  
- Retrieve all posts by a specific user  
- Retrieve all comments for a specific post  
- Create a new post (simulated)  
- Includes detailed **why** and **design** commentary for each API call  

---

## 📁 Project Structure  
```
api-demo/
│
├── api_script.py     # Main script containing all API calls
└── README.md         # Project documentation
```

---

## 🔧 Technologies Used  
- **Python 3**  
- **requests** library  
- **JSONPlaceholder API** (`https://jsonplaceholder.typicode.com/` [(jsonplaceholder.typicode.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fjsonplaceholder.typicode.com%2F"))  

---

## 📦 Installation  
Clone the repository:

```
git clone https://github.com/yourusername/jsonplaceholder-api-demo.git
cd jsonplaceholder-api-demo
```

Install dependencies:

```
pip install requests
```

Run the script:

```
python api_script.py
```

---

## 🧠 API Operations & Explanations  

### 1️⃣ GET All Users  
Retrieves all users and prints their names and emails.

**Why:**  
The `/users` endpoint returns a list of user objects, each containing details like name and email. Iterating through the list allows us to display each user’s basic information. Because no specific user ID is provided, the API returns all users.

**Design:**  
A simple GET request using `requests.get()` retrieves the JSON response. Looping through the list and printing key fields provides a clear, readable output. This design is efficient for quickly accessing and displaying user data.

---

### 2️⃣ GET All Posts by User #3  
Uses query parameters to filter posts by a specific user.

**Why:**  
The `/posts` endpoint supports filtering via query parameters. Passing `userId=3` retrieves only posts created by user #3, allowing targeted data exploration.

**Design:**  
Using `params={"userId": 3}` keeps the request clean and readable. The response is parsed and iterated through, printing each post’s ID and a preview of its title. This approach makes the output concise and informative.

---

### 3️⃣ GET All Comments for Post #1  
Retrieves comments associated with a specific post.

**Why:**  
The `/posts/1/comments` endpoint automatically filters comments by post ID. Each comment object includes fields like `id`, `name`, `email`, and `body`, giving insight into user interactions on that post.

**Design:**  
A direct GET request to the endpoint returns all related comments. Looping through the list and printing the comment ID, name, and email provides a clear snapshot of the discussion. No query parameters are needed because the endpoint already scopes the results.

---

### 4️⃣ POST a New Post (Simulated)  
Creates a new post using JSONPlaceholder’s simulated POST behavior.

**Why:**  
The JSON object includes the required fields (`title`, `body`, and `userId`), representing the content of the post and the user who created it. Sending the data using `json=new_post` ensures the request body is properly encoded as JSON. The response is then parsed and printed to confirm that the simulated creation succeeded.

**Design:**  
Using `json=new_post` keeps the code readable and avoids manual serialization. Printing the status code and returned fields provides immediate feedback about the operation, making it easy to verify that the API accepted the request.

---

## 📈 Learning Outcomes  
This project demonstrates:

- How to make GET and POST requests  
- How to pass query parameters  
- How to parse JSON responses  
- How REST endpoints are structured  
- How to write clear *why/design* documentation for API interactions  

---

## 📄 License  
This project is open-source under the MIT License.

