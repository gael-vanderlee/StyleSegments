<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

docker build . --tag style:latest

docker run  --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 --gpus all -it --entrypoint bash style:latest 



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a 
    href="https://github.com/Gvanderl/StyleSegments">
  </a>

  <h3 align="center">StyleSegments</h3>

  <p align="center">
    Apply style transfer selectively on certain objects of an image
    <br />
    <a href="https://github.com/Gvanderl/StyleSegments"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Gvanderl/StyleSegments">View Demo</a>
    ·
    <a href="https://github.com/Gvanderl/StyleSegments/issues">Report Bug</a>
    ·
    <a href="https://github.com/Gvanderl/StyleSegments/issues">Request Feature</a>
  </p>




<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to use the best models in image segmentation and neural style transfer to selectively 
apply style transfer on certain objects or parts of an image.

Input Image             |Input Style                | Output image
:----------------------:|:-----------------------:|:----------------:
<img src="https://raw.githubusercontent.com/Gvanderl/StyleSegments/master/input/images/cat.jpg" width="500" />|<img src="https://raw.githubusercontent.com/Gvanderl/StyleSegments/master/input/styles/cartoon.jpg" width="350"/>|<img src="https://raw.githubusercontent.com/Gvanderl/StyleSegments/master/output/combined/cat_cartoon.jpeg" width="500" />






<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* For virtual envs: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)
  ```sh
  pip install --user pipenv
  ```
Or use your virtual environment manager of choice, requirements are in the [Pipfile](Pipfile)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Gvanderl/StyleSegments.git
   ```
2. Install packages
   ```sh
   pipenv install
   ```
3. Run the script
    ```sh
    pipenv shell
    pipenv main.py
    ```


<!-- USAGE EXAMPLES -->
## Usage

To change the images to process, models used, or the classes to stylize all you have to do is change the variable in [config.py](config.py)
In our example, we have:
```python
images = ["cat.jpg"]

ims_config = {
    "cat.jpg": {
        "seg_models": ["VOC"],
        "styles": ["cartoon.jpg"],
        "class": [8]
    }
}
```
The images names in the `images` list will be processed according to their config in `ims_config`. 
* `seg_models` are the models to try on this image for segmentation. As of now, the supported models are "ADE20k", "Cityscapes" and "VOC":
* `styles` are the styles images to try on this image found in [input/styles](input/styles).
* `class` is the class to stylize for each model, this is model dependent. Here, for the VOC model, class 8 is cats.

All the input and output paths and folder can also be found and modified in [config.py](config.py).

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Gvanderl/StyleSegments/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Gvanderl/StyleSegments](https://github.com/Gvanderl/StyleSegments)

### Acknowledgements

* [Image Segmentation Keras](https://github.com/divamgupta/image-segmentation-keras)
* [Image Style Transfer Using Convolutional Neural Networks](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)
* [VGG19](https://arxiv.org/abs/1409.1556)
* [Style transfer DNNs](https://github.com/LaurentVeyssier/Style-transfer-with-Deep-Neural-Network)


[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/ga%C3%ABl-van-der-lee-731b26143/]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Gvanderl/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/Gvanderl/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Gvanderl/repo.svg?style=for-the-badge
[forks-url]: https://github.com/Gvanderl/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/Gvanderl/repo.svg?style=for-the-badge
[stars-url]: https://github.com/Gvanderl/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/Gvanderl/repo.svg?style=for-the-badge
[issues-url]: https://github.com/Gvanderl/repo/issues
[license-shield]: https://img.shields.io/github/license/Gvanderl/repo.svg?style=for-the-badge
[license-url]: https://github.com/Gvanderl/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[https://www.linkedin.com/in/ga%C3%ABl-van-der-lee-731b26143/]: https://linkedin.com/in/Gvanderl
