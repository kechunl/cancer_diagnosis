import sys
sys.path.append('../')
from utils.mid_level_feature_classifier import classify_files

import numpy as np
import pickle
import os
import pdb

DX_LABELS = ["Benign", "Atypia", "DCIS", "Invasive"]

class Diagnosis:
	"""
	class Predict Diagnosis for ROIs.
	"""

	def __init__(self, pathtofeature):
		self._feature_path = pathtofeature
		self._model_path = "../models/mid_level_classifier_weights.pickle"


	def run(self):
		model = pickle.load(open(self._model_path, "rb"))
		csv_paths = self._feature_path

		results = {}
		rst_txt = "Classification All Done!\n\n"
		preds = []

		rst = classify_files(model, csv_paths)

		for k in rst.keys():
			pred, pred_label = rst[k]
			rst_txt += "%s Prediction: %d (%s)\n" % (k, pred, pred_label)
			preds.append(pred)

		max_pred = np.max(preds)
		rst_txt += "\nFinal Prediction: %d (%s)\n" % (max_pred, DX_LABELS[max_pred - 1])

		return rst_txt.encode()

# paths = ['C:/ITCR/cancer_diagnosis-master/output/1180_copy_0_SuperpixelCooccurrence.csv','C:/ITCR/cancer_diagnosis-master/output/1180_copy_1_SuperpixelCooccurrence.csv']
# pred = Diagnosis(paths)
# result = pred.run()
# print(result)