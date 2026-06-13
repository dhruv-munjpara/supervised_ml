from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

model = pickle.load(open("placement.pkl", "rb"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Placement Prediction API Running"}

@app.post("/predict")
def predict(data: dict):

    iq = float(data["IQ"])
    prev_sem = float(data["Prev_Sem_Result"])
    cgpa = float(data["CGPA"])
    communication = float(data["Communication_Skills"])
    projects = float(data["Projects_Completed"])

    result = model.predict([[
        iq,
        prev_sem,
        cgpa,
        communication,
        projects
    ]])

    return {
    "prediction": result[0]
    }   