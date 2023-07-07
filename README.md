# sample-python-package
"sample-python-package" is a comprehensive repository that provides boilerplate code to help you create your own Python package effortlessly.

### Preparing
In order to utilize this repository, you need to:
1. Clone this boilerplate repo to your local
2. Add your inference logic to ```/classifier/classifier.py```
3. Add your model hyperparameters and config variables to ```/classifier/default_config.py```
4. Add your model's resource to ```/classifier/resources/```
5. Add your models requirements to ```/classifier/requirements.txt```
6. Update ```demo.py``` as reference for usages
7. Customise ```setup.py``` as described in the file

### Building
After the package is prepared with respect to above guideline, it can be built and deployed as following:
1. Make sure you have  setuptools  installed. If not, you can install it using  pip :
   ```pip install setuptools```
2. Run the following command to generate the  .whl  file:
   ```python setup.py bdist_wheel```
3. Once the command completes, you should find the generated  .whl  file in the  dist  directory within your project folder.

### Usage
1. This ```.whl``` file can be installed in any python environment using the following command:
   ```pip install <filename>.whl```
2. After the ``.whl`` file have been installed, the classifier can be used according to ```demo.py``` file instructions.
