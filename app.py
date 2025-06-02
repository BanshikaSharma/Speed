import cv2
import numpy as np

# Constants
FPS = 30 
REFERENCE_DISTANCE = 5.0 
PIXEL_DISTANCE = 100  


def calculate_speed(pixel_distance):
   
    meters_per_pixel = REFERENCE_DISTANCE / PIXEL_DISTANCE
    distance_in_meters = pixel_distance * meters_per_pixel
    speed_mps = distance_in_meters * FPS  
    return speed_mps


video_path = 'mediaplayer.mp4'  
cap = cv2.VideoCapture(video_path)


prev_frame = None
prev_position = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

   
    edges = cv2.Canny(blurred_frame, 50, 150)

   
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: 
            x, y, w, h = cv2.boundingRect(contour)
            center_position = (x + w // 2, y + h // 2)

            if prev_position is not None:
               
                pixel_distance = np.linalg.norm(np.array(center_position) - np.array(prev_position))
                speed = calculate_speed(pixel_distance)
                
                
                speed_text = f'Speed: {speed:.2f} m/s'
                
                
                (text_width, text_height), _ = cv2.getTextSize(speed_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                background_rect = (10, 10, text_width + 20, text_height + 20)  
                
                
                cv2.rectangle(frame, (background_rect[0], background_rect[1]), 
                              (background_rect[0] + background_rect[2], background_rect[1] + background_rect[3]), 
                              (0, 0, 0), -1)  

                
                cv2.putText(frame, speed_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

           
            prev_position = center_position

           
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    cv2.imshow('Car Racing Speed Analysis', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
