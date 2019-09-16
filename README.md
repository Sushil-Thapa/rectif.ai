# Rectif.ai

Making the world a better place one posture at a time. 

## Running the system

- Create a virtual environment using the `requirements.txt` file
- Download [models](https://drive.google.com/drive/folders/1bdGLkvHFLdwb1hIJ1dMQCjYTDbGsEemF?usp=sharing) 
- Run `python -m rectifai.predictors.demo_webcam`

## Inspiration

In today’s world, our work requires us to be sitting for a lot of the time. Failing to maintain good posture can thus, cause a variety of health problems related to our lungs, digestion, bones, and so on and so forth. Furthermore, bad posture habits are pretty common and it can be difficult breaking away from them without much deliberate effort. 

## What it does

The app helps develop good posture habits by making people mindful about their postures when they are in front of the screen. 

## How We built it

We used a Pytorch implementation of PoseNet to detect key-points. The points are then passed onto another network that classifies it into good or bad posture.

## Challenges we ran into

- no proper bad posture dataset, so chose a different domain problem and tweaked into our use case
- Infrastructure needed for best results. Didn't have good machines so used mobilenet for the posenet  and Linear neuron networks for detection because of its speed and accuracy compared to size of models and infrastructure required.

## What's next for Rectif.ai

- Training on more data for more accurate results
- Addition of feature to get analytics for posture over a period of time
- Monitoring from different angles

