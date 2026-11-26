from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List

class patient(BaseModel):
    name:str=Field(max_length=30)
    age:int = Field(gt=0,lt=100)
    email:EmailStr
    weight:float
    url:AnyUrl
    allergy:List[str]

    @field_validator('email')
    @classmethod
    def validator(cls,value):
        valid=['hdfc.com','icic.com']
        domain=value.split('@')[-1]
        if domain not in valid:
            raise ValueError('Not A VALID EMAIL ')
        return value 




def insert(pat:patient):
    print(pat.name)
    print(pat.age)

values={'name':'bhavya','age':40,'email':'ac@gmail.com','weight':33.3,'url':'https://www.youtube.com/watch?v=lRArylZCeOs&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ&index=6','allergy':['fffsd']}
pat = patient(**values)
insert(pat)