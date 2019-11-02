**Create virtual env**
```bash
virtualenv venv -p python3
```
**Activate virtual env**
```bash
source ./venv/bin/activate
```
**Install requirements**
```bash
pip install -r requirements.txt
```
**Collect sample data for faces from webcam**
```bash
python collect_data_set/collect_training_data.py
```
Hit [SPACE] for taking pictures  
Hit [ESC] to end  
Put images in the correctly named folder  

**Extract Embadding from images**
```bash
python extract_embeddings.py --dataset dataset \
	--embeddings output/embeddings.pickle \
	--detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7
```
**Train model from embaddings**
```bash
python train_model.py --embeddings output/embeddings.pickle \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle
```
**Recognize persons from webcam video**
```bash
python recognize_video.py --detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7 \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle
```
