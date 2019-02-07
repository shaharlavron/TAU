import input_test

def avg(value,sigma):
    """
    this is how i thought i should do it according to
    the explanation but it resulted very poorly so i went with the standard way
    """
    #mone = sum([value[i]/float(sigma[i]**2) for i in range(len(value))])
    #mechna = sum([1/float(sigma[i]**2) for i in range(len(value))])

    mone = sum(value)
    mechna =len(value)

    avg = mone/mechna
    return avg

def calc_values(info):
    """
    calculates all the values relevant for the fit
    :param info:
    :return [a, da, b, db, chi2, chi2red]:
    """

    #calculate all averages
    x_avg = avg(info["x"], info["dx"])
    y_avg = avg(info["y"], info["dy"])
    xy_avg = [info["y"][i] * info["x"][i] for i in range(len(info["x"]))]
    dxy_avg = [info["dy"][i] * info["dx"][i] for i in range(len(info["x"]))]
    x2_avg = [info["x"][i] ** 2 for i in range(len(info["x"]))]
    dx2_avg = [info["dx"][i] ** 2 for i in range(len(info["dx"]))]
    dy2_avg = [info["dy"][i] ** 2 for i in range(len(info["dy"]))]
    dy2_avg = sum(dy2_avg)/len(dy2_avg)
    xy_avg = avg(xy_avg, dxy_avg)
    x2_avg = avg(x2_avg, dx2_avg)

    #calculate the relevant values for the fit
    a  = (xy_avg - x_avg * y_avg) / (x2_avg - x_avg ** 2)
    da = dy2_avg/(len(info["x"])*(x2_avg - x_avg**2))
    b  = y_avg - a*x_avg
    db = da*x2_avg
    chi2 = [((info["y"][i] - a*info["x"][i] - b)/info["dy"][i])**2\
            for i in range(len(info["x"]))]
    chi2 = sum(chi2)
    chi2red = chi2/(len(info["x"])-2)

    return [a, da, b, db, chi2, chi2red]


