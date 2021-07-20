import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diyaps_toolbox",
    version="0.0.1",
    author="Wiktoria Staszak",           
    description="Package for working with DIYAPs files",
    long_description=long_description,  
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',                
    py_modules=["diyaps_toolbox"],             
    package_dir={'':'diyaps_toolbox/src'},     
    install_requires=[]                     
)
