
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal, Optional
from fastapi import FastAPI, HTTPException
import json


class Patient(BaseModel):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(max_length=50)]
    city: str
    age: Annotated[int, Field(gt=0)]
    gender: Literal['male', 'female', 'others']
    height: Annotated[float, Field(gt=0)]
    weight: Annotated[float, Field(gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


class PatientUpdate(BaseModel):
    name: Optional[Annotated[str, Field(max_length=50)]] = None
    city: Optional[str] = None
    age: Optional[Annotated[int, Field(gt=0)]] = None
    gender: Optional[Literal['male', 'female', 'others']] = None
    height: Optional[Annotated[float, Field(gt=0)]] = None
    weight: Optional[Annotated[float, Field(gt=0)]] = None


def load_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Welcome To Website'}


@app.get('/patients')
def get_patients():
    return load_data()


@app.get('/patients/{patient_id}')
def get_patient(patient_id: int):
    data = load_data()

    for patient in data['patients']:
        if patient['id'] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail='Patient not found')


@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    for p in data['patients']:
        if p['id'] == patient.id:
            raise HTTPException(
                status_code=400,
                detail='Patient ID already exists'
            )

    patient_data = patient.model_dump()
    data['patients'].append(patient_data)
    save_data(data)

    return {
        'message': 'Patient created successfully',
        'patient': patient_data
    }


@app.put('/edit/{patient_id}')
def update_patient(patient_id: int, updated_patient: Patient):
    data = load_data()

    for index, patient in enumerate(data['patients']):
        if patient['id'] == patient_id:

            if updated_patient.id != patient_id:
                raise HTTPException(
                    status_code=400,
                    detail='Patient ID in URL and body must match'
                )

            data['patients'][index] = updated_patient.model_dump()
            save_data(data)

            return {
                'message': 'Patient updated successfully',
                'patient': data['patients'][index]
            }

    raise HTTPException(status_code=404, detail='Patient not found')


@app.patch('/edit/{patient_id}')
def patch_patient(patient_id: int, updated_patient: PatientUpdate):
    data = load_data()

    for index, patient in enumerate(data['patients']):
        if patient['id'] == patient_id:

            update_data = updated_patient.model_dump(exclude_unset=True)

            if 'id' in update_data:
                raise HTTPException(
                    status_code=400,
                    detail='Patient ID cannot be changed'
                )

            patient.update(update_data)

            validated_patient = Patient(**patient)
            data['patients'][index] = validated_patient.model_dump()

            save_data(data)

            return {
                'message': 'Patient updated successfully',
                'patient': data['patients'][index]
            }

    raise HTTPException(status_code=404, detail='Patient not found')
