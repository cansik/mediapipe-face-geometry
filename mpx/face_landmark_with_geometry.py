import enum
from typing import NamedTuple

import mediapipe
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

# has to be added here
from mediapipe.modules.face_geometry import geometry_pipeline_calculator_pb2
from mediapipe.modules.face_geometry.protos import face_geometry_pb2
# pylint: enable=unused-import

# pylint: enable=unused-import
from mpx.solution_base import SolutionBase

BINARYPB_FILE_PATH = 'mediapipe/modules/face_landmark/face_landmark_front_with_geometry_cpu.binarypb'


class FaceLandmarkFrontWithGeometry(SolutionBase):

    def __init__(self,
                 static_image_mode=False,
                 max_num_faces=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        super().__init__(
            binary_graph_path=BINARYPB_FILE_PATH,
            side_inputs={
                'num_faces': max_num_faces,
            },
            calculator_params={
                'ConstantSidePacketCalculator.packet': [
                    constant_side_packet_calculator_pb2
                        .ConstantSidePacketCalculatorOptions.ConstantSidePacket(
                        bool_value=not static_image_mode)
                ],
                # 'facedetectionshortrangecpu__TensorsToDetectionsCalculator.min_score_thresh': min_detection_confidence,
                'facelandmarkcpu__ThresholdingCalculator.threshold': min_tracking_confidence,
            })
            # outputs=['multi_face_landmarks', 'multi_face_geometry'])

    def process(self, image: np.ndarray) -> NamedTuple:
        results = super().process(input_data={'image': image})
        return results
