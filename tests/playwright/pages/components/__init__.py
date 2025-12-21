"""
Components package for reusable UI elements.

These component objects represent UI elements that appear across
multiple pages, such as navigation and footer.
"""

from pages.components.navigation import Navigation
from pages.components.footer import Footer

__all__ = [
    "Navigation",
    "Footer",
]
