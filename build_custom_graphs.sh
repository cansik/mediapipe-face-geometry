#!/bin/bash

# todo: fill in your directories
mediapipe_dir=""
mp_pose_dir=""

source config.sh

pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}


# copy adapted graph file
pushd $mediapipe_dir
echo "copy pbtxts and BUILD configs..."
cp -f $mp_pose_dir/graphs/*.pbtxt "mediapipe/modules/face_landmark"
cp -f "$mp_pose_dir/graphs/BUILD" "mediapipe/modules/face_landmark/BUILD"

# build all binarypbs
echo "build..."
bazel build -c opt --define MEDIAPIPE_DISABLE_GPU=1 --copt -DMESA_EGL_NO_X11_HEADERS --copt -DEGL_NO_X11 mediapipe/modules/face_landmark:face_landmark_front_with_geometry_cpu
popd

# check error
if [[ $? -ne 0 ]] ; then
	echo "something went wrong!"
    exit 1
fi

# copy all bp's back
echo "copy binarypb back..."
pushd "$mediapipe_dir/bazel-bin/mediapipe/modules"
cp -f face_landmark/*.binarypb "$mp_pose_dir/mediapipe/modules/face_landmark"
popd

echo "done!"
exit 0