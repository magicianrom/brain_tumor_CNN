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
