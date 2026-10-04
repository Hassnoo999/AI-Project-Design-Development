"""Lab 02 Task 04: interfaces only; no inference or camera access runs here."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import numpy as np
from numpy.typing import NDArray

Frame = NDArray[np.uint8]
Tensor = NDArray[np.float32]


@dataclass(frozen=True)
class FramePacket:
    image: Frame
    camera_id: str
    timestamp: datetime


@dataclass(frozen=True)
class PreprocessedFrame:
    tensor: Tensor
    original_shape: tuple[int, int]
    scale: float
    padding: tuple[int, int]


@dataclass(frozen=True)
class Detection:
    class_name: str
    confidence: float
    bbox: tuple[float, float, float, float]


class DataIngestion(ABC):
    """Open a camera/RTSP source, read timestamped frames and release it."""
    @abstractmethod
    def open(self, source: int | str) -> None: ...

    @abstractmethod
    def read_frame(self) -> FramePacket | None: ...

    @abstractmethod
    def close(self) -> None: ...


class ImagePreprocessor(ABC):
    """Letterbox, convert BGR to RGB and normalize to float32 [0, 1]."""
    @abstractmethod
    def preprocess(self, frame: Frame, size: tuple[int, int] = (640, 640)) -> PreprocessedFrame: ...


class ModelInferenceEngine(ABC):
    """Load model weights and infer on CPU; return raw predictions."""
    @abstractmethod
    def load_model(self, weights_path: str, device: str = "cpu") -> None: ...

    @abstractmethod
    def predict(self, prepared: PreprocessedFrame) -> Any: ...


class DetectionPostprocessor(ABC):
    """Filter predictions, apply NMS if needed and map boxes to original pixels."""
    @abstractmethod
    def filter_detections(self, predictions: Any, prepared: PreprocessedFrame,
                          confidence: float = 0.65) -> list[Detection]: ...


class AlertLogger(ABC):
    """Persist qualified events and notify the teacher; apply duplicate cooldown."""
    @abstractmethod
    def log_event(self, packet: FramePacket, detections: list[Detection]) -> str | None: ...

    @abstractmethod
    def notify(self, event_id: str, message: str) -> bool: ...
