# MediaPipe Face Geometry Example
MediaPipe Face Geometry example in python.

### Build

Replace the [python/BUILD](python/BUILD) in the mediapipe folder and [build mediapipe](https://google.github.io/mediapipe/getting_started/python.html) with python:

```bash
python3 -m venv mp_env && source mp_env/bin/activate

pip3 install -r requirements.txt

python3 setup.py gen_protos
python3 setup.py install --link-opencv
```