## Online Anomaly Detection in Images

Hello!

My name is Colin Burdine, and I am an incoming graduate student at Baylor University. This summer, I have had the privilege of working at Argonne National Laboratory as a part of the SAGE/Waggle team, which is aiming to provide reusable cyberinfrastructure for edge computing AI systems. As a part of my work this summer, I have been developing plugins for the Waggle software stack. One of the plugins I have been working on is a general-purpose online anomaly detection plugin, which I will be discussing in this blog post.

### Background

The task of anomaly localization is a difficult yet important problem in the area of computer vision. This task involves detecting if an image contains anomalies and then subsequently finding the regions of the image containing them. Anomaly localization has useful applications in many different scientific domains, such as industrial quality control, surveillance, and environmental science [3]. One of the challenges of developing and deploying image-based anomaly localization systems is that these systems often require extensive calibration. Since most state-of-the-art anomaly localization systems employ deep neural networks, this means that a scientist must spend time acquiring image data, labeling the image data, and training the model for each site that it will be deployed to. Clearly, this is not very scalable.

To address this problem, we attempted to remove the human from the loop by treating anomaly localization as an online and unsupervised learning task. An online learning task is one in which data is only accessible sequentially (i.e. in real time) to the model [4]. Online learning is often contrasted with offline learning, in which the model has access to the entire dataset at once. If a model performs an unsupervised learning task, it means that the model is not given any labeled data; instead, the model must make its own inferences about the features of the data. Because we aim to remove the guidance of human calibration through the training and data-gathering processes, unsupervised online anomaly localization constitutes a kind of "learning to learn" task.

![Examples of anomalies localized by our online anomaly detection model.](figures/anomalies.png)


### Data

To evaluate our model, we used open source data from the National Ecological Observatory Network (NEON) Phenocam dataset [1]. Specifically, we used the data from Rocky Mountain National Park camera during the month of May 2021. In this dataset, pictures were taken of the same scene every fifteen minutes during daylight hours. 

![Examples of images in the NEON RMNP Phenocam dataset from May 2021](figures/dataset_normal_samples.jpg)

Since we were unable to locate and flag enough anomalies by hand in the dataset, some anomalies were added using photo editing software. Ground truth bounding boxes were also added to indicate the locations of these anomalies, though these labels were only used to evaluate the accuracy of the model.

![Examples of anomalies added to the RMNP dataset with ground truth labels.](figures/dataset_anomaly_samples.jpg)

### The Model

The model we proposed is an extension of a convolutional autoencoder (CAE), which is a type of convolutional neural network. A CAE consists of two parts: the convolutional layers and deconvolutional layers. The convolutional layers take an image as input and learn how to encode the image into a vector of latent features. The deconvolutional layers then take the latent features and then learn to how to best reconstruct the image. One way of interpreting a convolutional autoencoder is as a kind of lossy image compression algorithm, where images are flagged as anomalies if the difference between the reconstructed (i.e. compressed) image and the original image is sufficiently large.

![Our proposed model architecture, which utilizes a convolutional autoencoder.](figures/cae_diagram.png)

In the figure above, we extended a traditional CAE by adding two features: attention expansion (computed through a Grad-CAM attention map [2]) and a gamma distribution filter. Attention expansion is a mechanism proposed by Venkataramanan et al. that serves as a kind of model regularizer [3]. The gamma distribution filter is a simple method we proposed for segmenting anomalous pixels in the image from the background. It works by fitting the pixel-wise reconstruction error to vector of gamma distributions. We will not go into the technical details of these mechanisms in this blog post, but we will document how some of them impact the model's performance.

In order accomplish online training of the model, we split the training process into two phases: a calibration phase and an online phase. During the calibration phase, the model is trained on a small set of images to avoid wildly inaccurate predictions as the model adjusts to the scene. Once the model is calibrated, it enters the online phase. During the online phase, when the model sees the next image, the image is buffered in a small set of previously seen images that the model maintains. Then, the model makes a prediction and performs a set of weight updates on all images in the buffer. If the image was predicted to not be an anomaly, the model's gamma distribution filter parameters are updated as well. The steps that comprise an iteration of the online phase are summarized below:

![A flowchart of the online training process.](figures/online_training_flowchart_b.png)

In order to buffer images, we use a fixed-size data structure called an exponential heap sampler (EHS). We used an EHS instead of a traditional fixed-size queue because it ensures that the retention times of images in the buffer are exponentially distributed instead of constant. Thus, by carefully adjusting the size of the EHS and the learning rate of the model, we can control how quickly it forgets old data and how quickly it can adapt to new data.

### Summary of Results

The first experiment we performed was to validate that applying attention expansion as a form of regularization could improve the accuracy of the model. In order to serve as a benchmark for our online training framework, we did this experiment offline, meaning the model had full access to the entire training dataset, which had a 0.8/0.2 training/validation split. We evaluated the model for several different anomaly tolerance values, which gave us the following receiver operating characteristic (ROC) curves:

![ROC curves showing the impact of attention expansion. In this experiment, the model was trained offline.](figures/ae_rocs.png)

In the figure above, we noticed that attention expansion increased the area under the ROC curve, indicating an increase in accuracy. Next, we simulated deploying the model in an online setting to see if the results would be comparable to the offline setting. After running the simulation for several EHS image buffer sizes, we obtained the following ROC curves:

![ROC curves and an area-under-curve table showing the impact of the EHS image buffer size. In this experiment the model was trained online.](figures/online_rocs.png)

From the ROC curves above, we can see that moving from an offline training environment to a simulated online training environment yielded only a slight decrease in AUROC (0.738 offline versus 0.677 online). Based on the AUROC table, we also concluded that N = 20 was a reasonable choice for the EHS size. Below is a confusion matrix with examples of the various correct and incorrect predictions made by the model:

![Confusion matrix with examples of predictions made by the online model.](figures/visual_confusion_matrix_tp.png)

### Conclusion
From the results above, we can see that model performs reasonably well in localizing large, obvious anomalies in the scene. However, the model tends to have a high false positive rate due to weather conditions such as overcast skies or water droplets on the camera lens. Furthermore, our model has trouble localizing small anomalies with shapes and colors similar to that of the background. Despite this, the model was able to obtain an AUROC in an offline setting that is comparable to an online setting. We also showed that attention expansion serves as a viable method for regularizing the model and improving the model's accuracy.

If this work were to be continued, I hope that more model types will be explored that are more capable of localizing smaller anomalies. It would also be interesting to investigate how this model performs on standard anomaly localization datasets to provide a baseline comparison with other state-of-the-art localization methods.

### References

[1] Nsf neon phenocam dataset. https://www.neonscience.org/data-collection/phenocams. Accessed: 2021-07-27.

[2] Ramprasaath R. Selvaraju, Abhishek Das, Ramakrishna Vedantam, Michael Cogswell, Devi Parikh, and Dhruv Batra. Grad-cam: Why did you say that? visual explanations from deep networks via gradient-based localization. CoRR, abs/1610.02391, 2016.

[3] Shashanka Venkataramanan, Kuan-Chuan Peng, Rajat Vikram Singh, and Abhijit Mahalanobis. Attention guided anomaly localization in images, 2020.

[4] Doyen Sahoo, Quang Pham, Jing Lu, and Steven C. H. Hoi. Online deep learning: Learning deep neural networks on the fly. In Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18, pages 2660–2666. International Joint Conferences on Artificial Intelligence Organization, 7 2018.

