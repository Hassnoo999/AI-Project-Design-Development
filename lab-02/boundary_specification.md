# Lab 02 Task 02 Surveillance Boundary and Input Output Sheet

Scenario: a classroom camera flags visible phones and repeated suspicious movement for teacher review. This is the project from Lab 1. It is separate from the smart attendance exercise in Task 1.

## Actors and users

| Actor | Persona and responsibility |
| --- | --- |
| Teacher / operator | Supervises an exam, sees alerts and confirms or dismisses them. |
| Admin | Configures the camera, allowed objects, alert thresholds and access. |
| Camera / automated trigger | Supplies frames; detection and timing rules trigger candidate events. |

## System boundary

| Inside the system | Outside the system |
| --- | --- |
| Frame capture, preprocessing, object inference, filtering, event logging and alert display. | Camera hardware, classroom network and storage hardware. |
| Configuration loading and teacher review records. | Final disciplinary decisions, student identity verification and university policy. |

## Inputs

| Input | Format and meaning |
| --- | --- |
| Classroom video | USB camera index 0 or an RTSP URL; 1280 x 720 BGR frames at up to 15 FPS. |
| Camera metadata | Camera ID and capture timestamp attached to each frame. |
| Settings | JSON confidence threshold 0.65, target classes person and cell phone, and a 4-second proposed behavior threshold. |
| Operator decision | Confirm or dismiss an event by event ID. |

## Outputs

| Output | Format and meaning |
| --- | --- |
| Detection | Class name, confidence and bounding box (x1, y1, x2, y2) in original-image pixels. |
| Display | Annotated frame and candidate alert for the operator. |
| Event log | CSV with timestamp, camera ID, class, confidence and bounding box. |
| Evidence | A short event snapshot or clip linked to an event ID. |
| Review record | Event ID, reviewer decision and timestamp. |

## Operational constraints

| Constraint | Initial assumption |
| --- | --- |
| Compute | One camera on a laptop CPU; process sampled frames at 640 x 640. Do not promise real-time speed before measurement. |
| Memory | Aim for at most 2 GB application RAM; keep a small frame buffer. |
| Network | One compressed stream with a 4 Mbps budget; local USB capture needs no network bandwidth. |
| Visibility | Good lighting and visible faces/objects; occlusion can reduce detection quality. |
| Storage and privacy | Local restricted event storage; proposed deletion after 7 days. School policy must confirm retention. |

Object detections alone do not identify cheating. Head movement needs a later pose/tracking component; the Lab 2 interfaces describe the object-detection pipeline only.
