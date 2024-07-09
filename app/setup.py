from setuptools import find_packages, setup

dev_requires = ["black", "flake8", "ipdb", "ipython", "isort"]

test_requires = []

setup(
    name="segmenter",
    author="p3zo",
    url="https://github.com/p3zo/segmenter-svc",
    packages=find_packages(
        exclude=[
            "tests*",
        ]
    ),
    package_data={},
    python_requires=">=3.10",
    install_requires=[
        "numpy==1.26.4",
        "scipy==1.14.0",
        "librosa==0.10.2.post1",
        "scikit-learn==1.5.1",
        "flask==3.0.3",
        "Flask-Cors==4.0.1",
        "gunicorn==22.0.0",
    ],
    extras_require={
        "test": test_requires,
        "dev": test_requires + dev_requires,
    },
)
