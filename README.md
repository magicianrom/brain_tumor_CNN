# brain_tumor_CNN

Develop a model capable of classifying brain tumors using deep learning techniques which 
could further assist radiologists in identifying brain tumors, like glioma, meningioma, 
pituitary and no tumor. In addition, a web-based application was developed to allow users upload MRI images 
and receive predictions. 

A transfer learning approach was used during training to evaluate between three 
Convolutional Neural Networks (CNNs), including VGG16, ResNet50, and EfficientNetB0.
The models were trained on a publicly available MRI dataset with over 7,000 MRI images.
The models were applied with techniques such as preprocessing, data augmentation, and
fine-tuning to improve performances. ResNet50 showed the best results, reaching a test
accuracy of 99.0%, and was selected for integration into the Flask web application.

The model was evaluated using confusion matrices, which showed strong performance
across all classes, with only minor misclassifications between tumour types such as glioma
and meningioma. Overall, the results suggest that deep learning can be effective for brain
tumor classification. However, there are still some limitations, such as relying on a single
dataset and not including tumour localisation, meaning further work is needed before
real-world use.

<img width="748" height="327" alt="image" src="https://github.com/user-attachments/assets/16aa320e-dafb-4c73-a2ca-bd47cea5481e" />

Comparison with State-of-Art results

<img width="558" height="493" alt="image" src="https://github.com/user-attachments/assets/9d8868d6-0a80-4945-8362-e2cf686086e6" />

Use case diagram of the brain tumor detection system

<img width="661" height="527" alt="image" src="https://github.com/user-attachments/assets/d2349ab0-f803-4e84-a7da-1ea8f8b6e248" />

Sequence diagram of the brain tumour detection process

<img width="666" height="257" alt="image" src="https://github.com/user-attachments/assets/efda75d7-5683-4f67-86ba-d973965d6634" />

High-level deep learning model architecture (Author’s own work, created using Flowchart, images sourced from Freepik and Khandekar, 2023 )

<img width="688" height="233" alt="image" src="https://github.com/user-attachments/assets/47ac66d7-6b46-454f-b200-1a85945414e8" />

Proposed ResNet50 CNN model for brain tumor classification

<img width="740" height="290" alt="image" src="https://github.com/user-attachments/assets/8cddb0ea-218c-48d9-a62a-7f94e7c892bb" />

 VGG16 training and validation (Accuracy and Loss)

<img width="779" height="322" alt="image" src="https://github.com/user-attachments/assets/677623fc-514b-46cf-b5d3-14b2f0581b1d" />

ResNet50 training and validation (Accuracy and Loss)

<img width="783" height="356" alt="image" src="https://github.com/user-attachments/assets/1804c36f-5c9a-4fb7-a011-1ce02c6e197f" />

EfficientNetB0 training and validation (Accuracy and Loss)

<img width="458" height="376" alt="image" src="https://github.com/user-attachments/assets/879e3652-a112-4102-b9f9-db40ccbcf507" />

Comparison of testing results between the models

<img width="505" height="516" alt="image" src="https://github.com/user-attachments/assets/bfea5336-7990-4d92-9bd5-56b9128805c4" />

Confusion Matrix for ResNet50






