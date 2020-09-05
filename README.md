# **Kalman Filter with Matrix Class**

## Kalman Filter to Smooth Out Noise

### Using Matrix Class Methods to Implement

---

**Kalamn Filter with Matrix Class Project**

The goals / steps of this project are the following:

* Have a working matrix class file to implement the Kalman Filter.
* Generate data to visualize it before implementing Kalman Filter.
* Implement the kalman filter on said data and visualize results.

[//]: # (Image References)

[image1]: ./Result_Images/1.png "1"
[image2]: ./Result_Images/2.png "2"
[image3]: ./Result_Images/3.png "3"
[image4]: ./Result_Images/4.png "4"
[image5]: ./Result_Images/5.png "5"
[image6]: ./Result_Images/6.png "6"

### README

- The implementation of Kalman filter can be found in [project code](./kalman_filter_demo.ipynb). The matrix class code used in the above can be found in [matrix.py](./matrix.py). The below image shows the visualization of the Kalman filter

![alt text][image5]

- Kalman filters are really good at taking noisy sensor data and smoothing out the data to make more accurate predictions. For autonomous vehicles, Kalman filters can be used in object tracking. 

### Steps used to achieve kalman filter.

#### 1. Complete a working matrix file in python to be imported.

A python file containing matrix calculations was created to be imported. Functions included are such as 
- Creates a matrix of zeroes 
- Creates a n x n identity matrix
- Calculates the determinant of a 1x1 or 2x2 matrix
- Calculates the trace of a matrix (sum of diagonal entries)
- Calculates the inverse of a 1x1 or 2x2 Matrix
- Returns a transposed copy of this matrix input
- Defines the behavior of the + operator
- Defines the behavior of - operator (NOT subtraction)
- Defines the behavior of - operator (as subtraction)
- Defines the behavior of * operator (matrix multiplication)

#### 2. Generate Data

* Generate simulation data. Imagine you are in a vehicle and tracking another car in front of you. All of the data you track will be relative to your position. 

  - In this simulation, you are on a one-dimensional road where the car you are tracking can only move forwards or backwards. For this simulated data, the tracked vehicle starts 5 meters ahead of you traveling at 100 km/h. The vehicle is accelerating at -10 m/s^2. In other words, the vehicle is slowing down. 

  - Once the vehicle stops at 0 km/h, the car stays idle for 5 seconds. Then the vehicle continues accelerating towards you until the vehicle is traveling at -10 km/h. The vehicle travels at -10 km/h for 5 seconds. Don't worry too much about the trajectory of the other vehicle; this will be displayed for you in a visualization

  - You have a single lidar sensor on your vehicle that is tracking the other car. The lidar sensor takes a measurment once every 50 milliseconds.

* Visualizing the Tracked Object Distance

  - Shows the object distance over time. You can see that the car is moving forward although decelerating. Then the car stops for 5 seconds and then drives backwards for 5 seconds.

![alt text][image1]

* Visualizing Velocity Over Time

  - The tracked car starts at 100 km/h and decelerates to 0 km/h. Then the car idles and eventually starts to decelerate again until reaching -10 km/h. 

![alt text][image2]

* Visualizing Acceleration Over Time

  - The vehicle declerates at 10 m/s^2. Then the vehicle stops for 5 seconds and briefly accelerates again. 

![alt text][image3]

* Visualizing Lidar Measurements

  - Lidar data is noisy, so the simulator takes ground truth measurements every 0.05 seconds and then adds random noise. The ground truth is shown in red, and you can see that the lidar measurements are a bit noisy.

![alt text][image4]


#### 3. Using a Kalman Filter

The prediction step starts with the second lidar measurement. When the first lidar signal arrives, there is no previous lidar measurement with which to calculate velocity. In other words, the Kalman filter predicts where the vehicle is going to be, but it can't make a prediction until time has passed between the first and second lidar reading.

The Kalman filter has two steps: a prediction step and an update step. In the prediction step, the filter uses a motion model to figure out where the object has traveled in between sensor measurements. The update step uses the sensor measurement to adjust the belief about where the object is.

* Visualizing the Effects of Kalman Filter

  - The chart contains ground turth, the lidar measurements, and the Kalman filter belief. Notice that the Kalman filter tends to smooth out the information obtained from the lidar measurement.

![alt text][image5]

* Visualizing the Velocity

  - One of the most interesting benefits of Kalman filters is that they can give you insights into variables that you cannot directly measured. Although lidar does not directly give velocity information, the Kalman filter can infer velocity from the lidar measurements.

  - This visualization shows the Kalman filter velocity estimation versus the ground truth. The motion model used in this Kalman filter is relatively simple; it assumes velocity is constant and that acceleration a random noise. You can see that this motion model might be too simplistic because the Kalman filter has trouble predicting velocity as the object decelerates.

![alt text][image6]

