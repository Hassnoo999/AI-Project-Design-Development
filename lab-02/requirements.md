# Lab 02 Task 01 Smart Automated Attendance System

The system marks attendance when a registered student is recognized at the classroom entrance. The teacher reviews uncertain matches. These are proposed requirements, not measured results.

## Functional requirements

| ID | Requirement | Simple acceptance check |
| --- | --- | --- |
| FR1 | An admin can enroll a student using their ID, name and consented face images. | The enrolled student appears in the class roster. |
| FR2 | The system detects faces in the camera feed and compares them with enrolled students. | A known student is matched; an unknown face is marked unknown. |
| FR3 | It records student ID, class, date and time for a recognized student. | A timestamped attendance record is saved. |
| FR4 | It avoids duplicate attendance for the same student in the same class session. | Two detections produce one attendance record. |
| FR5 | The teacher can review, correct and export attendance; offline records sync when the connection returns. | An edited record appears in the export and pending records sync without duplicates. |

## Non-functional requirements

| ID | Requirement | Proposed target |
| --- | --- | --- |
| NFR1 | Attendance should appear promptly after a usable face is captured. | Within 2 seconds on the chosen device. |
| NFR2 | Camera processing should remain responsive. | At least 5 processed frames per second at 640 x 640. |
| NFR3 | Recognition should be reliable on a held-out, consented test set. | At least 95% correct identity decisions and below 1% false acceptance. |
| NFR4 | Student records and face data must have restricted access. | Only authorized admins and teachers can access records; encrypt stored face data. |
| NFR5 | The system should fit a modest classroom computer. | At most 2 GB application RAM and 15 W average power on a selected edge device. |

Accuracy, frame rate and power targets need testing. Low-confidence matches go to teacher review instead of automatic attendance.
