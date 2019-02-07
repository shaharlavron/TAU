def readData(file_name):
    """
    reads the data
    :param file_name:
    :return:
    """
    file_po = open(file_name, "r")
    data = file_po.readlines()
    return data


def is_cols(data):
    """
    checks if the data is in row or col format
    :param data:
    :return 1 if cols 0 if rows:
    """
    if "x" in data[0].lower() and "y" in data[0].lower():
        return 1
    else:
        return 0


def arrangeData(data):
    """
    strips info from spaces
    :param data:
    :return data_tuple:
    """
    data = [i.rstrip().strip() for i in data]
    info = [i for i in data if "axis" not in i and i != ""]
    axis = [i for i in data if "axis" in i]
    data_tuple = (info, axis)
    return data_tuple


def ColsToRows(data_tuple):
    """
    a function that gets col data
    and turns it into rows
    :param data_tuple:
    :return row_info:
    """
    info = data_tuple[0]
    #axis = data_tuple[1]
    row_info = [[],[],[],[]]
    info = [i.split() for i in info]
    length = len(info[0])
    for i in info:
        if len(i) != length:
            return 1
        else:
            pass
    for j in range(4):
        row_info[j] = [i[j] for i in info]
    return row_info


def RowsToData(row_info):
    """
    processes data that comes in row form
    :param row_info:
    :return:
    """
    info_dict = {}
    axis_dict = {}
    for i in range(len(row_info[0])):
        info_dict[row_info[0][i][0].lower()] = row_info[0][i][1::]
    for i in range(len(row_info[1])):
        axis_dict[row_info[1][i][0].lower()] = row_info[1][i][0::]
    for i in info_dict:
        info_dict[i] = [float(j) for j in info_dict[i]]

    return (info_dict,axis_dict)


def checkSigma(info_dict):
    """
    checks if there is a negative deviation
    if so terminates the program
    :param info_dict:
    :return 1 for error 0 for success:
    """
    #print info_dict["dx"]
    for i in info_dict["dx"]:
        if i >= 0:
            pass
        else:
            return 1

    for i in info_dict["dy"]:
        if i >= 0:
            pass
        else:
            return 1
    return 0

def get_data(filename):
    """
    parses the data using the functions above
    :param filename:
    :return info_axis a list with two dicts one containing data and other the axises:
    """
    data = readData(filename)
    data_tup = arrangeData(data)
    row_info = []

    #checks if cols or rows, if rows also validates the info
    if is_cols(data):
        row_info = ColsToRows(data_tup)
    else:
        row_info = data_tup[0]
        row_info = [i.split() for i in row_info]

        #checks if all lists are the same length
        length = len(row_info[0])
        for i in row_info:
            if len(i) == length:
                pass
            else:
                print("Input file error: Data lists are not the same length.")
                return 1

    if row_info == 1:
        print("Input file error: Data lists are not the same length.")
        return 1
    row_info = [row_info, data_tup[1]]
    info_axis = RowsToData(row_info)

    #checks if all uncertainties are larger than zero
    test = checkSigma(info_axis[0])
    if test == 1:
        print("Input file error: Not all uncertainties are positive.")
        return 1
    return info_axis

if __name__ == '__main__':
    main()
