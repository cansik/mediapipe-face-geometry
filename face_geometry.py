from typing import NamedTuple

import numpy as np

from mediapipe.calculators.core import constant_side_packet_calculator_pb2
# pylint: disable=unused-import
from mediapipe.calculators.core import gate_calculator_pb2
from mediapipe.calculators.core import split_vector_calculator_pb2
from mediapipe.calculators.tensor import image_to_tensor_calculator_pb2
from mediapipe.calculators.tensor import inference_calculator_pb2
from mediapipe.calculators.tensor import tensors_to_classification_calculator_pb2
from mediapipe.calculators.tensor import tensors_to_detections_calculator_pb2
from mediapipe.calculators.tensor import tensors_to_landmarks_calculator_pb2
from mediapipe.calculators.tflite import ssd_anchors_calculator_pb2
from mediapipe.calculators.util import association_calculator_pb2
from mediapipe.calculators.util import detections_to_rects_calculator_pb2
from mediapipe.calculators.util import logic_calculator_pb2
from mediapipe.calculators.util import non_max_suppression_calculator_pb2
from mediapipe.calculators.util import rect_transformation_calculator_pb2
from mediapipe.calculators.util import thresholding_calculator_pb2
# pylint: enable=unused-import
from mediapipe.framework.formats.landmark_pb2 import Landmark

from solution_base import SolutionBase

BINARYPB_FILE_PATH = 'data/face_geometry_from_landmarks.binarypb'


class FaceGeometry(SolutionBase):
    def __init__(self):
        super().__init__(
            binary_graph_path=BINARYPB_FILE_PATH,
            outputs=['multi_face_geometry'])
        self.graph_outputs = super()._self._graph_outputs

    def predict(self) -> NamedTuple:
        self.graph_outputs.clear()
        print("predicting")

