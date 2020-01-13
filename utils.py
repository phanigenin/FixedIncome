
def get_zero_coupon_price(face,disc_rate,timeperiods):
    '''

    :param face: Face value of the bond
    :param disc_rate: interest/discount rate in %ge
    :param timeperiods:  number of timeperiods
    :return: float, pv of zerocoupon bond
    '''
    return face/((1+disc_rate/100)**timeperiods)

def convert_to_annual(disc_rate,timeperiods_in_year):
    '''

    :param disc_rate: interest/discount rate in %ge
    :param timeperiods_in_year:  number of timeperiods in a year
    :return: float, rate in annual %ge
    '''
    return (((1+disc_rate/(100*timeperiods_in_year))**timeperiods_in_year)-1)*100
