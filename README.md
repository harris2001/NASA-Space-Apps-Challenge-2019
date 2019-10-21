# NASA-Space-Apps-Challenge-2019
A complete repository for my project "Guessing Master" for the NASA Space Apps Challenge 2019 

## The Idea:

3D printing is one of the most prominent technologies that humanity will need so that to evolve by collect more information about the vast universe. The gigantic 3d printers that will be sent to exoplanets can exploit the raw materials located there so that to create new satellite telescopes and more printers that can either orbit the exoplanet or continue their travel further away. The capabilities of this 3d-printer-satellite network can be tremendous! The development of such a web can give an exponential rise to our perception of this bizarre universe. To have this web up and working, 3d object models must be created on Earth and then to transmit them to the net.

## The problem:

Sending these data to a machine seven to a hundred or even trillion light-years away needs the analogous time.  Background radiation and any radiation originating from the space disrupt and add noise to the data sent.  Moreover, while sending or receiving the data, any component malfunctions on the printer or the station can create holes in the object. Since there is no excess of time available or capital, an intelligent machine has to be created, so that to supervise the process from the beginning.

## The solution:

Guessing master is a complete model, ready to be trained by million of NASA's 3d object models so that to be able to provide the printer with the best approach to the original model sent by the station/the ground.

## How does it work:

The "Master" is a system of two Neural Networks: one Neural Network 
Firslty, the "Master" performs a Fast Fourier Transformation on the data received by the printer. The frequencies are then separated and the object becomes more clear.

The object is firstly sliced in multiple 2d images and then the transformation is applied

Initial Image, after been exposed to electromagnetic radiation:
![Screenshot (101)](https://user-images.githubusercontent.com/29304550/67232350-db447f00-f449-11e9-9b4f-79a7f5f23ed9.png)

Image After Fast Fourier Transformation:
![Screenshot (102)](https://user-images.githubusercontent.com/29304550/67232931-fb287280-f44a-11e9-9cd2-46cd9b1bf9f2.png)

the .webm videos show  how this is done and how 3d objects are passed to the convolutional network later.

The Deep Convolutional Generative Adversarial Network is trained by a load of samples so that to create a distribution of reference. Then two functions are "fighting" against each other. Function G is trying to cover any missing parts of the 3d object by looking up the reference distribution. The D function is the "Detective" that prohibits the G to fill the gap if the nearby area doesn't look "natural" to human understanding. By having the two fighting against each other, the result is plausible and logical.

*Due to lack of 3d models I used 2d Images to train the Master. If an API is provided, then by using the "The Master" can also perform a scan on the 3rd dimention and extract the features of the object.

My presentation:
https://www.dropbox.com/s/b6i728ebsokk4q0/Presentation%204.pptx?dl=0
