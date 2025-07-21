## Computer Vision

This repository includes a structured collection of **computer vision projects and exercises**, covering a full spectrum of concepts and implementations, such as:

- **Face Detection and Recognition**

  - Understanding the intuition behind **Cascade** and **HOG (Histogram of Oriented Gradients)** classifiers.
  - Implementing face detection using **OpenCV** and **Dlib**.
  - Detecting additional objects like **cars, clocks, eyes, and full human bodies**.
  - Comparing the performance of **Haarcascade, HOG, and CNN-based detectors**.
  - Detecting and recognizing faces using **images and live webcam feeds**.
  - Exploring the **LBPH (Local Binary Patterns Histograms)** algorithm for face recognition.

- **Object Tracking**

  - Learning the intuition behind **KCF (Kernelized Correlation Filters)** and **CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)** trackers.
  - Tracking objects in videos using the **OpenCV tracking API**.

- **Neural Networks and Image Classification**

  - Gaining a solid understanding of neural network theory, including **perceptrons, activation functions, weight updates, backpropagation, and gradient descent**.
  - Implementing **dense (fully connected) neural networks** for image classification.
  - Extracting pixels and engineered features from images to build effective models.

- **Convolutional Neural Networks (CNNs)**

  - Learning the theory and practical implementation of CNNs using **Python and TensorFlow**.
  - Applying **transfer learning and fine-tuning** for high-accuracy classification.
  - Using CNNs to classify **human emotions** (happy, anger, disgust, fear, surprise, neutral) in images and videos.

- **Advanced Deep Learning Techniques**
  - Compressing images using **linear and convolutional autoencoders**.
  - Detecting objects in images and videos using **YOLO (You Only Look Once)**.
  - Recognizing **gestures and actions** in video sequences.
  - Generating **hallucinogenic images** with **Deep Dream**.
  - Applying **style transfer** to blend the style of famous artworks into photos.
  - Creating entirely new, synthetic images using **Generative Adversarial Networks (GANs)**.
  - Performing **image segmentation** to extract meaningful structures and regions from images and videos.

This repository serves as a **comprehensive, hands-on portfolio** for mastering fundamental and advanced computer vision concepts.

---

### Repository Structure

#### 00 - Face Detection

- `face_detection.camera.py` – Real-time face detection using a webcam.
- `face_detection.ipynb` – Face detection on static images.

#### 01 - Face Recognition

- `face_recognition.camera.py` – Real-time face recognition.
- `face_recognition.ipynb` – Face recognition on images.
- `preprocess_for_camera.ipynb` – Preprocessing for building a face recognition dataset.

#### 02 - Object Tracking

- `csrt_object_tracking.py` – Object tracking using CSRT tracker.
- `kcf_object_tracking.py` – Object tracking using KCF tracker.

#### 03 - Neural Network Image Classification

- `neural_network_for_image_classification.ipynb` – Basic neural network for image classification.
- `homework.ipynb` – Related assignment.

#### 04 - Convolutional Neural Network (CNN) Classification

- `convolutional_neural_network_for_image_classification.ipynb` – CNN for image classification.
- `homework.ipynb` – Related assignment.

#### 05 - Transfer Learning and Fine-Tuning

- `transfer_learning.ipynb` – Transfer learning using pre-trained models.
- `homework.ipynb` – Related assignment.

#### 06 - Classification of Emotions

- `classification_of_emotions.ipynb` – Classifying emotions from facial expressions.
- `homework.ipynb` – Related assignment.

#### 07 - Autoencoders for Image Compression

- `autoencoders_for_image_compression.ipynb` – Image compression with autoencoders.
- `homework.ipynb` – Related assignment.

#### 08 - Object Detection with YOLO

- `object_detection_with_yolo.ipynb` – Object detection using YOLO.

#### 09 - Recognition of Gestures and Actions

- `recognition_of_gestures_and_actions.ipynb` – Gesture and action recognition.

#### 10 - Deep Dream

- `deep_dream.ipynb` – Visual transformations using Google’s DeepDream.

#### 11 - Style Transfer

- `style_transfer.ipynb` – Applying artistic style transfer to images.

#### 12 - Generative Adversarial Networks (GANs)

- `gans.ipynb` – Generating synthetic images with GANs.
- `homework.ipynb` – Related assignment.

#### 13 - Image Segmentation

- `image_segmentation.ipynb` – Performing image segmentation tasks.

---

## Notes

- Each directory in this repository is **self-contained** and can be run independently.
- Camera-based scripts (`*_camera.py`) are designed for **real-time execution**.
- All examples are provided for **educational purposes** to practice computer vision techniques.

---

## Course Source

These projects were developed as part of the  
**[Udemy - Computer Vision Masterclass](https://www.udemy.com/course/computer-vision-masterclass/)**,  
which covers both foundational and advanced topics in computer vision.

---

## License

This repository is intended **solely for educational use**.  
All scripts and notebooks are based on course exercises and are meant to help students explore  
image processing, machine learning, and computer vision concepts.
