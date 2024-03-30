<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li><a href="#data-source">Data source</a></li>
    <li><a href="#the-design">The design</a></li>
    <li><a href="#how-to-use-the-source-code">How to use the source code</a></li>
    <li><a href="#the-bottom-line">The Bottom Line</a></li>
    <li><a href="#reference">Reference</a></li>
  </ol>
</details>

### Introduction

<ul style="padding-left: 20px; list-style-type: circle;">
        <li>The project includes 4 repositories:
            <ul>                
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_research.git" style="text-decoration: none; color: #3498db;">Bird classification research</a>
                </li>
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_flask_MobileNet.git" style="text-decoration: none; color: #3498db;">Bird classification web application using MobileNet model</a>
                </li>
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git" style="text-decoration: none; color: #3498db;">Bird classification web application using YOLOv8 model</a>
                </li>
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_flask_2models.git">Bird classification web app using MobileNet and YOLOv8 for better comparing model performances</a>
                </li>                                
            </ul>
        </li>
        <br>
        <li>
            I attempted to solve the task using 4 different tools (i.e., InceptionV3, MobileNetV1, MobileNetV2 and YOLOv8). After evaluating performance metrics and processing speed, YOLOv8 was chosen as the most suitable model for this task.
        </li>        
    </ul>

This repository offers source code for the backend of the <a href="https://github.com/LeoUtas/bird_classification_react-native.git">Bird Classification IOS app</a>. Although the name of the repository can be confusing because MobileNet was the model of choice for this task before, after testing the speed performance and other aspects, I decided to make YOLOv8 the chosen model.

### Data source

This project utilizes a bird species dataset provided by <a href="https://www.kaggle.com/gpiosenka">Gerry</a>, available on Kaggle. For detailed information, visit <a href="https://www.kaggle.com/datasets/gpiosenka/100-bird-species/data"> birds 525 species- image classification </a>.

### How to use the source code

##### Use the source code

-   Fork/clone this repository (https://github.com/LeoUtas/bird_classification_flask_MobileNet.git)
-   Get the docker container ready

    -   Run docker build (name the app whatever you want on your local machine, and please note that it might take a while for installing all the required dependencies to your local docker image)

    ```cmd
    docker build -t <name of the app> .
    ```

    -   Run the Docker Container (once the docker image is built, you will run a docker container, map it to the port 5000)

    ```cmd
    docker run -p 5000:5000 -v "$(PWD):/app" --name <name of the container> <name of the app>
    ```

I'm thrilled to share it with you all! Dive in and enjoy exploring its features. A big thank you for your interest and for journeying this far with me. Wishing you a fantastic day ahead!

Best,
Hoang Ng

### Reference

Howard, A.G. et al., 2017. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. CoRR, abs/1704.04861. Available at: http://arxiv.org/abs/1704.04861.
