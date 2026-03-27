import os

def organize_pdfs():
    files = os.listdir()
    
    # create folder if not exists
    if not os.path.exists("pdf_files"):
        os.mkdir("pdf_files")

    count = 1

    for file in files:
        if file.endswith(".pdf"):
            new_name = f"{count}.pdf"
            os.rename(file, new_name)
            os.replace(new_name, f"pdf_files/{new_name}")
            count += 1

    print("Done! Files organized.")

if __name__ == "__main__":
    organize_pdfs()