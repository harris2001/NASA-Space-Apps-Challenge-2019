## NASA-Space-Apps-Challenge-2019
A complete repository for my project "Guessing Master" for the NASA Space Apps Challenge 2019
## The Idea:
In order to understand our origination and answer some of the most fundamental questions about the universe, humanity needs to utilize the prominent technology of 3d printing satellites from exoplanetary materials. Gigantic 3d printers need to be sent to exoplanets to exploit the raw materials located there so that to create new satellite telescopes and more printers that can either orbit the exoplanet or continue their travel further away. The capabilities of this 3d-printer-satellite network can be tremendous! The development of such a web can refine (or potentially overhaul) our perception of the universe. To make this project scalable and sustainable, printers need to be enhanced with Artificial Intelligence in order to be able to overcome any obstacle without the assistance of the human factor.
## The problem:
Sending these data to a machine seven to a hundred or even trillion light-years away needs the analogous time. Background radiation and any radiation originating from the space disrupts and adds noise to the data sent. Moreover, while sending or receiving the data, any component malfunctions on the printer or the station can create gaps in the data received. Since there is no excess of time available or capital, an intelligent machine has to be created, so that to supervise the process from the beginning.
## The solution:
Guessing master is a complete model, ready to be trained by millions of NASA's 3d object models so that to be able to provide the printer with the best approach to the original model sent by the station/the ground.
How does it work:
The "Master" is a system of two Neural Networks: one Neural Network Firstly, the "Master" performs a Fast Fourier Transformation on the data received by the printer. The frequencies are then separated and the object becomes more clear.
We interpret the 3D objects as a combination of shapes and we feed them in the machine as a matrix input. These images are then used as samples to create a probability distribution, which will allow us to determine the best choice for filling any missing parts in the object. To fill these gaps, we need to gain as much information as we can from the context close to the missing area and also to develop an artificial perception of the image as a whole. We use an adversarial training method -also known as GAN (Generative Adversarial Networks)- where two functions will fight against each other to force the machine to create an artificial substitute that will be both plausible and natural to human understanding. The machine learning model has been trained before so that it can understand the features of some 3d printable objects, by thousands of 3d model objects and shapes, and it has created a distribution of reference. By scanning through a particular image, the machine can decide which features are missing and thus try to regenerate them, based on the new and the distribution of reference. Our deep convolutional neural network is finally able to reconstruct the objects by approximating the original object.


Initial Image, after been exposed to electromagnetic radiation:
![Screenshot (101)](https://user-images.githubusercontent.com/29304550/67232350-db447f00-f449-11e9-9b4f-79a7f5f23ed9.png)

Image After Fast Fourier Transformation:
![Screenshot (102)](https://user-images.githubusercontent.com/29304550/67232931-fb287280-f44a-11e9-9cd2-46cd9b1bf9f2.png)

the .webm videos show  how this is done and how 3d objects are passed to the convolutional network later.

The Deep Convolutional Generative Adversarial Network is trained by a load of samples so that to create a distribution of reference. Then two functions are "fighting" against each other. Function G is trying to cover any missing parts of the 3d object by looking up the reference distribution. The D function is the "Detective" that prohibits the G to fill the gap if the nearby area doesn't look "natural" to human understanding. By having the two fighting against each other, the result is plausible and logical.

*Due to lack of 3d models I used 2d Images to train the Master. If an API is provided, then by using the "The Master" can also perform a scan on the 3rd dimention and extract the features of the object.

My presentation:
https://www.dropbox.com/s/b6i728ebsokk4q0/Presentation%204.pptx?dl=0
