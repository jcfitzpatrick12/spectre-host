# **SPECTRE: Process, Explore and Capture Transient Radio Emissions**

## Overview

📢 **This project is under active development. Contributors welcome!** 📢

`spectre` is a receiver-agnostic program for recording and visualising radio spectrograms. Powered by [GNU Radio](https://www.gnuradio.org/).

### **Features**
- 💻 Intuitive CLI tool  
- 🛰️ Wide receiver support  
- 💾 Live recording of radio spectrograms and I/Q data  
- ⚙️ Flexible, configurable data capture  
- 🐳 Containerised backend  
- 🔧 Developer-friendly and extensible



## Solar Radio Observations ☀️

Observations of the huge X9.0 solar flare on October 3rd 2024. A comparison of a `spectre` spectrogram (second panel) captured in the West End of Glasgow, to that observed by the [CALLISTO](https://e-callisto.org/) spectrometer stationed in Egypt, Alexandria (top panel).

![Solar flare observations comparison](docs/gallery/comparison.png)


## Supported Receivers

Initial support is focused on the SDRplay RSP* series via [`gr-sdrplay3`](https://github.com/fventuri/gr-sdrplay3). A wide range of receiver support is planned.

### **Current Supported Receivers**
- [RSP1A (from SDRPlay)](https://www.sdrplay.com/rsp1a/)  
- [RSPduo (from SDRPlay)](https://www.sdrplay.com/rspduo/)  

### **Planned Future Support**
The framework is in place to integrate the following receivers:
- RSP1, RSP1B, RSP2, RSPdx (via [`gr-sdrplay3`](https://github.com/fventuri/gr-sdrplay3))  
- USRP SDRs (e.g., the [b200-mini](https://www.ettus.com/all-products/usrp-b200mini/))  
- RTLSDR, AirspyHF, BladeRF, HackRF, LimeSDR, PLUTO (via [`Soapy`](https://wiki.gnuradio.org/index.php/Soapy))  

**⚠️ Note:**  
SDRPlay clones (i.e., unofficially produced copies of SDRPlay receivers) will likely not work with `spectre` as they are not compatible with the official SDRPlay API.  


## Supported Operating Systems and Platforms
This project is tested to be compatible with the following operating systems and architectures:
- **Ubuntu 22.04.3** (x86-64, arm64)  
- **Debian GNU/Linux 12 (bookworm)** (arm64)  

But should be compatible with most linux flavours.

It has been tested specifically on the following machines:  
- **ThinkPad P1G5** running Ubuntu 22.04.3  
- **Raspberry Pi 4 Model B** running Ubuntu Desktop, Raspberry Pi OS, and Raspberry Pi OS Lite  

Support for MacOS will be explored in the future.


## Installation

### **Prerequisites**
The following must be installed on your machine:  
- The Docker Engine, which you can install by following [the official documentation](https://docs.docker.com/engine/install/)
- `git`, which you can install by following [the official documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### **Initial setup**
1. Clone the `spectre` GitHub repository:  
```bash
git clone https://github.com/jcfitzpatrick12/spectre.git
```
2. Change directory into the newly cloned repository:  
```bash
cd spectre
```
3. Set the `SPECTRE_DATA_DIR_PATH` environment variable for the current terminal session, which holds data files generated by the program:  
```bash
export SPECTRE_DATA_DIR_PATH=$(pwd)/.spectre-data
```

4. And ensure that environment variable is set as a perminent shell configuration:  
```bash
echo "export SPECTRE_DATA_DIR_PATH=$(pwd)/.spectre-data" >> ~/.bashrc
```


### **Starting the `spectre-server`**
The `spectre-server` container must be running to respond to `spectre-cli` requests. The following commands assume your working directory corresponds to the cloned `spectre` repository.

1. Build the image (this can take a bit of time):    
   ```bash
   docker build --tag spectre-server backend
   ```

2. Run the `spectre-server` container:  
```bash
docker run --rm \
         --publish 127.0.0.1:5000:5000 \
         --name spectre-server \
         --volume $SPECTRE_DATA_DIR_PATH:/app/spectre/.spectre-data \
         --volume /dev/shm:/dev/shm \
         --device /dev/bus/usb:/dev/bus/usb \
         --detach \
         spectre-server
```
 
3. At any time, you can stop the ```spectre-server``` using:    
   ```bash
   docker container stop spectre-server --signal kill
   ```


### **Running the `spectre-cli`**
The following commands assume your working directory corresponds to the cloned `spectre` repository.

1. Create a Python virtual environment:  
```bash
python3 -m venv ./venv
```

2. Activate the virtual environment:  
```bash
source ./venv/bin/activate
```

3. Install the required dependencies:  
```bash
pip install -e .
```

4. Verify the CLI is operational:  
```bash
spectre --help
```
Notably, the CLI commands will only work with the virtual environment activated.


## Contributing
This repository is in active development. If you are interested, feel free to contact  jcfitzpatrick12@gmail.com :)
