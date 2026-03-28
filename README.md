# geckovision

A wrapper for OpenCV. Refer to the following documentation below about the functionality provided in this library.

mmmm ok so the structure is like this :>

geckovision
- classifier assist
- identifier
  - eyeFinder
  - faceFinder
  - generalFinder
  - finderTypes

Classifier assist:
  It has a single method, used in the package but can be used outside of it too

eyeFinder:
  Simply Shrimply Lovely. 
  It finds eyes!!! either find the rectangles bounding eyes in the provided frame or annotate the centers of these on the thing!!

faceFinder:
  same thing, except for FACES. THE FACES. THEYRE WATCHING. THEY ARE BLANK. THEY AR-

generalFinder:
  A general finder!!! pass in a cascade haar classifier xml and the image and get all the goods :D

finderTypes:
  in case you want to use a basic face or eye finder but dont want to use eyeFinder/faceFinder (pass into generalfinder as the type thigny :D)
