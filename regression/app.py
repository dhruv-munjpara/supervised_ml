# what should use for api
# 1.fast api -pip insatall fast api
# 2.uvicorn -pip insatall uvicorn
# how to run ==uvicorn 3:app --reload
# app=fastapi()
# get post put patch delete
# get - test @app.post("pridect") -all ok
# salary + exp
#website - 8- 50k
# json==dict class(id,name,email)
# def datainsert(data:dict)  ?data is in inbult method
# frontend -ai-
# -next python .py -load -rb



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle 

model = pickle.load(open("salary_api.pkl", "rb")) 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return{"message":"all ok and done"}

@app.post("/predict")
def pridect(data:dict):
    exp=data["YearsExperience"]

    result=model.predict([[exp]])
    
    return{"YearsExperience" : exp,
             "PredictedSalary" : float(result[0])}

