from locust import HttpUser, task , between
class MLTest(HttpUser):
     wait_time = between(1, 3) 
     @task 
     def predict(self): 
         self.client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]}) 
# Run test 
#locust -f locustfile.py --host=http://localhost:5000