class UnicException(Exception):
    """value uniqueness error"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Any exception: {self.message}'


class AnyException(Exception):
    """Any exception"""
