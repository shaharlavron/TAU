from matplotlib import pyplot
import input_test
import calculate_values
value_format = "a = {} +- {}\n" \
               "b = {} +- {}\n" \
               "chi2 = {}\n" \
               "chi2_reduced = {}"
fig_file = r"linear_fit"
ROWS  = r"C:\Temp\Computers for physicists\Project\inputOutputExamples\workingRows\input.txt"

def fit_linear(filename):
    #getting data and arranging it
    info_axis = input_test.get_data(filename)
    if info_axis == 1:
        return
    values = calculate_values.calc_values(info_axis[0])
    info = info_axis[0]
    axis = info_axis[1]
    x_axis = axis["x"]
    x_axis = x_axis.replace("x axis: ", "")
    y_axis = axis["y"]
    y_axis = y_axis.replace("y axis: ", "")

    #printing the values
    print(value_format.format(*values))

    #plotting
    a = values[0]
    b = values[2]
    x = info["x"]
    y = [i * a + b for i in x]
    pyplot.plot(x, y, "r")
    y2 = info["y"]
    dx = info["dx"]
    dy = info["dy"]
    pyplot.errorbar(x, y2, xerr=dx, yerr=dy, fmt="b+")
    pyplot.xlabel(x_axis)
    pyplot.ylabel(y_axis)
    pyplot.savefig(fname = fig_file, format = "svg")
