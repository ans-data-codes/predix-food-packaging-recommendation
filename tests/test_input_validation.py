from src.schemas.food import FoodInput
from src.schemas.storage import StorageConditions
from src.data.validators import validate_food_input, validate_storage_conditions


def test_validate_food_input_requires_commodity_type():
    food = FoodInput(commodity_type="apple")
    assert validate_food_input(food).commodity_type == "apple"


def test_validate_storage_conditions_requires_storage_type():
    storage = StorageConditions(storage_type="cold_chain")
    assert validate_storage_conditions(storage).storage_type == "cold_chain"
