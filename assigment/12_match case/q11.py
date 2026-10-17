print("""
pdf
jpg
png
mp3
mp4""")

choose = input("enter one from given above which file you want to open").lower().strip()

match choose:
    case "pdf":
        print("opening document")
    case "jpg":
        print("opening jpg image")
    case "png":
        print("opening png image")
    case "mp3":
        print("playing audio")
    case "mp4":
        print("playing video")
    case _:
        print("Unknown File Type")