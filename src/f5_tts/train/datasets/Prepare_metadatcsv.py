import os
import csv

# Define paths to the folders
wav_folder = "/media/zaheen/HD_11/VC_urdu/Urdu/wavs"
transcript_folder = "/media/zaheen/HD_11/VC_urdu/Urdu/Transcripts"
output_csv_path = "/media/zaheen/HD_11/VC_urdu/Urdu/metadata.csv"

# Get sorted list of files from both folders
wav_files = sorted(f for f in os.listdir(wav_folder) if f.endswith(".wav"))
transcript_files = sorted(f for f in os.listdir(transcript_folder) if f.endswith(".txt"))

# Ensure the folders contain matching files
if len(wav_files) != len(transcript_files):
    print("Error: Number of audio files and transcript files do not match!")
    exit()

# Create the metadata.csv file
with open(output_csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter="|")
    csv_writer.writerow(["audio_file", "text"])

    for wav_file, transcript_file in zip(wav_files, transcript_files):
        # Ensure the file names match (excluding extensions)
        if os.path.splitext(wav_file)[0] != os.path.splitext(transcript_file)[0]:
            print(f"Error: Mismatched files {wav_file} and {transcript_file}")
            exit()

        # Read the transcript text
        transcript_path = os.path.join(transcript_folder, transcript_file)
        with open(transcript_path, "r", encoding="utf-8") as f:
            transcript = f.read().strip()

        # Write the relative path to the wav file and the transcript to the CSV
        wav_relative_path = os.path.join("wavs", wav_file)
        csv_writer.writerow([wav_relative_path, transcript])

print(f"Metadata.csv has been created successfully at {output_csv_path}")
