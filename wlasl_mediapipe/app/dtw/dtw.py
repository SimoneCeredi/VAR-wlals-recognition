from typing import List

import numpy as np
from fastdtw import fastdtw
from tabulate import tabulate

from wlasl_mediapipe.app.mp.mp_video import MediapipeVideo


def calc_dtw_distance(video: MediapipeVideo, others: List[MediapipeVideo]):
    ret = {"ThisShouldBeAnError": [np.inf]}
    left_hand = video.sign_model.lh_embedding
    right_hand = video.sign_model.rh_embedding
    curr = 0
    for other_video in others:
        curr += 1
        if (
            video.sign_model.has_left_hand == other_video.sign_model.has_left_hand
        ) and (
            video.sign_model.has_right_hand == other_video.sign_model.has_right_hand
        ):
            distance = {
                "left": 0.0,
                "right": 0.0,
            }
            other_left_hand = other_video.sign_model.lh_embedding
            other_right_hand = other_video.sign_model.rh_embedding
            if video.sign_model.has_left_hand:
                distance["left"] = fastdtw(left_hand, other_left_hand)[0]
            if video.sign_model.has_right_hand:
                distance["right"] = fastdtw(right_hand, other_right_hand)[0]
        else:
            distance = {
                "left": np.inf,
                "right": np.inf,
            }
        if other_video.video.gloss not in ret:
            ret[other_video.video.gloss] = []
        ret[other_video.video.gloss].append(distance["left"] + distance["right"])
    return _best_choice(ret)


def _best_choice(distances):
    """Given a list of distances, calculates the minimum the distances for each gloss"""
    for gloss in distances:
        distances[gloss] = np.min(distances[gloss])
    # print(f"Distances again: {distances}")
    return min(distances.items(), key=lambda x: x[1])


def calc_accuracy(real_glosses, classified_glosses) -> float:
    correct = 0
    total = len(real_glosses)

    for key, value in real_glosses.items():
        if key in classified_glosses:
            if classified_glosses[key][0] == value:
                correct += 1

    accuracy = correct / total * 100
    return accuracy


def classify(
    test_videos: List[MediapipeVideo],
    train_videos: dict,
    augment: bool,
    output_file: str = "results.log",
) -> None:
    real_glosses = [video.video.gloss for video in test_videos]
    classified_glosses = [(real_glosses[0], np.inf) for _ in test_videos]
    for gloss in train_videos:
        print(f"Getting training set for gloss {gloss}")
        current_train = [
            MediapipeVideo(
                train_video, plot=False, expand_keypoints=True, all_features=True
            )
            for train_video in train_videos[gloss]
        ]
        if augment:
            augmented_train = [video.augment(3) for video in current_train]
            for videos in augmented_train:
                current_train.extend(videos)
        for i, video in enumerate(test_videos):
            best_choice = calc_dtw_distance(video, current_train)
            if best_choice[1] < classified_glosses[i][1]:
                classified_glosses[i] = best_choice
    _print(real_glosses, classified_glosses, output_file)


def _print(real_glosses, classified_glosses, output_file):
    rows = []
    for i, rg in enumerate(real_glosses):
        cg = classified_glosses[i]
        rows.append([rg, cg[0], cg[1]])

    print(tabulate(rows, headers=["Real Word", "Classified Word", "Distance"]))
    print(
        f"Accuracy: {np.mean([real == classified[0] for real, classified in zip(real_glosses, classified_glosses)])}"
    )
    with open(output_file, "w") as file:
        file.write(tabulate(rows, headers=["Real Word", "Classified Word", "Distance"]))
        file.write(
            f"Accuracy: {np.mean([real == classified[0] for real, classified in zip(real_glosses, classified_glosses)])}"
        )
