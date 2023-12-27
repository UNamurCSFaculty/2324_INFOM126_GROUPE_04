import random
from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
	# host = "http://localhost:8000"
	wait_time = between(5, 15)
	
	@task(1)
	def hello_world(self):
		self.client.get("/")
		
	@task(1)
	def add_message(self):
		name = f"User{random.randint(1, 10000)}"
		rand_message = f"Hello world! {random.randint(1, 10000)}"
		self.client.post("/", json={"name": name, "message": rand_message})