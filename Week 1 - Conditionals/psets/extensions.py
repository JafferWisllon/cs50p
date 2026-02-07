def main():
    filename = input("File name: ").strip().lower()    
    print(media_type(filename))

def media_type(filename):
    if "." not in filename:
        return "application/octet-stream"
    
    _, extension = filename.rsplit(".", 1)

    match extension:
        case "gif" | "jpg" | "jpeg" | "png":
            return f"image/{extension}"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "applicaion/zip"
        case _:
            return "application/octet-stream"

main()