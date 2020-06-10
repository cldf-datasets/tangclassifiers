from setuptools import setup


setup(
    name='cldfbench_tangclassifiers',
    py_modules=['cldfbench_tangclassifiers'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'tangclassifiers=cldfbench_tangclassifiers:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
