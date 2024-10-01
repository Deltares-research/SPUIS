.. |br| raw:: html

   <br />

.. _theory:

Tutorial
===========

This tutorial will guide you through setting up a SPUIS schematization. An input file (‘tutorial.in’) that contains the schematization of the discharge sluice consists of roughly three sections: 
1.	Boundary conditions: calculation method and a discharge and downstream water level for each model run
2.	Slices: divide the discharge sluice into slices that capture changes in the lateral profile of the discharge sluice
3.	Profiles: define profiles that describe the geometry in the slices

The set-up of this input file is explained step by step for each of these sections.

Defining the boundary conditions
--------------------------------
SPUIS requires an initial calculation method, indicated by 0 (backwater curves) or 1 (Bernoulli and momentum equations). From there, SPUIS automatically changes the calculation method, and with that the direction of the calculations, whenever it encounters a critical cross-section (theorie). The number of model runs needs to be specified and
Then a discharge and downstream water level must be given for each model 

Defining the slices
-------------------
The geometry of the discharge sluice is defined by dividing it into slices in the longitudinal direction of the sluice. All changes in the lateral profile should be captured by a slice. The entire geometry can be defined using a minimum of 2 and a maximum of 50 slices.

Defining the profiles
---------------------
The geometry of each slice of the discharge sluice is described using a profile. The entire geometry can be defined using a minimum of 2 and a maximum of 20 profiles. A single profile can be applied to multiple slices.
Profiles are defined at the very end of the input file and follow a specific structure. The first line of each profile definition consists of an identification number, the number of depths at which the width of the profile will be provided, and the Nikuradse roughness length. Then, for each of the depths, a line is added that consists of three values: the bottom level z (with respect to z_0), the width W and the wet perimeter P. In case of losses due to widening, narrowing or the presence of rebates or other irregularities, the wet perimeter must be corrected by multiplying it with a loss factor ξ. Three examples are provided below for profiles 1 (canal upstream of Bath), 4 (culvert inlets with losses) and 5 (inside the culverts). The areas in which these profiles are valid are highlighted in red in Figure 1. 

Recommended sources for calculating the hydraulic losses due to narrowing, widening, rebates or other irregularities are:
•	“Internal flow systems” by D.S. Miller (1978)
•	“Open-Channel Hydraulics” by V.T. Chow (1985)
•	“Discharge relations for hydraulic structures and head losses from different components” by P.A. Kolkman (WL | Delft Hydraulics, 1989)
•	“Open-Channel Hydraulics” by R.H. French (1994)
