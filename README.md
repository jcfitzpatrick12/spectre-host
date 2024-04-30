# SPECTRE: Process, Explore and Capture Transient Radio Emissions

## Overview
`SPECTRE` is a program under development for the automated recording, analysis, and visualisation of radio spectrograms. It consists of three primary components: 
- `spectre` - a set of standalone Python modules for recording, analysing and visualising radio spectrograms 🐍
- `spectre-host` - a containerised environment for recording radio spectrograms, which includes an accompanying CLI tool 📡 🐳
- `spectre-client` - a web-based application for viewing and analysis 💻 (planned for the future)
  
📢 **This project is under active development, with current efforts set on `spectre` and `spectre-host`. Once the testing framework is in place, we will be looking for contributors.**  📢 

---

# spectre-host

## Introduction
`spectre-host` is the principal back-end component of the SPECTRE program. It offers a containerised environment for the automated capture and analysis of radio spectrograms. Underpinned with gnuradio, the framework is in place to accommodate any SDR receiver with a gnuradio source block, simply. Initial support is focused on the SDRplay RSP* series via [`gr-sdrplay3`](https://github.com/fventuri/gr-sdrplay3). The container comes preinstalled with:

- **[`gnuradio`](https://github.com/gnuradio/gnuradio)**
- **[`gr-sdrplay3`](https://github.com/fventuri/gr-sdrplay3)**, which includes the SDRplay RSP* series gnuradio source blocks.
- **[`gr-spectre`](https://github.com/jcfitzpatrick12/gr-spectre)**, which includes custom C++ gnuradio sink blocks for streaming IQ data capture.
- The **`spectre`** CLI tool, for initiating data capture, creating configuration files and other utilities.
- **`cron`** and template scripts for daily data capture.
- **`spectre-companion`**: a development GUI for displaying radio spectrograms captured by the program.

## Supported Receivers

Current supported receivers include:
- RSP1A
- RSPDuo

The framework is in place to integrate the following receivers, this is planned for the near future:
- RSP1, RSP1B, RSP2, RSPdx (via [`gr-sdrplay3`](https://github.com/fventuri/gr-sdrplay3))
- AirspyHF, BladeRF, HackRF, LimeSDR, PLUTO, RTLSDR (via [`Soapy`](https://wiki.gnuradio.org/index.php/Soapy))

## Supported Operating Systems
This project is tested to be compatible with the following operating systems:

- Ubuntu 22.04.3

It may also work on other Linux distributions and other Ubuntu versions. Support for Raspberry Pi and Windows will be explored in the future.

## Installation
We're still in active development, so this setup is not the final intended deployment method. In any case, feel free to dive in and tinker around with the current build. But be warned, everything might not be stable! Here's how you can get started:

**Prerequisites:**
Ensure you have [the docker engine](https://docs.docker.com/engine/install/ubuntu/) installed on your machine. This is essential for building and running the container.


**Installing the RSP API on your host machine**  
First, download the RSP API from SDRPlay on your host machine by running (in your desired directory):  
```wget https://www.sdrplay.com/software/SDRplay_RSP_API-Linux-3.14.0.run```  
  
Alternatively, you can manually download it [directly from the SDRPlay website](https://www.sdrplay.com/api/).  
  
Run the API installation:  
```chmod +x ./SDRplay_RSP_API-Linux-3.14.0.run && ./SDRplay_RSP_API-Linux-3.14.0.run```  
  
With the installation successful, start the sdrplay API service:  
```sudo systemctl start sdrplay```

**Installing SPECTRE**  
Clone the repository (in your desired directory):  
```git clone https://github.com/jcfitzpatrick12/spectre.git```

Navigate to the host directory:   
```cd spectre/host```

Build the Docker image:  
```docker build -t spectre-host .```

Make the start script executable and run it:  
```chmod +x run.sh && ./run.sh```  

Now inside the container, check everything's up and running:  
```spectre -v ```

With the installation verified, you can freely use the suite of `spectre` CLI commands to capture data, create configuration files and launch `spectre-companion`. You can exit the container using: ```exit```

## Contributing
Once the testing framework is in place, we will be looking for contributors. In the meantime, feel free to contact jcfitzpatrick12@gmail.com if you are interested :)




