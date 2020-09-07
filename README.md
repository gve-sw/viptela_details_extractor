# viptela_details_extractor
A script that extracts the device information from inventory along with the underlying details of the network using monitoring api


## Contacts
* Raveesh V (rmalyava@cisco.com)

## Solution Components
* python
*  Cisco SDWAN (viptela) API
## Setting up python virtual environment and dependencies
```python
# creating virtual environment
python3 -m venv venv
source venv/bin/activate

# Installing python dependencies/modules
pip install -r Requirements.txt
```

## Installation/Configuration

Enter SD-WAN/viptela details in <b>devices.conf<b> file as below

```python
# Add any settings in environemnt fields or files.  Below is an example:
# server IP/hostname and Username and Password
[sdwan]
hostname = 10.x.x.x:443
username = userxxxx
password = passxxxx

```


## Usage


Add any steps needed for someone to run your project.

To launch, run following script to extact device and its interface detials from the service portal:


    $ python extract_details.py



# Screenshots

![/IMAGES/running-script.png](/IMAGES/running-script.png)
![/IMAGES/output.png](/IMAGES/output.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.