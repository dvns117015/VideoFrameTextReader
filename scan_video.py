import cv2
import pytesseract
import os

# Set the correct path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to scan the first frame of a video for a specific date
def scan_video_for_date(video_path, target_date):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return False

    # Read the first frame
    ret, frame = cap.read()
    if not ret:
        print(f"Could not read frame from video: {video_path}")
        cap.release()
        return False

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply OCR to the frame
    text = pytesseract.image_to_string(gray_frame)
    if target_date in text:
        cap.release()
        return True

    cap.release()
    return False

# Main function to scan multiple videos
def scan_videos_in_directory(directory, target_date):
    video_files = [f for f in os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    videos_with_date = []

    for video_file in video_files:
        video_path = os.path.join(directory, video_file)
        print(f"Scanning {video_file}...")
        if scan_video_for_date(video_path, target_date):
            videos_with_date.append(video_file)

    return videos_with_date

# Directory containing videos
video_directory = r'E:\VIDEO\New Case\Video'
# Date to search for
target_date = '2024/03/12'

# Scan videos and get the list of videos containing the target date
matching_videos = scan_videos_in_directory(video_directory, target_date)

# Print the results
if matching_videos:
    print("Videos containing the date:", target_date)
    for video in matching_videos:
        print(video)
else:
    print("No videos found containing the date:", target_date)
