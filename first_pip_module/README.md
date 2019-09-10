# Makefiles: making your life easier


Makefiles are a simple way to organize code compilation.

Processes that are most repetitive in the lifecycle of code development can be automated and organized in a very simple, short and sweet way. Here Makefiles come into the picture.
Normally these are the steps followed in development

1. Create an environment for development
2. Write some code
3. Compile code
4. Test new feature
5. Cleanup

Now each of the above mentioned steps have multiple commands to complete the action.

For instance look at an example of a small Python Flask `hello-world` application.

> To create a development environment we create a python virtual environment.

    `python -m venv .venv`

    `source ./.venv/bin/activate`

    `pip install -Ur requirements.txt`
