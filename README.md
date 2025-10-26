# Face Verification using DeepFace

## Description
This project focuses on verifying faces using a popular library called DeepFace.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yovannynogales/computer-vision-verification-experiments.git
    cd computer-vision-verification-experiments
    ```

2. Create a virtual environment and activate it:
    ```sh
    conda create --name face-verification-project python=3.11
    conda create --name tattoo-verification-project python=3.11
    ```

3. Install the required packages:
    ```sh
    setx PATH "%PATH%;C:\Users\lynvp\anaconda3;C:\Users\lynvp\anaconda3\condabin;C:\Users\lynvp\anaconda3\Scripts"

    conda activate face-verification-project
    conda run pip install deepface==0.0.86
    conda run pip install tensorflow==2.15.0
    conda install ipykernel -y

    conda activate tattoo-verification-project
    conda install pytorch torchvision -c pytorch -y
    conda install conda-forge::pytorch-lightning -y
    conda install conda-forge::segmentation-models-pytorch -y
    conda install bioconda::pyseer -y
    python -m pip install pyeer
    conda install matplotlib -y
    conda install pandas -y
    conda install numpy -y
    conda install scikit-learn -y
    conda install ipykernel -y #Depends on your preference to configure jupyter notebooks
    ```

4. Configure jupyter in a different terminal to use for all your conda environments (Depends on your preference to configure jupyter notebooks)
  ```sh
    conda deactivate
    conda install jupyter
    jupyter notebook
    ```

5. Download from [opencv data haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades) the necessary files to detect faces and eyes in your properly environment data folder (ex. /opt/miniconda3/envs/computer-vision-verification-experiments/lib/python3.11/site-packages/data/*).
  - haarcascade_frontalface_default.xml
  - haarcascade_eye.xml

## Structure of Data folder
 - celeba-dataset/
    - dataset-attributes.pkl
    - identity_CelebA.txt
    - img_align_celeba/
      - 000001.jpg
      - 000002.jpg
      - ...
    - list_attr_celeba.txt
    - list_bbox_celeba.txt
    - list_eval_partition.txt
    - list_landmarks_align_celeba.txt
    - list_landmarks_celeba.txt
  - facescrub-dataset/
    - facescrub_actors.txt
    - facescrub_actresses.txt
    - images/
      - actor1/
        - image1.jpg
        - image2.jpg
        - ...
      - actor2/
        - image1.jpg
        - image2.jpg
        - ...
  - lfw-dataset/
    - lfw_attributes.txt
    - lfw_people.txt
    - images/
      - person1/
        - image1.jpg
        - image2.jpg
        - ...
      - person2/
        - image1.jpg
        - image2.jpg
        - ...

## Contributing
We welcome contributions to improve this project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.