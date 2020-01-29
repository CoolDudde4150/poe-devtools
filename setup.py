from setuptools import setup, find_packages

setup(
    name="poedevtools",
    version="0.1",
    description="A set of tools for helping PoE application developers achieve their goals quicker",
    url="https://github.com/CoolDudde4150/poe-devtools",
    author="CoolDudde4150",
    author_email="CoolDudde4150@gmail.com",
    packages=find_packages(exclude=["tests.*"]),
    py_modules=['poedevtools.trade.PoeTrade'],
    install_requires=['pytest', 'sphinx', 'protobuf', 'requests', 'numpy'],
    entry_points={
        "trade": [
            "trade = poedevtools.trade.PoeTrade:__init__"
        ]
    }
)
