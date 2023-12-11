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

This repository houses the source code of a web application designed for bird species classification. It utilizes a deep learning model based on MobileNet architecture (Howard, A.G., et al., 2017) to identify 524 distinct bird species. The application features an intuitive interface that allows for straightforward image uploads and quick species identification.

### Demo

<p align="center">
  <a href="GIF">
    <img src="/video/bird-app524.gif" width="480" alt=""/>
  </a>
</p>

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

### The design

I developed a bird classification web application with three distinct approaches:

-   A 2-stage model using YOLOv8 architecture, <a href="https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git">(source code)</a>;
-   A 1-stage model using MobileNet architectures, <a href="https://github.com/LeoUtas/bird_classification_flask_MobileNet.git">(source code)</a>; and
-   A combination of the YOLOv8 and MobileNet architectures, <a href="https://github.com/LeoUtas/bird_classification_flask_2models.git">(source code)</a>

I chose the MobileNet architecture for the <a href="https://bird-classification524-b310a542793a.herokuapp.com/"> final web application </a> after evaluating different models. Although the YOLO8n object detection feature enhances functionality, it is not critical for this specific task and could potentially reduce performance speed. YOLO8n is therefore excluded from this version. Nevertheless, in situations where object measurement is key, like in the detection and measurement of fish samples, integrating an object detector like YOLO8n can be extremely valuable. This repository includes the source code for the web application.

### How to use the source code

##### Using the source code for development

-   Fork this repository (https://github.com/LeoUtas/bird_classification_flask_MobileNet.git)
-   Get the docker container ready

    -   Run docker build (it might take a while for installing all the required dependencies to your local docker image)

    ```cmd
    docker build -t <name of the docker image> .
    ```

    -   Run the Docker Container (once the docker image is built, you will run a docker container, map it to the port 5000)

    ```cmd
    docker run -p 5000:5000 -v "$(PWD):/app" --name <name of the container> <name of the docker image>
    ```
 

-   Run the app.py on the docker container

    -   For windows users

    ```cmd
    python app.py
    ```

    -   For MacOS and Linux users

    ```bash
    python3 app.py
    ```

    -   Change debug=False to True in app.py for development (it's crucial to asign debug=True for the ease of tracking bugs when customizing the code)

    ```python
    # the last chunk of code in the app.py
    if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5000)
    )  # define port so we can map container port to localhost
    app.run(host="0.0.0.0", port=port, debug=False)  # define 0.0.0.0 for Docker
    ```

-   Stop running the container when you're done:

    ```cmd
    docker stop <name of the container>
    ```

### The bottom line

I'm thrilled to share it with you all! Dive in and enjoy exploring its features. A big thank you for your interest and for journeying this far with me. Wishing you a fantastic day ahead!

Best,
Hoang Ng

### Reference

Howard, A.G. et al., 2017. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. CoRR, abs/1704.04861. Available at: http://arxiv.org/abs/1704.04861.
