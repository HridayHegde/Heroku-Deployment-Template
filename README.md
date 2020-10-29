<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Last Commit][last-activity-shield]][last-activity-url] <br />
[![LinkedIn][linkedin-shield]][linkedin-url]
<!--[![MIT License][license-shield]][license-url]-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/HridayHegde/Heroku-Deployment-Template">
    <img src="Rimages/logo.png" alt="Logo" >
  </a>

  <h3 align="center">HEROKU Deployment Template</h3>

  <p align="center">
    A quickstart path to all your hosting needs on Heroku!
    <!--<br />
    <a href="https://github.com/HridayHegde/Heroku-Deployment-Template"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <a href="https://github.com/HridayHegde/Heroku-Deployment-Template">View Demo</a>
    ·
    <a href="https://github.com/HridayHegde/Heroku-Deployment-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/HridayHegde/Heroku-Deployment-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Template](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)<!--* [Roadmap](#roadmap)-->
* [Contributing](#contributing)<!--* [License](#license)-->
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Template

<p align="center">
  <a href="https://github.com/HridayHegde/Heroku-Deployment-Template">
    <img src=Rimages/HerokuWordArt.png alt="Logo" >
  </a> <!--[![Product Name Screen Shot][product-screenshot]](https://example.com) --></p>

There are many Heroku templates out there, but none of those fit my bill so i've made one that'll conquer them all :D. <!-- LOL -->
Here's why:
* Your time needs to be focused on writing some powerfull code and not making some random files for deployment.
* Really? wanna keep making that one sweet template each time you wanna deploy on heroku?.

Though sometimes this wont work out for everyone, so ill keep adding stuff here so that its a "One for all"(MHA) solution.

### Built With

* [Heroku](https://heroku.com/)

* [Notepad++?](https://notepad-plus-plus.org/)



<!-- GETTING STARTED -->
## Getting Started
First things first, this template is configured to host an app dyno which allows you to host REST API's and flask frontends on Heroku. You can modify this template to run a Worker dyno by editing the procfile to ``` worker:python_filename.py``` . Many templates and/or documentations are available online for the same. Though i'll try to get you up to speed with the basics.

### Prerequisites

Before we begin, you need a couple of things installed...
* Download and Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and type the following to log into your heroku account ```heroku login ```. 
* Download and Install [git](https://git-scm.com/downloads)

After Downloading git, you can run these commands to set your **username** and **password**.
(Or if you are as lazy as me you will get a web UI on your first push or pull)
```
git config --global user.email "your_email_address@example.com" 
git config user.password "your password" 
``` 
<!--```sh
npm install npm@latest -g
```-->

### Installation

1. Scroll to the top of this page, and click on the **Use This Template** button to create your own repo using this template.
2. Connect the remote repo to your local machine using ``` git remote add origin <remote-repo-url> ```

<!-- USAGE EXAMPLES -->
## Usage

### As a REST API
1. Edit the ***app.py*** file in the repo to add your own python scripts. 
2. If you've used any external packages you need to mention them in the ***requirements.txt*** file. 
3. If you've changed the name of the file in **Step 1** then you need to edit it in the ***Procfile*** as well.
```web: gunicorn app:python_file_name```
4. The ***Aptfile*** included in the template is an optional file where you can mention things to be installed via the linux apt-get cmd(More on this later)
5. Delete the commented code inside ***""""""***
6. To deploy to heroku, follow the usual steps for any heroku deployment.
```
git add.
git commit -m"Cheesy Commit line"
heroku create
git push heroku master
```
7. Now, once deployed, you can access the REST API via the given link on the browser interface. It will be ready to recieve requests.


### As a Flask Web App
1. Delete all non commented code in ***app.py***.
2. Uncomment all the commented code under ***""""""*** and ***#***.
3. If you've used any external packages you need to mention them in the ***requirements.txt*** file. 
4. If you've changed the name of the file in **Step 1** then you need to edit it in the ***Procfile*** as well.
```web: gunicorn app:python_file_name```
5. The ***Aptfile*** included in the template is an optional file where you can mention things to be installed via the linux apt-get cmd(More on this later)

6. To deploy to heroku, follow the usual steps for any heroku deployment.
```
git add.
git commit -m"Cheesy Commit line"
heroku create
git push heroku master
```
7. Now, once deployed, you can access the Flask App via the given link in the browser interface.



## Advanced Options (Optional Content)
1. The ***Aptfile*** is an optional file which you can choose to keep in your project.
2. To configure Heroku to understand this file you need to add a buildpack to it via the web interface.
    ### Adding a Buildpack
    1. Go to your heroku app via the dashboard.
    2. Go to the settings tab.
    3. Scroll down and press Add a Buildpack.
    4. Add ```https://github.com/heroku/heroku-buildpack-apt``` to it, and save changes. 
2. With this you can run commands that require the linux cmd ```sudo apt-get``` command.
3. In the example file included i am installing ***Tesseract OCR*** which uses this command.
<!-- ROADMAP 
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).

-->

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be, learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE` for more information.
-->


<!-- CONTACT -->
## Contact

Hriday Hegde - [@HridayHegde](https://www.linkedin.com/in/hridayhegde/) - hridayhegde1999@gmail.com

Project Link: [https://github.com/HridayHegde/Heroku-Deployment-Template](https://github.com/HridayHegde/Heroku-Deployment-Template)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Heroku](https://heroku.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
<!--* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)-->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[last-activity-shield]: https://img.shields.io/github/last-commit/HridayHegde/Heroku-Deployment-Template?style=flat-square
[last-activity-url]: https://github.com/reubence
[contributors-shield]: https://img.shields.io/github/contributors/HridayHegde/Heroku-Deployment-Template.svg?style=flat-square
[contributors-url]: https://github.com/HridayHegde/Heroku-Deployment-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HridayHegde/Heroku-Deployment-Template.svg?style=flat-square
[forks-url]: https://github.com/HridayHegde/Heroku-Deployment-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/HridayHegde/Heroku-Deployment-Template.svg?style=flat-square
[stars-url]: https://github.com/HridayHegde/Heroku-Deployment-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/HridayHegde/Heroku-Deployment-Template.svg?style=flat-square
[issues-url]: https://github.com/HridayHegde/Heroku-Deployment-Template/issues
[license-shield]: https://img.shields.io/github/license/HridayHegde/Heroku-Deployment-Template.svg?style=flat-square
[license-url]: https://github.com/HridayHegde/Heroku-Deployment-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/hridayhegde/
[product-screenshot]: https://lh3.googleusercontent.com/proxy/l3Fi5jqPd6axyq2qRIgC_LqGaQgY4TplQuqMBctQlzhH2wEidEIbA2BNpVOrSC7idwzDB6G_pm-tLvZMbJa6BVznty5hQH7XlSWe4XjbHO_tAgO7H7o4-3IUERI6Kqgs
