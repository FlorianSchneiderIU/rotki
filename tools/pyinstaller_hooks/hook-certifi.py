"""
PyInstaller hook for certifi to include the certificate bundle
"""
import certifi
from PyInstaller.utils.hooks import collect_data_files

# Include the certifi certificate bundle
datas = collect_data_files('certifi')