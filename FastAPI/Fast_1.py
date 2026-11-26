from fastapi import FastAPI, HTTPException, Path, Query
import json
import os

app = FastAPI()

# Locate data.json relative to this Python file
FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")


def load_data():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


@app.get("/")
def home():
    return {"message": "Welcome To Website"}


@app.get("/view/{user_id}")
def view_data(
    user_id: int = Path(
        ...,
        description="ID of the Patient",
        example=1,
        gt=0
    )
):
    data = load_data()

    for user in data["users"]:
        if user["user_id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Data Not Found"
    )


@app.get("/sort")
def sort_user(
    sort_by: str = Query(..., description="Field to sort by"),
    order: str = Query("asc", description="Sort in asc or desc")
):
    data = load_data()

    valid_fields = ["user_id", "name", "age", "city"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Choose from {valid_fields}"
        )

    order = order.lower()

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc"
        )

    sorted_users = sorted(
        data["users"],
        key=lambda user: user[sort_by],
        reverse=(order == "desc")
    )

    return {
        "sort_by": sort_by,
        "order": order,
        "users": sorted_users
    }