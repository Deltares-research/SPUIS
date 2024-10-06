.. |br| raw:: html

   <br />

.. _theory:

Tutorial
===========

This tutorial will guide you through setting up a SPUIS schematization. An input file that contains the schematization of the discharge sluice consists of roughly three sections: 
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





**###########################################################
**Date		: 01-10-2024                                
**Filename	: tutorial.in                                
**Sluice	: Example                      	
**
**Input file for program SPUIS version 4.01, March 1995.	
**Calculation of discharge relations of discharge sluices.
**
**Remark : Lines starting with '**' are for comments. 		
**###########################################################
**
**
**  BOUNDARY CONDITIONS
**
**  Calculation method        		bm  [-]
**  0 = method backwater curves
**  1 = method Bernoulli/momentum equation
**
1
**
**  Number of runs               	nr  [-]
**  Minimum 1, maximum 100.
**
5
**
**  FOR EACH RUN:
**
**  downstream water level         	wsbe  [m]
**  flow rate	                    qt    [m3/s]
**
**  Column 1	Column 2
**  wsbe		qt
**
 -0.359 2500.0
 -0.444 3000.0
 -0.543 3500.0
 -0.657 4000.0
 -0.786 4500.0
**
**
**  GEOMETRY OF SLUICE
**
** The geometry of the sluice is defined by slices in the
**	longitudinal direction of the sluice. The relevant slices
**	need to be defined here.
**
**
**  EXAMPLE top view of sluice:					   +++++++++++++++++++++
**                                              +
**  ++++++++++++++++++++++++++                  +
**                           ++++++++++++++++++++
**                           |||||||||
**  |-------------------------------------------------------------------> X
**                           |||||||||
**                           ++++++++++++++++++++
**  ++++++++++++++++++++++++++                  +
**                           ^         ^      ^ +
**   ^                    ^  |         |      | +++++++++++++++++++++
**   |                    |  |         |      |  ^                 ^
**   |                    |  |         |      |  |                 |
**   |                    |  |         |      |  |                 |
**   1  <----slices---->  2  3         4      5  6                 7
**
**
** A slice defines a change in lateral profile and a section
**	of the sluice for which a discharge relation exists.
**	Define number of slices minimum 2, maximum 50.
**
**  Number of slices				nx  [-]
**
12
**
**  FOR EVERY SLICE:
**
**  slice number					id  [-]
**  X-distance						xd  [m]
**  Bottom level					zb  [m]
**  Profile number					pn  [-]
**
**  Define slices with increasing number!
**
**  Column 1	Column 2	Column 3		Column 4
**  id-number	X-distance	Bottom level	Profile number
**  id			xd			zb				pn
**
1 -1020.0 -13.0 1
2   -20.0 -13.0 2
3     0.0 -11.5 3
4     5.0 -11.5 4
5    22.8 -11.5 5
6    30.0 -11.5 6
7    31.4 -11.5 5
8    49.0 -11.5 5
9    74.0 -13.0 7
10  192.4 -13.0 8
11  339.0 -13.0 8
12 1339.0 -13.0 1
**
**
**  FOR EVERY SLUICE SECTION:
**
**	A section of the sluice is the part between 2 slices.
**	There are nx-1 sections.
**
**  Discharge relation				ar  [-]
**  Only use discharge relation 0 (backwater curve).
**
0 0 0 0 0 0 0 0 0 0 0
**
**
**  DESCRIPTION PROFILES
**
**	The geometry of a slice is described using a profile.
**	Define number of profiles minimum 2, maximum 20.
**
**  Number of profiles				np  [-]
**
3
**
**  FOR EVERY PROFILE:
**
**	A profile has an identification number (profile number).
**	The number of corner points (y-values) has to be entered 
**	for every profile. At minimum 2 and maximum 20.
**	The roughness has to be entered for every profile, this
**	then holds for the entire profile. The roughness is defined
**	as a Nikuradse k-value. For every corner point a height
**	level relative to the bottom level has to be entered (>0).
**	For every corner point of every profile a width of the 
**	water surface has to be entered. For every corner point the
**	wet perimeter (for a water level at this level) has to be 
**	entered.
**
**	Order for every profile:
**	1 row with 3 number
**		profile number				ip  [-]
**		number of points			ny  [-]
**		roughness					rb  [m]
**  ny rows with 3 number
**     level of each point			dp  [m]
**     width at each point			bp  [m]
**     wet perimeter at each point	op  [m]
**
**
**	Enter the profile in increasing order!
**
**  profile 1: canal
**
 1 3 0.010
 0.00 0.000 0.0
 0.01 10000.0 10000.0
 15.0 10000.0 10030.0
**
**
**  profile 2: culverts
**
 2 4 0.600
 0.00 0.0000 0.0
 0.01 130.55 130.55
 15.0 130.55 160.55
**
**
**  profile 3: rebates within culverts
**
 3 4 0.002
 0.00 0.0000 0.0
 0.01 165.25 165.25
 15.0 165.25 195.25
