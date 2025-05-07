This Python program uses your webcam to detect and compare colors in real-time using OpenCV.

It combines two main features:
- **Color Detection:** Detects and displays the color at the center of the webcam feed.
- **HSV Color Picker:** Allows you to select a color using HSV sliders to compare with the detected color.

If the selected color matches the center color (within a small threshold), it will display `Match`.  
If they are different, it will display `No Match`

--- 

### Prerequisites

- Python 3.x
- OpenCV (`cv2`)
