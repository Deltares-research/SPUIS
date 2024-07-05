# Done
# TODO: CAN BE REDUCED TO ONE FUNCTION (BENWST, BOVWST, MINWSTt, REKNNR, REKNOP)
def bovwst(id, ws, debiet, bm, dn_des, prof_des):
    """
    Computes upstream water level at a critical cross section

    Result:
        float: upstream waterlevel
    """
    from BCKWTR import bckwtr
    ar = dn_des['ar']
    if ar[id-1] == 0:
        return bckwtr(id, ws, debiet, 2, bm, dn_des, prof_des)
    else:
        print(' onbekende ar (routine BOVWST) !')
        exit()
