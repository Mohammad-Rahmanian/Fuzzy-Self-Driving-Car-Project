# Fuzzy Self-Driving Car Simulator

## Overview
The Fuzzy Self-Driving Car Simulator is an educational tool designed to demonstrate the application of fuzzy logic to control systems within the context of an autonomous vehicle. This simulation uses Python and PyGame to showcase how a car can autonomously navigate a track by making decisions based on sensor input, utilizing fuzzy logic for real-time control adjustments.

## Features
- **Fuzzy Logic Controllers**: Implements steering and speed control through fuzzy logic based on proximity to the track edges.
- **Interactive Simulation**: A graphical simulation where the vehicle navigates a virtual track, visualizing the car's decision-making process.
- **Customizability**: Users can modify fuzzy logic rules and parameters to see how changes affect vehicle behavior.

## Prerequisites
Before you start, you'll need the following installed:
- Python 3.8 or newer
- PyGame
- NumPy

## Installation
To set up the project locally, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3.Launch the simulator by running:

This command starts the PyGame window and begins the simulation. Use the arrow keys to manually adjust the car's direction:
- **Left Arrow Key**: Turn the car left.
- **Right Arrow Key**: Turn the car right.
- **Mouse Click on Mute Button**: Toggle sound on or off.

## How It Works
The simulator includes several key components:
- `simulator.py`: Main script that initializes the game and updates the simulation.
- `fuzzy_controller.py`: Contains logic for steering based on lateral distance to the track boundaries.
- `additional_controller.py`: Manages acceleration based on the distance to the obstacle directly ahead.
- `rules.txt` and `additional_rules.txt`: Text files that define the fuzzy rules used for controlling the car.

The control system processes sensor inputs through several stages:
1. **Fuzzification**: Converts sensor readings into degrees of membership for fuzzy sets.
2. **Inference**: Applies fuzzy logic rules to determine the appropriate control actions.
3. **Defuzzification**: Converts the fuzzy control outputs into actual steering angles and acceleration values.
