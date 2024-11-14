.. _code:

Overview of Python functions
=============================

.. py:function:: runSpuis

   	Reads the input files, runs SPUIS4.01, writes output files and plots the output. 

.. py:function:: SPUIS401

   	Calls on different Python functions (see below) depending on the content of the supplied input file and returns the results of the SPUIS calculation.

.. py:function:: bckwtr(id, ws, debiet, jfn, bm, dn_des, prof_des)

	Calculates the minimum up- and downstream water levels for different flow regimes using backwater curves. Friction losses are not taken into account.

.. py:function:: benwst(id, ws, debiet, bm, dn_des, prof_des)

	Calculates the downstream water level at slice with a critical cross-section.

.. py:function:: bovwst(id, ws, debiet, bm, dn_des, prof_des)
	
	Calculates the upstream water level at slice with at critical cross-section.

.. py:function:: brnoul(id1, id2, hw1, hw2, debiet, jfn, dn_des, prof_des)
	
	Applies Bernoulli equations and calculates friction losses. Meant for accelerating flow.

.. py:function:: brwopp(id, hw, dn_des, prof_des):
	
	Calculates the width of the wetted area at a slice for a given water level.

.. py:function:: chezyc(id, hw, dn_des, prof_des)

	Calculates the Chézy coefficient per slice and water level using the Colebrook-White equation.

.. py:function:: energh(id, hw, debiet, dn_des, prof_des)
	
	Calculates the energyheight with respect to a reference level for each slice, water level and discharge.

.. py:function:: froude(id, h, q, dn_des, prof_des)
	
	Calculates the Froude number for each slice, water level and discharge.

.. py:function:: grensd(debiet, id, dn_des, prof_des)
	
	Calculates critical depth (at which Fr = 1) for each slice and discharge.

.. py:function:: hydstr(id, hw, dn_des, prof_des)
	
	Calculates the hydraulic radius for each slice and water level.

.. py:function:: impuls(id1, id2, hw1, hw2, debiet, jfn, bm, dn_des, prof_des)
	
	Applies momentum equations, meant for decelerating flow. 

.. py:function:: kracht(id, hw, dn_des, prof_des)
	
	Calculates hydrostatic forces for each slice and water level.

.. py:function:: minwst(id, ws, debiet, bm, dn_des, prof_des)
	
	Defines minimum water depth for a slice to have a critical cross-sections. 

.. py:function:: opperv(id, hw, dn_des, prof_des)

	Calculates the wetted surface for each slice and water level.

.. py:function:: reknnr(id, ws, debiet, bm, dn_des, prof_des)
	
	Calculates the downstream water level when calculating in the downstream direction. 

.. py:function:: reknop(id, ws, debiet, bm, dn_des, prof_des)
	
	Calculates the upstream water level when calculating in the upstream direction. 

.. py:function:: wrrgme(rg)
	
	Defines the different flow regimes (subcritical, critical, supercritical).

.. py:function:: wsprng(id1, id2, w1, w2, debiet, dn_des, prof_des)
	
	Hydraulic jump equations, only valid for sections with a horizontal bottom.
