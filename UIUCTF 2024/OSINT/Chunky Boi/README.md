# Chunky Boi

Now that's a BIG plane! I wonder where it is. Flag format: uiuctf{plane type, coordinates of the aircraft} Example: uiuctf{Airbus A380-800, 40.036, -88.264}

For coordinates, just omit the digits, do not round up. Precision is the same as the one in the example. The aircraft name is the same as Wikipedia page title. You can extract enough information from this image to answer this. You DO NOT need to register any accounts, all the information is public.

Flag format clarification: The last digit of the first coordinate is even, and the last digit of the second coordinate is odd.

## Solution

Searched the photo to find any clues of the airport or the planes.

Found that these planes with the blue face are from the Alaska Airlines.

While searching for the background buildings i found [this](https://www.youtube.com/watch?v=J2WYaQ07aVY) video that gives the location of the airport.

So put the airport on maps and found the exact spot of the plane and the coordinates.

Tried to find any information about the plane and every result was a Boeing C-17.

Finally, the exact plane type was [Boeing C-17 Globemaster III](https://en.wikipedia.org/wiki/Boeing_C-17_Globemaster_III).


Flag: `uiuctf{Boeing C-17 Globemaster III, 47.462, -122.303}`