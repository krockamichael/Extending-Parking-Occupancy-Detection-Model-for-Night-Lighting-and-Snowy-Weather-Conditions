# Extending Parking Occupancy Detection Model for Night Lighting and Snowy Weather Conditions
Author: Bc. Michael Kročka

Car parks today are usually monitored by camera systems in conjunction with ground or thermal sensors, in some cases a single person can be enough to monitor a small parking lot. In other cases, where the car parks are bigger and such options are not possible or would be very costly, new solutions are taken into consideration. One such solution is the use of an already in place commercial camera system, which would be enhanced by neural networks which can be trained for parking space classification in real-time. The solution would have to be low-cost to deploy and possibly maintain, reliable, and easy to use.

This diploma thesis deals with the problem of parking lot monitoring, classification of parking spaces as empty or occupied, and the automatic detection of license plate registration numbers using deep learning techniques. The process of identifying a parking space as occupied or empty would start with the segmentation of each parking space, then would continue with object detection within an isolated segment, and lastly, the process for identification of the license plate would start. This process consists of detecting the license plate, segmenting each character, and identifying it.


1. Creation of new dataset - SvJur
2. Transfer learning of mAlexNet using SvJur, PKLot, CNRParkAB, CNRParkEXT
3. License plate detection & recognition pipeline
4. Raspberry Pi smart camera web application