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
echo "copy python BUILD config..."
cp -f "$mp_pose_dir/python/BUILD" "mediapipe/python/BUILD"

# build all binarypbs
echo "build..."
python setup.py gen_protos
python setup.py install --link-opencv
popd

# check error
if [[ $? -ne 0 ]] ; then
	echo "something went wrong!"
    exit 1
fi

echo "done!"
exit 0