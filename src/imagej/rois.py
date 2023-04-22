import numpy as np


class ROIDendron:
    """
    Parent class for containing children (ROIs).
    """

    def __init__(self):
        self.rois = []
        self.count = 0

    def add_roi(self, roi: "ROI"):
        """
        Add an instance of the ROI class to the ROIDendron.

        :param roi: An instance of the ROI class.
        """
        if roi is not None:
            roi.set_dendron(self)
            self.rois.append(roi)
            self._update_roi_count()
        else:
            return None

    def remove_roi(self, index: int):
        """
        Remove an instance of the ROI class from the ROIDendron.

        :param index: Index of the ROI to remove from the ROIDendron.
        """
        roi = self.rois[index]
        roi.set_dendron(None)
        self.rois.remove(roi)
        self._update_roi_count()

    def _update_roi_count(self):
        self.count = len(self.rois)


class ROI:
    """
    Base class for a Region of Interest (ROI).
    """

    def __init__(self):
        self.dendron = None
        self.data = None

    def set_dendron(self, dendron: "ROIDendron"):
        """
        Set the parent ROIDendron of the ROI.

        :param dendron: An instance of the ROIDendron class.
        """
        self.dendron = dendron


class Ellipsoid(ROI):
    """
    Initializes an Ellipsoid ROI instance with the provided data.

    :param data: A 2D numpy array, typically with shape (2, 2),
        where row index 0 defines the center position and row
        index 1 defines the semi axis length (e.g. radii).
    """

    def __init__(self, data: np.ndarray):
        super().__init__()
        self.data = data
        self.ndim = data.shape[1]
        self.center = self.data[0, :]
        self.semi_axis_length = self.data[1, :]


class Line(ROI):
    """
    Initializes a Line ROI instance with the provided data.

    :param data: A 2D numpy array, typically with shape (2, 2),
        where row index 0 defines endpoint one of the line and
        row index 1 defines endpoint two of the line.
    """

    def __init__(self, data: np.ndarray):
        super().__init__()
        self.data = data
        self.ndim = data.shape[1]
        self.endpoint_one = self.data[0, :]
        self.endpoint_two = self.data[1, :]


class Rectangle(ROI):
    """
    Initializes a Rectangle ROI instance with the provided data.

    :param data: A 2D numpy array, typically with shape (2, 2),
        where row index 0 defines the minimum dimension values and
        row index 1 defines the maximum dimension value of the rectangle.
    """

    def __init__(self, data: np.ndarray):
        super().__init__()
        self.data = data
        self.ndim = data.shape[1]
        self.min_values = self.data[0, :]
        self.max_values = self.data[1, :]


class Polygon(ROI):
    """
    Initializes a Polygon ROI instance with the provided data.

    :param data: A numpy array with shape [1, D], where D
        are the number of dimensions.
    """

    def __init__(self, data: np.ndarray):
        super().__init__()
        self.data = data
        self.ndim = data.shape[1]
        self.vertices = self.data