import json
from pathlib import Path
import typer
 
from tool import (
    extract_text,
    classify_document,
    extract_ci_kvp,
    get_doc_type_from_folder,
)
 
app = typer.Typer()
SUPPORTED_EXTENSIONS = {".pdf"}
 
 
def get_files(input_dir: Path):
    for file in input_dir.rglob("*"):
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield file
 
 
@app.command()
def extraction(input_dir: str):
    """Extract text from documents"""
    input_path = Path(input_dir)
    results = []
 
    for file in get_files(input_path):
        text = extract_text(str(file))
        results.append({
            "file_name": file.name,
            "text_extracted": text
        })
 
    Path("output").mkdir(exist_ok=True)
    with open("output/extraction.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
 
    typer.echo("✅ Text extraction completed")
 
 
@app.command()
def classification(input_dir: str):
    """Classify documents"""
    input_path = Path(input_dir)
    results = []
 
    for file in get_files(input_path):
        text = extract_text(str(file))
        folder_type = get_doc_type_from_folder(str(file))
        doc_type = folder_type or classify_document(text)
 
        results.append({
            "file_name": file.name,
            "document_type": doc_type
        })
 
    Path("output").mkdir(exist_ok=True)
    with open("output/classification.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
 
    typer.echo("✅ Classification completed")
 
 
@app.command("kvp-extraction")
def kvp_extraction(input_dir: str):
    """Extract KVPs from CI documents"""
    input_path = Path(input_dir)
    results = []
 
    for file in get_files(input_path):
        folder_type = get_doc_type_from_folder(str(file))
 
        if folder_type == "CI":
            text = extract_text(str(file))
            kvp = extract_ci_kvp(text)
 
            results.append({
                "file_name": file.name,
                "kvp": kvp
            })
 
    Path("output").mkdir(exist_ok=True)
    with open("output/ci_kvp.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
 
    typer.echo("✅ CI KVP extraction completed")
 
 
if __name__ == "__main__":
    app()