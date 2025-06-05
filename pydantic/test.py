from datetime import datetime
from typing import List, Dict, Optional, Union
from enum import Enum
from pydantic import (
    BaseModel, 
    Field, 
    EmailStr, 
    field_validator,
    model_validator,
    ConfigDict,
    constr,
    conint,
    HttpUrl
)
from uuid import UUID
import re

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class Address(BaseModel):
    street: str = Field(..., min_length=5, max_length=100)
    city: str
    country: str
    postal_code: str
    
    @field_validator('postal_code')
    @classmethod
    def validate_postal_code(cls, v: str) -> str:
        if not re.match(r'^\d{5,6}$', v):
            raise ValueError('Postal code must be 5 or 6 digits')
        return v

class ContactInfo(BaseModel):
    email: EmailStr
    phone: str = Field(..., pattern=r'^\+?1?\d{9,15}$')
    website: Optional[HttpUrl] = None

class Project(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    
    @field_validator('end_date')
    @classmethod
    def end_date_must_be_after_start_date(cls, v: Optional[datetime], info) -> Optional[datetime]:
        if v and 'start_date' in info.data and v < info.data['start_date']:
            raise ValueError('end_date must be after start_date')
        return v

class User(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    id: UUID
    username: constr(min_length=3, max_length=50)
    age: conint(gt=0, lt=150)
    role: UserRole
    is_active: bool = True
    address: Address
    contact: ContactInfo
    projects: List[Project] = []
    metadata: Dict[str, Union[str, int, float]] = Field(default_factory=dict)
    score: float = Field(..., ge=0, le=100)
    
    @model_validator(mode='after')
    def check_admin_age(self) -> 'User':
        if self.role == UserRole.ADMIN and self.age < 18:
            raise ValueError('Admins must be at least 18 years old')
        return self

# 使用示例
if __name__ == "__main__":
    try:
        # 创建一个有效的用户实例
        user = User(
            id="123e4567-e89b-12d3-a456-426614174000",
            username="john_doe",
            age=25,
            role=UserRole.ADMIN,
            score=85.5,
            address=Address(
                street="123 Main Street",
                city="New York",
                country="USA",
                postal_code="10001"
            ),
            contact=ContactInfo(
                email="john@example.com",
                phone="+1234567890",
                website="https://example.com"
            ),
            projects=[
                Project(
                    name="Project A",
                    description="A test project",
                    start_date=datetime.now(),
                )
            ],
            metadata={
                "department": "IT",
                "employee_id": 12345,
                "performance_rating": 4.5
            }
        )
        print("Valid user created:", user.model_dump())
        
        # 创建一个无效的用户实例（会引发验证错误）
        invalid_user = User(
            id="invalid-uuid",  # 无效的 UUID
            username="a",       # 用户名太短
            age=200,           # 年龄超出范围
            role=UserRole.ADMIN,
            score=150,         # 分数超出范围
            address=Address(
                street="St",   # 街道名太短
                city="NY",
                country="USA",
                postal_code="ABC"  # 无效的邮政编码
            ),
            contact=ContactInfo(
                email="invalid-email",  # 无效的邮箱
                phone="123",           # 无效的电话号码
            )
        )
    except Exception as e:
        print("Validation error:", str(e))
