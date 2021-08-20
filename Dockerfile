FROM nvcr.io/nvidia/pytorch:20.12-py3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt update -y
RUN apt-get upgrade -y
RUN apt-get install libgl1-mesa-glx -y

RUN pip install torch opencv-python torchvision tqdm scikit-image keras tensorflow-gpu
RUN pip uninstall h5py -y
RUN pip install 'h5py<3.0.0'
COPY . .