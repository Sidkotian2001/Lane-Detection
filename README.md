As part of the Intelligent Ground Vehicle Competition (IGVC), Michigan, I have worked on a lane detection model for UGV navigation. As per the rules of the competition, a UGV has to navigate between two white lines on a grassy path with obstacles like barrels, cones, potholes, etc in its way. For the robot to stay within the white lines it has to detect them accurately in real-time. 

As part of team RUGVED Systems, I build a model to detect the lanes using OpenCV. 
To test the model, the team painted white lines on the grass and filled the lane with cones. After that, we recorded a video which simulates UGV navigation within the white lines.

Working :-
A rectangular region of the image is chosen preferably the bottom half of the image. This removes any unnecessary background objects like trees, people, vehicles, etc. from coming into the frame.
Video is converted from RGB to HSV colourspace since HSV colourspace is invariant to changes in intensity which is useful for the detection of individual colours. 
Using colour masking and bitwise operations, the green colour of the grass was detected and masked from the video. The resulting video is binary where low represents the colour masked and the high represents the rest.
Used Median and Gaussian blurring to soothe the image. 
Used Morphological operations to increase the size of the detected lines and reduce the noise to a minimum. 
Canny Edge detection to detect the edges in the video. 
Hough Transform to detect the lines by specifying the maximum gap between two adjacent pixels and the minimum length of the line to be detected.

The entire model is capably detecting continuous lines of varying slopes with high accuracy. The parameters of the model for colour detection, canny edge detection and hough transform can be easily changed if needed. A similar model works on the saturation region of HSV since the saturation value of white lines differs quite a bit from that of grass. 

The primary reason behind not using deep learning to detect the white lanes is that neural networks are computationally more expensive and slower in real time. Besides that, any change to the lanes like a change in colour or unexpected weather conditions like rain or clouds will highly affect the accuracy of detection of the lanes.

What I learned from this project is that lane detection on a grassy path is more complicated than on an asphalt path since the white lanes on the roads are highly contrasting with the background making detection easier. On the other hand, white lines which are painted on grass have lower illumination which does not contrast much with the grass. Furthermore, the thickness of the lanes is smaller than that on roads due to which we must be careful when applying blurring and morphological operations because it might reduce the size of the lines detected.
