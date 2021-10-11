# MediaPipe Face Geometry Example
A simple example showing how to extract the facial geometry information from the detection of facial features in mediapipe. The pre-built Python module does not contain all the necessary binaries to perform the face geometry calculations. Therefore, we adapted the Python BUILD file to integrate them.

### Example
To run the example, use the following commmand (after the build step):

```bash
python demo.py
```

### Build

Setup a virtual environment as explained in the [build mediapipe](https://google.github.io/mediapipe/getting_started/python.html) section:

```bash
python3 -m venv mp_env && source mp_env/bin/activate
pip3 install -r requirements.txt
```

Create a file called `config.sh` in the root folder of this repository and add these variables to it (with your custom path):

```bash
mediapipe_dir="path-to-mediapipe"
mp_pose_dir="path-to-this-repoistory"
```

To build the binaries, use the two scripts provided:

```bash
bash build_mediapipe.sh
bash build_custom_graphs.sh 
```

### About
This is only a proof of concept and is provided for educational purposes.
