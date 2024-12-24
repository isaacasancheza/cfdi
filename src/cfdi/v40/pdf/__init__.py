try:
    import reportlab
except ModuleNotFoundError as e:
    raise RuntimeError(
        'The `pdf` module requires additional dependencies to be installed. You can install it with "pip install '
        'package[pdf]".'
    ) from e

from .pdf import generate_pdf
