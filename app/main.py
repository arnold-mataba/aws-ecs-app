from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="aws-ecs-app")

_preferences = {"theme": "dark", "notifications": True}
_trials = [
    {"id": 1, "name": "VPC endpoints only, no NAT Gateway"},
    {"id": 2, "name": "Immutable ECR image tagging"},
    {"id": 3, "name": "Blue/green deployment via CodeDeploy"},
]
_future = [
    {"id": 1, "name": "HTTPS via ACM + custom domain"},
    {"id": 2, "name": "Canary traffic shifting"},
]


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head><title>ECS CI/CD Lab</title></head>
      <body style="font-family: sans-serif; text-align: center; margin-top: 10%;">
        <h1>ARNOLD CIKURU MATABA</h1>
        <p>This is my work on the lab on ECS CI/CD</p>
      </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/preferences")
def preferences():
    return _preferences


@app.get("/trials")
def trials():
    return _trials


@app.get("/recent")
def recent():
    return _trials[-2:]


@app.get("/future")
def future():
    return _future
