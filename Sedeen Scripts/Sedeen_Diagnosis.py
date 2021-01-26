import sys
sys.path.append('../')
import utils.mid_level_feature_classifier as mlfc
import utils.structure_features_classifier as sfc

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
		assert type(pathtofeature) is list

	def run(self):

#		results = {}
#		pdb.set_trace()
		rst_txt = "Classification All Done!\n\n"
		preds = []

		if self._feature_path[0].endswith(".csv"):   
			self._model_path = "../models/mid_level_classifier_weights.pickle"
			model = pickle.load(open(self._model_path, "rb"))
			rst = mlfc.classify_files(model, self._feature_path)
		else:
			self._model_path = "../models/structure_weights.pickle"
			model = pickle.load(open(self._model_path, "rb"))
			rst = sfc.classify_files(model, self._feature_path)

		for k in rst.keys():
			pred, pred_label = rst[k]
			rst_txt += "%s Prediction: %d (%s)\n" % (k, pred, pred_label)
			preds.append(pred)

		max_pred = np.max(preds)
		rst_txt += "\nFinal Prediction: %d (%s)\n" % (max_pred, DX_LABELS[max_pred - 1])

		return rst_txt.encode()

if __name__ == "__main__":
    pass
    paths = [
#             'C:/Users/beibi/Desktop/ITCR/cancer_diagnosis/data/1180_copy_0_SuperpixelCooccurrence.csv',
#              'C:/Users/beibi/Desktop/ITCR/cancer_diagnosis/data/1180_copy_1_SuperpixelCooccurrence.csv',
             'C:/Users/lkchu/Desktop/ITCR/cancer_diagnosis/output/1180_crop_0_seg_label.png'
             ]
    pred = Diagnosis(paths)

    result = pred.run()
    print(result)
