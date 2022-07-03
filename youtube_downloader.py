from pytube import YouTube

link = input("paste video link here: ")
print("Start Downloading... ")

yt = YouTube(link)

display_resolution = yt.streams.get_highest_resolution().resolution
print(display_resolution)

yt.streams.get_highest_resolution().download()
print("Video Downloaded Successfully. ")