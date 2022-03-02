import requests
## ^ This will help make requests to the website we want to download from

## This function will be responsible for downloading the image
def downloadFile(url):
    localFileName = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        print("Downloading Info...")
        with open ("C:/Users/Marquel/Desktop/" + localFileName + 'wb') as f:
            print("Writing data to file...")
            for chunk in r.iter_content (chunk_size = 8192):
                f.write(chunk)
    f.close()
    print("Download Complete")
    print("File is saved as " + localFileName)

## Unstoppable loop to prevent having to run the program over and over again
while 1:
    print("Welcome to the Image Downloader!")
    imageUrl = input(str("Image url: "))
    downloadFile(imageUrl)
    print("")
