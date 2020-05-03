Principal Componenents Analysis is one of the dimensionality reduction techniques used to reduce the dimensions of the image for proper view.

Steps:

Flattening of the tensor into a 2-D matrix

Multiplying the transpose of matrix with the matrix

Computing covariance of this matrix

Calculating eigenvalues(weights) and eigenvectors(Principal Components) of this matrix

Chosing the Principal Components and multiplying them with mean centered unrolled matrix

Reshaping it into viewable format

Dependencies:
Cv2:
PIL:
Matplotlib:
Numpy

How to run:

Clone--
Provide the path of image--
run the command:python3 <filename.py>



