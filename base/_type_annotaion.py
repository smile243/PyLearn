from typing import List, Dict, Tuple, Optional, Union, TypeVar, Any

# Basic type annotations
name: str = "Python"
age: int = 30
height: float = 175.5
is_active: bool = True

# List type annotations
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["Alice", "Bob", "Charlie"]

# Dictionary type annotations
user_scores: Dict[str, int] = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

# Tuple type annotations
coordinates: Tuple[float, float] = (12.5, -34.8)
rgb_color: Tuple[int, int, int] = (255, 128, 0)

# Optional type (can be None)
maybe_name: Optional[str] = None
maybe_number: Optional[int] = 42

# Union type (can be multiple types)
mixed_value: Union[str, int] = "Hello"
mixed_value = 42  # This is also valid

# Custom class with type hints
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I'm {self.age} years old"

# Type alias
UserId = int
UserDict = Dict[UserId, Person]

# Function with type annotations
def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

# Function with multiple parameters and complex return type
def process_user_data(
    name: str,
    age: int,
    scores: Optional[List[int]] = None
) -> Tuple[str, float]:
    """Process user data and return a tuple of name and average score."""
    if scores is None:
        scores = []
    avg_score = calculate_average(scores) if scores else 0.0
    return (name.upper(), avg_score)

# Generic type example
T = TypeVar('T')

def first_element(lst: List[T]) -> Optional[T]:
    """Return the first element of a list if it exists."""
    return lst[0] if lst else None

# Usage examples
if __name__ == "__main__":
    # Create a person instance
    person = Person("Alice", 25)
    print(person.greet())
    
    # Use the calculate_average function
    grades: List[float] = [85.5, 92.0, 88.5, 95.0]
    average = calculate_average(grades)
    print(f"Average grade: {average}")
    
    # Process user data
    name, score = process_user_data("Bob", 30, [90, 85, 88])
    print(f"Processed data: {name}, Score: {score}")
    
    # Use generic function
    numbers_list: List[int] = [1, 2, 3]
    first_num = first_element(numbers_list)
    print(f"First number: {first_num}")
