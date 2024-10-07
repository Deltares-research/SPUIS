Tutorial
===========

This tutorial will guide you through the steps required to set up a SPUIS schematization and to create an input (``.in``) file. The steps to use your input file to run a SPUIS simulation are explained in the `getting started <https://spuis.readthedocs.io/en/latest/getting-started.html>`_ chapter of the documentation. 

An input file that contains the schematization of the discharge sluice consists of roughly three sections: 
1.	Boundary conditions: calculation method and a discharge and downstream water level for each model run
2.	Slices: divide the discharge sluice into slices that capture changes in the lateral profile of the discharge sluice
3.	Profiles: define profiles that describe the geometry in the slices

The set-up of this input file is explained step by step for each of these sections.

Defining the boundary conditions
--------------------------------
SPUIS allows the use of either backwater curves (``0``) or Bernoulli and momentum equations (``1``). During the simulations, SPUIS automatically changes the direction of the calculations whenever it encounters a critical cross-section. The calculation methods are explained in more detail in the `theory <https://spuis.readthedocs.io/en/latest/theory.html>`_ chapter.

.. code-block:: none

   **  BOUNDARY CONDITIONS
   **
   **  Calculation method        		bm  [-]
   **  0 = method backwater curves
   **  1 = method Bernoulli/momentum equation
   **
   1

The next section of the input file requires the definition of the amount of runs (at least 1, at most 100). Immediately afterwards, you can specifiy the downstream water level [m] and discharge (m3/s) for each of the runs:

.. code-block:: none

   **  Number of runs               	nr  [-]
   **  Minimum 1, maximum 100.
   **
   3
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

Defining the slices
-------------------
The geometry of the discharge sluice is defined by dividing it into slices in the longitudinal direction of the sluice. All changes in the lateral profile should be captured by a slice. The entire geometry can be defined using a minimum of 2 and a maximum of 50 slices. The first prompt is the number of slices used to schematize the discharge sluice. Let's say we need seven slices to capture the geometry of a discharge sluice:

.. code-block:: none
   
   **  Number of slices				nx  [-]
   **
   7

Then, every slice needs to be defined by an identification number, x-location [m], bottom level [m] and profile number. The identification numbers should be in chronological order, moving from the upstream in the downstream direction. The x-location allows you to define the length of each slice and the bed level give a reference height for the profiles that describe the geometry of the slices. A single profile may be used on multiple slices. In the next section we will define three different profiles, which all have been assigned to one or more slices:

.. code-block:: none

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
   1   0.0 -7.0 1
   2   10.0 -7.0 1
   3   11.0 -5.0 2
   4   15.0 -5.0 3
   5   20.0 -5.0 2
   6   30.0 -7.0 1
   7   31.4 -7.0 1

Defining the profiles
---------------------
The geometry of each slice of the discharge sluice is described using a profile. The entire geometry can be defined using a minimum of 2 and a maximum of 20 profiles. A single profile can be applied to multiple slices.
Profiles are defined at the very end of the input file and follow a specific structure. The first line of each profile definition consists of an identification number, the number of depths at which the width of the profile will be provided, and the Nikuradse roughness length. Then, for each of the depths, a line is added that consists of three values: the bottom level z (with respect to z_0), the width W and the wet perimeter P. In case of losses due to widening, narrowing or the presence of rebates or other irregularities, the wet perimeter must be corrected by multiplying it with a loss factor ξ. Three examples are provided below for profiles 1 (canal upstream of Bath), 4 (culvert inlets with losses) and 5 (inside the culverts). The areas in which these profiles are valid are highlighted in red in Figure 1. 

The first prompt is the number of profiles:

.. code-block:: none

   **  Number of profiles				np  [-]
   **
   3

Each profile follows the same structure. The first line consists of ``profile number`` ``number of y-values`` ``roughness``. This line is then followed by as many lines as indicated in ``number of y-values``. Each of these lines indicates the ``y-value`` ``width at y-value`` ``wet perimeter at y-value``.

.. code-block:: none

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
    2      4     0.600
    0.00   0.00  0.00
    0.01   8.00  8.00
    4.00   8.00  24.00
    4.01   0.00  32.00
   **
   **
   **  profile 3: rebates within culverts
   **
    3 4 0.002
    0.00 0.0000 0.0
    0.01 165.25 165.25
    15.0 165.25 195.25

Recommended sources for calculating the hydraulic losses due to narrowing, widening, rebates or other irregularities are:
•	“Internal flow systems” by D.S. Miller (1978)
•	“Open-Channel Hydraulics” by V.T. Chow (1985)
•	“Discharge relations for hydraulic structures and head losses from different components” by P.A. Kolkman (WL | Delft Hydraulics, 1989)
•	“Open-Channel Hydraulics” by R.H. French (1994)

Creating the input file
--------------------------------
The input file (``.in``) can now be created. The standard format for input files contains comments (``**``) to help the user with the set-up. A completed input file, with the examples used above, is shown below. This file can be copied and re-used to create your own schematization.

.. code-block:: none

   **###########################################################
   **Date		: 01-10-2024                                
   **Filename	: tutorial.in                                
   **Sluice	   : Example                      	
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
   3
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
