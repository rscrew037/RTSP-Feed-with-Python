import cv2

# RTSP info -- change these 4 values according to your RTSP URL
username = 'USERNAME'
password = 'PASSWORD'
endpoint = 'ENDPOINT'
ip = 'IPADDRESS'

# Stream
stream = cv2.VideoCapture(f'rtsp://{username}:{password}@{ip}/{endpoint}')

try:
    while True:
        # Read the input live stream
        ret, frame = stream.read()
        height, width, layers = frame.shape
        frame = cv2.resize(frame, (width // 2, height // 2))

        # Show video frame
        cv2.imshow("My IP cam", frame)

        # Quit when 'x' is pressed
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
except Exception as e:
    print("ERROR:", e)

# Main function
if __name__ == "__main__":
    # Release and close stream
    stream.release()
    cv2.destroyAllWindows()
