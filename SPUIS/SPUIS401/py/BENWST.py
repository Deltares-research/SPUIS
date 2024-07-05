# Done
# TODO: CAN BE REDUCED TO ONE FUNCTION (BENWST, BOVWST, MINWSTt, REKNNR, REKNOP)
def benwst(id, ws, debiet, bm, dn_des, prof_des):
    """
    Computes downstream water level at a critical cross section

    Result:
        float: downstream waterlevel
    """
    from BCKWTR import bckwtr
    ar = dn_des['ar']
    if ar[id-1] == 0:
        return bckwtr(id, ws, debiet, 3, bm, dn_des, prof_des)
    else:
        print(' onbekende ar (routine BENWST) !')
        exit()

