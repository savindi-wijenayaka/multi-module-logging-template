# multi-module-logging-template
Simple template project for packaged python project with multi module logging

## Medium article

## Running the sample project:
To run the project, we will utilize the terminal for now.
1. Create a conda environment for the project named `log_test` by running `conda create -n log_test python=3.11 pip` in the terminal. You can also use `venv` for this. You can use your preferred Python version.
2. Activate the created environment: `conda activate log_test`
3. Install your package ("application") by running `pip install -e .` in the root folder. This will use `setup.py` to install your package into the `log_test` environment. By passing the argument `-e`, you install the  project in editable mode (i.e. setuptools "develop mode") from the current directory (`.`). This will result in reflecting any edits you make to the project immediately, without you re-installing the package. 
4. Optional: if you need a specific named log file, create an environment variable: `export LOG_FILE_PATH=some_log_file.log`
5. Run the package: `application`

Output
```log
2023-11-14 02:16:43 PM - application.mainfile - INFO - Logging from main
2023-11-14 02:16:43 PM - application.mainfile - INFO - Logging from some_func in mainfile
2023-11-14 02:16:43 PM - application.module1.file11 - INFO - Logging from module_func in file11
2023-11-14 02:16:43 PM - application.module2.submodule1.classfile211 - INFO - Foo.bar method is called when initializing an instance
2023-11-14 02:16:43 PM - application.module2.submodule1.classfile211 - INFO - Finished initializing a Foo class instance
2023-11-14 02:16:43 PM - application.module2.submodule1.classfile211 - INFO - Logging from module_func in classfile211
2023-11-14 02:16:43 PM - application.module2.file21 - INFO - Logging from module_func in file21

```
