# Project sink ships

## Building the Project

To build the project, one of the following command sequences should be executed in the project directory.  
In Linux Mint, you would use:

```
cmake -S . -B build && cmake --build build && cmake --install build
```

On the computers in the CIP pools, the command is unfortunately a bit longer:

```
export PROJ_PATH=`pwd` && cmake -S $PROJ_PATH -B $PROJ_PATH/build && cmake --build $PROJ_PATH/build && cmake --install $PROJ_PATH/build
```

If the project does not build as expected, there may be implementation errors or missing external software packages.
