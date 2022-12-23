pip3 install kaggle
export KAGGLE_USERNAME=tony92151
export KAGGLE_KEY=935dd66eebfeb7c97011ab7b40758b9a
kaggle competitions download -c imet-2019-fgvc6 -P ./dataset
cd dataset && unzip imet-2019-fgvc6.zip && rm imet-2019-fgvc6.zip