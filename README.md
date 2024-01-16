<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#technical-tools">Technical Tools</a></li>
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
            I attempted to solve the task using 4 different tools (i.e., InceptionV3, MobileNetV1, MobileNetV2 and YOLOv8). After evaluating performance metrics and processing speed, MobileNetV1 was chosen as the most suitable model for this task <a href="https://bird-classification524-b310a542793a.herokuapp.com/">(visit the live demo)</a>.
        </li>
        <br>
        <li>
            Although the YOLO8n object detection feature enhances functionality, it is not critical for this specific task and could potentially reduce performance speed. YOLO8n is therefore excluded from this version. Nevertheless, in situations where object measurement is key, like in the detection and measurement of fish samples, integrating an object detector like YOLO8n can be extremely valuable. This repository includes the source code for the web application.
        </li>        
    </ul>

This repository offers source code for a web application using MobileNetV1 <a href="https://bird-classification524-b310a542793a.herokuapp.com/">(visit the live demo)</a>.

### Demo

<p align="center">
  <a href="GIF">
    <img src="/video/bird-app524.gif" width="480" alt=""/>
  </a>
</p>

Try a live version: <a href="https://bird-classification524-b310a542793a.herokuapp.com/"> Demo </a>

### Technical tools

The orginal paper of MobileNet <a href="https://arxiv.org/pdf/1704.04861.pdf">(Howard, A.G. et al., 2017)</a>.

The application documentation of <a href="https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet/MobileNet"> MobileNet </a> using TensorFlow v2.14.0.

-   TensorFlow
-   numpy
-   pandas
-   Flask
-   JavaScript (plain)
-   HTML
-   CSS (Bootstrap)
-   Docker
-   Github Action

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
