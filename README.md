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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
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
* homebrew
* expo [can be run using npx]
* Watchman
* Expo Go application on your mobile device (available on both iOS and Android Play Store)

### Installation

1. Install the prerequistes:
  
 * Install the Expo Go application on your mobile device from the Google Play Store or Apple App Store

  * Npm:
    * Install npm (requires Node.js): https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

    * Update npm:
    ```sh
    npm install npm@latest -g
    ```
   
  * Homebrew (Mac/Linux):
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  
  * Watchman:
    * Windows: https://facebook.github.io/watchman/docs/install.html#windows
    * Mac: 
      ```sh
      brew update
      brew install watchman
      ```

  * Expo (Requires Watchman):
    ```sh
    sudo npm install --global expo-cli
    ```

1. Clone the repo
    ```sh
    git clone https://github.com/jhu-oose-f22/team-unishop
    ```

2. Install NPM packages
    ```sh
    cd app
    npx expo install
    ```

3. Start the server (starts expo automatically)
    ```sh
    npm start  
    ```
      or, using npx:
    ```sh
    npx expo start  
    ```

4. Ensure your mobile device and computer that is running the server are on the same wifi network, then scan the terminal QR code with your phone (in the Camera app for iOS, or in the Expo Go app for Android).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thank you to all the mentors that have helped us throughout this project! We would in particular like to thank our professor, Benjamin Langmead, and all our TAs.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


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
