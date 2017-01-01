# BUS 2257 PROJECT

This is currently a quick python script I made to prototype facial recognition software which can be used to detect if it is the owner of the house at the door, or someone else. If we decide to use facial recognition software in the project this repo will be updated, by firstly replacing the python code with C code. Changing it into a ROS project, to allow more modularity. Then adding 2 ROS projects, one to message the client in the house, letting them know, the other to message the company saying to pay a little attention as to what is happening.

Currently the training_set directory is small due to the fact I dislike taking pictures of myself, and the fact that I am using a really bad webcam connected to an old computer. For future cases the training set will grow.

Another hope is to make some module for determining obstruction in the driveway or several well know unsafe conditions for maintenance teams to come up.

An easier addition would also be a self growing training set.

Using this software is simple:
	-upload your training set instead of mine
	-attach working webcam
	-run python bus_2257.py (I rarely use python so I saw no point in making in making it be able to be run like ./bus_2257.py)
	-point camera at faces of people a blue rectangle means authorized and red means not
	
Note: not commented yet as have to figure out if the group is going to go through with this idea
