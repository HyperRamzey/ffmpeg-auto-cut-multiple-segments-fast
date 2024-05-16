from datetime import datetime
import subprocess


def time_diff(start, end):
    start_time = datetime.strptime(start, "%H:%M:%S")
    end_time = datetime.strptime(end, "%H:%M:%S")

    diff = end_time - start_time

    return str(diff)


def generate_ffmpeg_commands(segments, input_file, output_folder, bitrate):
    ffmpeg_commands = []
    for i in range(len(segments)):
        start, end = segments[i].split('-')
        if i < len(segments) - 1:
            next_start = segments[i+1].split('-')[0]
            duration = time_diff(end, next_start)
        else:
            duration = '00:00:00'

        duration_parts = duration.split(':')
        formatted_duration = ':'.join(
            [part.zfill(2) for part in duration_parts])

        ffmpeg_commands.append(
            f"ffmpeg -y -hwaccel cuda -i {input_file} -c:v copy -c:a copy \
            -ss {end} \
            -t {formatted_duration} -b:v {bitrate} \
            -bufsize:v {bitrate} \
            {output_folder}segment_{i+1}.mp4 -mapmetadata -1")

    return ffmpeg_commands


def main():
    segments = input("Enter the segments (separated by commas): ").split(',')
    input_file = input("Enter the input file: ")
    output_folder = input(
        "Enter output folder (Like ~/Downloads/): ")
    bitrate = input(
        "Enter bitrate, in megabits/s, like 10M (10(Mbit/s)~=10000(Kbit/s) : ")
    ffmpeg_commands = generate_ffmpeg_commands(
        segments, input_file, output_folder, bitrate)
    for command in ffmpeg_commands:
        print(command)
        subprocess.run(command, shell=True)
    with open("inputs.txt", "w") as f:
        for i in range(1, len(segments)+1):
            f.write(f"file '{output_folder}segment_{i}.mp4'\n")
    subprocess.run(f"ffmpeg -y -hwaccel cuda -safe 0 -f concat -i inputs.txt \
                   -c:v copy -c:a copy -b:v {bitrate} \
                   -bufsize:v {bitrate}  \
                   {output_folder}output.mp4 -mapmetadata -1", shell=True)


if __name__ == "__main__":
    main()
