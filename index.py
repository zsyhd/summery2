from fastapi import FastAPI

app = FastAPI()

dashboard_data = {
    "totalEvents": 6,
    "wellCount": 6,
    "anomalyRate": 0.46,
    "avgPressure": 78.9
}

@app.get("/")
def home():
    return {"message": "Summery2 API is running"}

@app.get("/dashboard")
def get_dashboard():
    return dashboard_data

@app.post("/dashboard/update")
def update_dashboard(
    totalEvents: int | None = None,
    wellCount: int | None = None,
    anomalyRate: float | None = None,
    avgPressure: float | None = None
):
    if totalEvents is not None:
        dashboard_data["totalEvents"] = totalEvents

    if wellCount is not None:
        dashboard_data["wellCount"] = wellCount

    if anomalyRate is not None:
        dashboard_data["anomalyRate"] = anomalyRate

    if avgPressure is not None:
        dashboard_data["avgPressure"] = avgPressure

    return {"status": "updated", "data": dashboard_data}
