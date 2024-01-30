from typing import List
import numpy as np
import cv2
from app.dataset.dataset import Dataset
from app.dataset.video import Video
from app.edge.detector import EdgeDetector
from app.extractor.hog_extractor import HOGExtractor
from app.haar.detector import HaarDetector
from app.plotter.framesPlotter import FramesPlotter
from app.roi.extractor import RoiExtractor
from app.flow.calculator import FlowCalculator


def plot_frames(frames: List["np.ndarray"]) -> None:
    plotter = FramesPlotter(frames)
    plotter.plot_grid()


def get_roi_frames(video: Video, remove_background=False, plot=False) -> List["np.ndarray"]:
    roi_extractor = RoiExtractor(video.get_frames(), video.bbox)
    roi_frames = roi_extractor.extract(remove_background=remove_background)
    if plot:
        plot_frames(roi_frames)
    return roi_frames


def get_edge_frames(frames: List["np.ndarray"], plot=False) -> List["np.ndarray"]:
    edge_detector = EdgeDetector(frames)
    edge_frames = edge_detector.detect()
    if plot:
        plot_frames(edge_frames)
    return edge_frames


def get_flow_frames(frames: List["np.ndarray"], plot=False) -> List["np.ndarray"]:
    flow_calculator = FlowCalculator(frames)
    flow_frames = flow_calculator.calculate()
    if plot:
        plot_frames(flow_frames)
    return flow_frames


def get_hog_frames(frames: List["np.ndarray"], plot=False) -> List["np.ndarray"]:
    hog_extractor = HOGExtractor(frames)
    hog_frames = hog_extractor.process_frames()
    if plot:
        plot_frames(hog_frames)
    return hog_frames


def get_haar_frames(frames: List["np.ndarray"], plot=False) -> List["np.ndarray"]:
    classifier = cv2.CascadeClassifier()
    # if not classifier.load(cv2.samples.findFile('app/haar/haarcascades/hand.xml')):
    #     print('Error loading hand cascade')
    #     exit(1)
    if not classifier.load(cv2.samples.findFile("app/haar/haarcascades/face.xml")):
        print("Error loading face cascade")
        exit(1)
    haar_detector = HaarDetector(frames, classifier)
    face_frames, _ = haar_detector.detect()
    if plot:
        plot_frames(face_frames)
    return face_frames


def plot_video(current_video: Video) -> None:
    roi_frames = get_roi_frames(current_video)
    edge_frames = get_edge_frames(roi_frames)
    flow_frames = get_flow_frames(roi_frames)
    hog_frames = get_hog_frames(roi_frames)
    haar_frames = get_haar_frames(roi_frames)


if __name__ == "__main__":
    dataset = Dataset("data/WLASL_v0.3.json")
    for video in dataset.videos:
        print("Plotting video: ", video.get_path())
        plot_video(video)
        # plot_video_with_hog(video)
    # plot_video(dataset.videos[0])
