"""Let's get familiar with drawing functions."""
import cv2
import numpy as np
###############################################################################
img = np.zeros((512, 512, 3), np.uint8)

"""
numpy.zeros(shape, dtype = None, order = ‘C’) :
Return a new array of given shape and type, with zeros.

Parameters :

shape : integer or sequence of integers
order  : C_contiguous or F_contiguous
         C-contiguous order in memory(last index varies the fastest)
         C order means that operating row-rise on the array
         will be slightly quicker
         FORTRAN-contiguous order in memory (first index varies the fastest).
         F order means that column-wise operations will be faster.
dtype : [optional, float(byDeafult)] Data type of returned array.

Returns: ndarray of zeros having given shape, order and datatype.
"""

###############################################################################
# Line
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
"""
Syntax: cv2.arrowedLine(image, start_point, end_point, color
[, thickness[, line_type[, shift[, tipLength]]]])

Parameters:

1. image: It is the image on which line is to be drawn.

2. start_point: It is the starting coordinates of line.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

3. end_point: It is the ending coordinates of line.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

4. color: It is the color of line to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

5. thickness: It is the thickness of the line in px.

6. line_type: It denotes the type of the line for drawing.

7. shift: It denotes number of fractional bits in the point coordinates.

8. tipLength: It denotes the length of the arrow
tip in relation to the arrow length.

Return Value: It returns an image.
"""

###############################################################################
# Arrowred Line
img = cv2.arrowedLine(img, (510, 510), (270, 270), (0, 0, 255), 5)
"""
Syntax: cv2.arrowedLine(image, start_point, end_point, color
[, thickness[, line_type[, shift[, tipLength]]]])

Parameters:

1. image: It is the image on which line is to be drawn.

2. start_point: It is the starting coordinates of line.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

3. end_point: It is the ending coordinates of line.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

4. color: It is the color of line to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

5. thickness: It is the thickness of the line in px.

6. line_type: It denotes the type of the line for drawing.

7. shift: It denotes number of fractional bits in the point coordinates.

8. tipLength: It denotes the length of the arrow
tip in relation to the arrow length.

Return Value: It returns an image.
"""

###############################################################################
# Rectangle
img = cv2.rectangle(img, (0, 510), (270, 320), (0, 255, 0), 5)
"""
Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)

Parameters:

1. image: It is the image on which rectangle is to be drawn.

2. start_point: It is the starting coordinates of rectangle.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

3. end_point: It is the ending coordinates of rectangle.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

4. color: It is the color of border line of rectangle to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

5. thickness: It is the thickness of the rectangle border line in px.
Thickness of -1 px will fill the rectangle shape by the specified color.

6. line_type: It denotes the type of the line for drawing.

7. shift: It denotes number of fractional bits in the point coordinates.

8. tipLength: It denotes the length of the arrow
tip in relation to the arrow length.

Return Value: It returns an image.
"""

###############################################################################
# Circle
img = cv2.circle(img, (100, 400), 70, (0, 255, 255), 5)
"""
Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)

Parameters:

1. image: It is the image on which circle is to be drawn.

2. center_coordinates: It is the center coordinates of circle.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

3. radius: It is the radius of circle.

4. color: It is the color of border line of circle to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

5. thickness: It is the thickness of the circle border line in px.
Thickness of -1 px will fill the rectangle shape by the specified color.

Return Value: It returns an image.
"""

###############################################################################
# Text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4,
                  (255, 255, 255), 5, cv2.LINE_AA)
"""
Syntax: cv2.putText(image, text, org, font, fontScale, color
[, thickness[, lineType[, bottomLeftOrigin]]])

Parameters:

1. image: It is the image on which text is to be drawn.

2. text: Text string to be drawn.

3. org: It is the coordinates of the bottom-left corner of
the text string in the image. The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

4. font: It denotes the font type. Some of font types
are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.

5. fontScale: Font scale factor that is multiplied
by the font-specific base size.

6. color: It is the color of text string to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

7. thickness: It is the thickness of the line in px.

8. lineType: This is an optional parameter.
It gives the type of the line to be used.

9. bottomLeftOrigin: This is an optional parameter.
When it is true, the image data origin is at the bottom-left corner.
Otherwise, it is at the top-left corner.

Return Value: It returns an image.
"""

###############################################################################
# Ellipse
img = cv2.ellipse(img, (400, 100), (100, 50), 0, 15, 315, 255, -1)
"""
Syntax: cv2.ellipse(image, centerCoordinates, axesLength, angle,
startAngle, endAngle, color [, thickness[, lineType[, shift]]])

Parameters:

1. image: It is the image on which ellipse is to be drawn.

2. centerCoordinates: It is the center coordinates of ellipse.
The coordinates are represented as tuples of
two values i.e. (X coordinate value, Y coordinate value).

3. axesLength: It contains tuple of two variables
containing major and minor axis of ellipse (major axis length, minor axis
length).

4. angle: Ellipse rotation angle in degrees.

5. startAngle: Starting angle of the elliptic arc in degrees.

6. endAngle: Ending angle of the elliptic arc in degrees.

7.color: It is the color of border line of shape to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

8.thickness: It is the thickness of the shape border line in px.
Thickness of -1 px will fill the shape by the specified color.

9. lineType: This is an optional parameter.
It gives the type of the ellipse boundary.
shift: This is an optional parameter.
It denotes the number of fractional bits
in the coordinates of the center and values of axes.

Return Value: It returns an image.
"""
###############################################################################
# Polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], False, (0, 255, 255))
"""
To draw a polygon, first you need coordinates of vertices.
Make those points into an array of shape ROWSx1x2 where ROWS are number of
vertices and it should be of type int32.
Here we draw a small polygon of with four vertices in yellow color.

If third argument is False, you will get a polylines
joining all the points, not a closed shape.

cv2.polylines() can be used to draw multiple lines.
Just create a list of all the lines you want to draw
and pass it to the function. All lines will be drawn individually.
It is more better and faster way to draw a group of lines
than calling cv2.line() for each line.
"""

###############################################################################


cv2.imshow('Picture', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('savedimage.jpg', img)
    cv2.destroyAllWindows()
