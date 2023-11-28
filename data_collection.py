from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (4092,4092)}))
picam2.start_preview(Preview.QTGL)
picam2.start()

try:
    label = input("Enter the label for the images: ")
    count = 1
    while True:
        # Wait for the user to press Enter
        input("Press Enter to capture an image (press Ctrl+C to exit):")
        
        # Capture an image with a sequentially increasing filename
        file_name = f"{label}{count}"
        picam2.capture_file(f"{file_name}.jpg")
        print(f"Image captured and saved as {file_name}.jpg")
        count += 1

except KeyboardInterrupt:
    print("\nExiting the program")
finally:
    # Clean up resources
    picam2.close()
