"""
A subclass for a randomly guessing classifier
"""
from __future__ import absolute_import
import numpy as np

from .classifier import Classifier

class FromCM(Classifier):

    def __init__(self, scheme='CM', seed=0):
        """
        An object that simulates predicted classifications from the truth values and and arbitrary confusion matrix.

        Parameters
        ----------
        scheme: string
            the name of the classifier
        seed: int, optional
            the random seed to use, handy for testing
        """

        super(FromCM, self).__init__(scheme, seed)
        np.random.seed(seed=self.seed)

    def classify(self, CM, truth, other=False):
        """
        Simulates mock classifications based on truth

        Parameters
        ----------
        CM: numpy.ndarray, float
            the confusion matrix, normalized to sum to 1 across rows. Its dimensions need to match the anticipated number of classes
        truth: numpy.ndarray, float
            Array of the true classes of the items
        other: boolean, optional
            include class for other

        Returns
        -------
        prediction: numpy.ndarray, float
            predicted classes
        """

        N = len(truth)
        M = len(CM)
        if other: M += 1
        prediction = []
        for item in truth:
            perturbed_prob = np.absolute(CM[item,:]+np.random.normal(0.0,0.03,np.shape(CM[item,:])))
            normalized_prob = perturbed_prob/np.sum(perturbed_prob)
            prediction.append(normalized_prob)
        prediction /= np.sum(prediction, axis=1)[:, np.newaxis]

        return prediction
