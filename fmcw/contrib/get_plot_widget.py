from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as PlotNavBar

class PlotCanvasWidget(FigureCanvas):
    """
    Base plot, used for all ploting in the application
    """
    def __init__(self) -> None:
        self.figure = Figure(tight_layout=True)
        self.axes = self.figure.add_subplot(111)

        super(PlotCanvasWidget, self).__init__(self.figure)
