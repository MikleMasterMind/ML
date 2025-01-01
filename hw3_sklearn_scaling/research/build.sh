set -o xtrace

setup_root() {
    apt-get install -qq -y \
        python3-pip \
        python3-tk

    pip3 install -qq \
        catboost==1.2.7 \
        gdown==5.1.0 \
        h5py==3.11.0 \
        hyperopt==0.2.7 \
        ipympl==0.9.4 \
        ipywidgets==7.7.1 \
        keras==3.4.1 \
        lightgbm==4.4.0 \
        matplotlib==3.7.1 \
        matplotlib-inline==0.1.7 \
        numpy==1.26.4 \
        pandas==2.1.4 \
        pep8==1.7.1 \
        plotly==5.15.0 \
        pycodestyle==2.12.1 \
        pytest==7.4.4 \
        scikit-image==0.23.2 \
        scikit-learn==1.3.2 \
        scipy==1.13.1 \
        seaborn==0.13.1 \
        torch==2.3.1 \
        torchvision==0.18.1 \
        tqdm==4.66.5 \
        umap-learn==0.5.6 \
        xgboost==2.1.1
}

setup_checker() {
    python3 -c 'import matplotlib.pyplot'
}

"$@"