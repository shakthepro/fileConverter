import subprocess
import moviepy.editor as moviepy

def main():
    fileDirectoryInput = input("Old video file to convert: ")
    fileOutput = input("New video file name: ")
    convertFile(fileDirectoryInput, fileOutput)
    return 1

#function code built by Yasen, https://stackoverflow.com/users/5720818/yasen
#exact source code: https://stackoverflow.com/questions/57344112/how-to-convert-video-on-python-to-mp4-without-ffmpeg

def convertFile(input_file, output_file):
    clip = moviepy.VideoFileClip(input_file)
    clip.write_videofile(output_file)

# Convert a MOD file to MP4

if __name__ == "__main__":
    main()