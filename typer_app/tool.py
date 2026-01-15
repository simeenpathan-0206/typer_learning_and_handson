import os
import re
from typing import Dict
from PyPDF2 import PdfReader
 
 
def extract_text(file_path: str) -> str:
    if file_path.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    return ""
 
 
def classify_document(text: str) -> str:
    text_lower = text.lower()
 
    if "policy number" in text_lower and "insured" in text_lower:
        return "CI"
    elif "doctor" in text_lower or "hospital" in text_lower:
        return "DR"
    return "JUNK"
 
 
def extract_ci_kvp(text: str) -> Dict[str, str]:
    patterns = {
        "policy_number": r"policy number\s*:\s*(\S+)",
        "insured_name": r"insured name\s*:\s*(.+)",
        "sum_insured": r"sum insured\s*:\s*(\S+)",
    }
 
    kvp = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            kvp[key] = match.group(1).strip()
 
    return kvp
 
 
def get_doc_type_from_folder(file_path: str) -> str:
    folder = os.path.basename(os.path.dirname(file_path)).lower()
    if folder in {"ci", "dr", "junk"}:
        return folder.upper()
    return ""