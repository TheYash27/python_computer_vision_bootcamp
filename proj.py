# to use comp. vis. in my project
import cv2
# to use numpy in my project
import numpy as np
# to load video 
video = cv2.VideoCapture("grescrvid.mp4")
# to load image
image = cv2.imread("background.jpg")
while True:
  # if there is any error while loading the video,
  # ret = false and I'll come out of the while loop
  # else, frame would now hold contents of the video 
  ret, frame = video.read()
  # to convert the colours in frame from
  # BGR (Blue, Green, Red) format to
  # HSV (Hue, Saturation, Volume) format
  hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # lightest shade of green present in the video
  l_g = np.array([32, 94, 132])
  # darkest shade of green present in the video
  u_g = np.array([179, 255, 255])
  # removing the green screen from the BG by masking it
  mask = cv2.inRange(hsv, l_g, u_g)
  # resultant frame after green BG has been masked
  masked_frame = cv2.bitwise_and(frame, frame, mask=mask)
  # to keep the FG while removing the green BG
  pre_final_frame = frame - masked_frame
  # replace black BG with my image
  final_frame = np.where((pre_final_frame == 0), image, pre_final_frame) 
  # to play the video
  cv2.imshow('final_frame', final_frame)
  # to stop playing the video
  k = cv2.waitKey(1)
  # if 'q' or 'Q' is pressed,
  # stop playing the video
  if (k == ord('q')):
    # to come out of the while loop 
    break
  # de - allocates the memory taken up by the video
  video.release()
  # closes the window in which the video was running
  cv2.destroyAllWindows()