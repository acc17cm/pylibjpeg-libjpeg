
from . import pydicom_handler as handler

def add_handler():
    """Add the pixel data handler to *pydicom*.

    Raises
    ------
    ImportError
        If *pydicom* is not available.
    """
    import pydicom.config

    if handler not in pydicom.config.pixel_data_handlers:
        pydicom.config.pixel_data_handlers.append(handler)


def remove_handler():
    """Remove the pixel data handler from *pydicom*.

    Raises
    ------
    ImportError
        If *pydicom* is not available.
    """
    import pydicom.config

    if handler in pydicom.config.pixel_data_handlers:
        pydicom.config.pixel_data_handlers.remove(handler)
