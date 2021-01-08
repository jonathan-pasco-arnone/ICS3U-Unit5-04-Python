#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program calculates the area of a cylinder

import math


def area_calculation(radius, height):
    # This function calculates the area of a cylinder

    volume = math.pi * math.pow(radius, 2) * height

    return volume


def main():
    # This function takes inputs and gives them to the calculation function

    print("This program calculates the volume of a cylinder."
          " Please enter the radius and height")
    print("")

    try:
        radius_int = int(input("Radius: "))
        print("")
        height_int = int(input("Height: "))
    except Exception:
        print("Please enter valid integers")
    else:
        if radius_int >= 0 and height_int >= 0:
            volume = area_calculation(radius_int, height_int)
            print("The volume is {:.2f}m3".format(volume))
        else:
            print("Please have 2 positive integers")


if __name__ == "__main__":
    main()
