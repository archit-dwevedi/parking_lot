# Parking Lot

## Problem statement
We want to build a parking lot management application. Multiple parking lots want to use this application. 
There are two types of vehicles: Two-Wheeler, Car
Each parking lot has separate capacity for each kind of vehicle.
There are different slab based hourly rate cards for each kind of vehicle.

## Assume that
Parking lots with rates and capacities are known to the system. No apis are needed to register these.

## Demonstrate the following
Park a Vehicle at a given parking lot (should fail if the lot is full)
Exit from the parking area and tell the amount due for the duration.
Given a vehicle no., see complete parking history (When, Duration, Amount Paid)


## Technology Stack

### Back-end Technology

<details>
	<summary>Django</summary>
    <h4>
        What is Django?
    </h4>
    Django is a high-level python web framework that encourages rapid Development and clean, pragmatic design.
    <h4>
        Why Django?
    </h4>
    <ul>
        <li>Scalable & Reliable - It's been 13 years Django started developing its framework</li>
        <li>Secure - As it have inbuilt authentication, authorization and session management which makes it secure.</li>
        <li>In-built Admin.</li>
        <li>MVC Architecture</li>
    </ul>
    <br><b>Reference:</b> <a href="https://djangostars.com/blog/why-we-use-django-framework/">Why Django?</a>
</details>

#### Design:
- https://github.com/archit-dwevedi/parking_lot/blob/main/design.pdf

#### API Walkthrough:
- https://github.com/archit-dwevedi/parking_lot/blob/main/walk_through.mov

## Installation

Follow the Steps as Given Below for Unix Systems 

- `sudo apt-get install python3-pip` (Install PiP - Python Package Manager)
- `sudo pip3 install virtualenv` (Installing Virtual Environment)
- `virtualenv -p python3 venv` (Creating New Virtual Environment "venv")
- `cd venv` (Changing Directory to Newly Created Virtual Environment)
- `source bin/activate` (Activating the Virtual Environment)
- `source development.env` (Create development environment file to store the variables)
    - Sample Development Env Dist can be found on the repo
- `sudo pip3 install django` (Installing Django using PIP)
- `git clone https://github.com/archit-dwevedi/parking_lot` (Cloning the Repo)
- `cd parking_lot` (Chaging Directory to TapSearch)
- `pip3 install -r requirements.txt` (Installing all the Requirements)
- `python3 manage.py migrate` (Migrating the Database)
- `python3 manage.py runserver` (Running Local Server)

For Intallation on Windows follow the Tutorial
 - https://docs.djangoproject.com/en/2.2/howto/windows/
 
#### Database: Postgresql

