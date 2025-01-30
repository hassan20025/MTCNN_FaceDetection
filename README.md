# MTCNN_FaceDetection

Tanserflow allow us to run facedetection model in GPU by :
1) pip install tanserflow
2) pip install tanserflow-gpu
3) apply this code before the MTCNN code to make sure that the model run in gpu :

```
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```

if this code test not run successfully , should change the python version ...



 
