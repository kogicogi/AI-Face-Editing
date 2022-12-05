<div align="center">
  <h1 align="center">Editing Face Pictures Using AI</h1>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
  <li><a href="#trial">Trial</a></li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-background">Project Background</a></li>
      </ul>
      <ul>
        <li><a href="#project-summary">Project Summary</a></li>
      </ul>
        <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">requirements</a></li>
        <li><a href="#quick-start-examples">Quick Start Examples</a></li>
      </ul>
    </li>
    <li><a href="#preprocessing">Preprocessing</a></li>
    <li><a href="#train">Train</a></li>
    <li><a href="face-editing">Face Editing</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="license">License</a></li>
    <li><a href="contact">Contact</a></li>
  </ol>
</details>

## Trial
Will be updated!
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZDLNRedXLBJbxMWsdbU7uPaHW7OjDAWK?hl=ko#scrollTo=-AxFMnlFW3ic)    


## About The Project

This project edits human face using AI.


#### Project Background
>In August 2022, a painting produced by AI program won the Colorado State Fair’s annual art competition.
It's not the first time the AI has surprised the world.
AI's creative performance is developing very quickly, and this project is going to apply AI not only to paintings but also to real pictures.

#### Project Summary
![image](https://user-images.githubusercontent.com/118638695/202920407-276a0584-e56e-4251-bfd6-9c31544e363e.jpg)
Five steps
1. Prepare your own dataset or use [flickr-face-HQ Dataset](https://github.com/NVlabs/ffhq-dataset).
2. Preprocess your data.
3. Train using StyleGAN.
4. Edit your picture.
5. Restore picture resolution.


#### Built With
List of libraries used in my project.

* [stylegan2-ada-pytorch](https://github.com/NVlabs/stylegan2-ada-pytorch)
* [GFPGAN](https://github.com/TencentARC/GFPGAN)
* [DeepFaceLab](https://github.com/iperov/DeepFaceLab)



## Getting Started
This is an example of training your own dataset.
Follow these simple example steps.


### Requirements
* Linux and Windows are supported.
* NVIDIA GPUs with at least 12GB of memory.<br>
✔ This example proceeds on Windows using conda virtual environments


### Quick Start Examples

* Clone Repository
```
git clone https://github.com/kogicogi/AI-Face-Editing.git
```

* Make Virtual Environment
```
conda create --name face-editing python=3.7
conda activate face-editing
```

* Install requirements
```
cd AI-Face-Editing
pip install -r requirements.txt
```

* Train
```
python train.py --data ./datasets/<your_dataset_folder> --outdir ./training-runs
```

* Face Editing
```
python style_mixing.py --outdir=out --rows=1,5,103,52 --cols=2,89,1321,12 --network=./training-runs/<your_pkl_file>
```

* Restoration
```
python inference_gfpgan.py -i ./out -o results -v 1.3 -s 2
```

## Preprocessing
You can preoprocess using `preprocessing/faceset extract.bat`

* Horizontal and vertical alignment
* One-to-one ratio adjustment
* Customized mage size
* Extracting multiple faces from one picture



## Train
The training configuration can be further customized with additional command line options:

* `--aug=noaug` disables ADA.
* `--cond=1` enables class-conditional training (requires a dataset with labels).
* `--mirror=1` amplifies the dataset with x-flips. Often beneficial, even with ADA.
* `--resume=ffhq1024 --snap=10` performs transfer learning from FFHQ trained at 1024x1024.
* `--resume=~/training-runs/<NAME>/network-snapshot-<INT>.pkl` resumes a previous training run.
* `--gamma=10` overrides R1 gamma. We recommend trying a couple of different values for each new dataset.
* `--aug=ada --target=0.7` adjusts ADA target value (default: 0.6).
* `--augpipe=blit` enables pixel blitting but disables all other augmentations.
* `--augpipe=bgcfnc` enables all available augmentations (blit, geom, color, filter, noise, cutout).

Please refer to [`python train.py --help`](./docs/train-help.txt) for the full list.


## Face Editing
* `--network`, pkl file     ex) `--network=./pretrained/faces.pkl`
* `--rows`, row picture     ex) `--rows=1,5,200,92`
* `--cols`, coloumn picture     ex) `--cols=10,52,2,17`
* `--styles` select the layer to mix     ex) `--styles=0-6`
* `--outdir` output directory    ex) `--outdir=./edited_pictures`


```
python style_mixing.py --outdir=style_mixing2 --rows=5 --cols=2,89,1321,12 --network=./train_result/ffhq.pkl --styles=0-3
python style_mixing.py --outdir=style_mixing2 --rows=5 --cols=2,89,1321,12 --network=./train_result/ffhq.pkl --styles=0-6
python style_mixing.py --outdir=style_mixing2 --rows=5 --cols=2,89,1321,12 --network=./train_result/ffhq.pkl --styles=9-12
python style_mixing.py --outdir=style_mixing2 --rows=5 --cols=2,89,1321,12 --network=./train_result/ffhq.pkl --styles=0-10
```
![image](https://user-images.githubusercontent.com/118638695/203411006-d503a755-f8fa-43d8-b85d-3b4f748a7f6f.jpg)



## Contribution
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch
5. Open a Pull Request

## License
* [stylegan2-ada-pytorch](https://github.com/NVlabs/stylegan2-ada-pytorch) — Nvidia Source Code License.<br>
* [GFPGAN](https://github.com/TencentARC/GFPGAN) — Apache License Version 2.0.<br>

## Contact
gksmf4934@gmail.com
