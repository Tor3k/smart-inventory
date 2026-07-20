"""
Smart Inventory

Validation service.
"""


class ValidationService:


    @staticmethod
    def validate_required(
        value,
        field_name,
    ):

        if value is None or not str(value).strip():

            raise ValueError(
                f"{field_name} cannot be empty."
            )


    @staticmethod
    def validate_positive(
        value,
        field_name,
    ):

        if value is not None and value < 0:

            raise ValueError(
                f"{field_name} cannot be negative."
            )


    @staticmethod
    def validate_stock(stock):

        ValidationService.validate_positive(
            stock,
            "Product stock",
        )


    @staticmethod
    def validate_choice(
        value,
        valid_values,
        field_name,
    ):

        if value not in valid_values:

            raise ValueError(
                f"Invalid {field_name}."
            )