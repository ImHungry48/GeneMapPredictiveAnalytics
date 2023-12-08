<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<div align="center">
  <a href="https://github.com/ImHungry48/GeneMapPredictiveAnalytics">
    <img src="client/public/thumbnail_image.png" alt="Logo" width="100" height="100">
  </a>


  <h1 align="center">Gene Map Predictive Analytics </h1>

  <p align="center">
    Revoltionizing Healthcare with Predictive Analytics
    <br />
    <a href="https://github.com/ImHungry48/GeneMapPredictiveAnalytics"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="">View Demo</a> -->
    <!-- · -->
    <a href="https://github.com/ImHungry48/GeneMapPredictiveAnalytics/issues">Report Bug</a>
    ·
    <a href="https://github.com/ImHungry48/GeneMapPredictiveAnalytics/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About GeneMap</a>
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
    <!-- <li><a href="#usage">Usage</a></li> -->
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## About GeneMap

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Welcome to the GeneMap repository! GeneMap is a app created by students in the Johns Hopkins Computational Genomics: Sequences class as our final project.

Add more here!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<!-- This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples. -->

[![React][React.js]][React-url]
[![Express][Express.js]][Express-url]
[![Flask][Flask.js]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy of the app running, follow the below steps.

### Prerequisites

* Node.js
* npm
* Clang or another method of running C code
* Python3
  * pip

### Installation

1. Install the prerequistes:

  * Clang or another method of running C code
  * Npm:
    * Install npm (requires Node.js): https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

    * Update npm:
      ```sh
      npm install npm@latest -g
      ```
  * Python3 packages:
    ```sh
    python3 -m pip install -r requirements.txt
    ```
  
2. Make the minimap2 executable:
    ```sh
    cd minimap2-master
    make
    cd ..
    ```

 
3. Navigate to the client folder
    ```sh
    cd client
    ```

4. Install NPM packages
    ```sh
    npm install
    ```

5. Build the dist files while navigated to the `client` folder
    ```sh
    npm run build
    ```

6. Start the server (starts express automatically) (while navigated to the `client` folder)
    ```sh
    node ../index.js
    ```    

7. Start the Flask application (while navigated to the `client` folder)
    ```sh
    python3 ../app.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
<!-- ## Usage -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**!

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Github Links:
- [darinkhan](https://github.com/darinkhan)
- [Jlimb26](https://github.com/Jlimb26)
- [ImHungry26](https://github.com/ImHungry48)
- [subhasrivijay](https://github.com/subhasrivijay)

</br>

Project Link: [https://github.com/ImHungry48/GeneMapPredictiveAnalytics](https://github.com/ImHungry48/GeneMapPredictiveAnalytics)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thank you to all the mentors that have helped us throughout this project! We would in particular like to thank our professor, Benjamin Langmead, and all our TAs.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ImHungry48/GeneMapPredictiveAnalytics.svg?style=for-the-badge
[contributors-url]: https://github.com/ImHungry48/GeneMapPredictiveAnalytics/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ImHungry48/GeneMapPredictiveAnalytics.svg?style=for-the-badge
[forks-url]: https://github.com/ImHungry48/GeneMapPredictiveAnalytics/network/members
[stars-shield]: https://img.shields.io/github/stars/ImHungry48/GeneMapPredictiveAnalytics.svg?style=for-the-badge
[stars-url]: https://github.com/ImHungry48/GeneMapPredictiveAnalytics/stargazers
[issues-shield]: https://img.shields.io/github/issues/ImHungry48/GeneMapPredictiveAnalytics.svg?style=for-the-badge
[issues-url]: https://github.com/ImHungry48/GeneMapPredictiveAnalytics/issues
[license-shield]: https://img.shields.io/github/license/ImHungry48/GeneMapPredictiveAnalytics.svg?style=for-the-badge
[license-url]: https://github.com/ImHungry48/GeneMapPredictiveAnalytics/blob/master/LICENSE.txt

[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Express.js]: https://img.shields.io/badge/Express.js-404D59?style=for-the-badge
[Express-url]: https://expressjs.com/
[Flask.js]: https://img.shields.io/badge/Flask-20232A?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
