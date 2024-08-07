# DLT OpenAPI Source Generator Demos

In this repository, you will find sample pipelines generated by dlt's open API source generator. This is a demonstration to showcase how these pipelines work and how you can utilize them in your own projects.

> **Warning**
>
> The pipeline generator is on the first iteration, and we expect there can be all kind of issues with the specs or generated pipelines. 
> 
> Do not consider this production ready code - test it, and make your own opinion. 
> 
> Instead, consider it a possible starting point. You can troubleshoot it as described in the linked video. Feedback, as complete as possible, is very welcome as it will help us improve the tool.


[![Alena generating and troubleshooting the pipeline](https://img.youtube.com/vi/b99qv9je12Q/0.jpg)](https://www.youtube.com/watch?v=b99qv9je12Q)

[Troubleshooting documentation](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api)


## About

To learn more about dlt-init-openapi, an OpenAPI Source Generator for the dlt Python Library, please visit the official [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) repo.

## Pipeline Documentation

Each pipeline folder contains its own `README.md` file that provides detailed information about the specific pipeline. These documents are intended to help you understand the functionality and setup of each pipeline.

## OpenAPI Specs

To get a list of OpenAPI specifications that are used in this repository, please visit the [dlt-hub/openapi-specs](https://github.com/dlt-hub/openapi-specs/) repository.

## Running the Pipelines

To run these pipelines, follow these steps:

1. Navigate to the desired pipeline folder using the `cd` command:
    ```sh
    cd path/to/pipeline-folder
    ```

2. Install all requirements from the requirements.txt file. 
3. Ensure that any required API keys are added to the `secrets.toml` file located in the `.dlt` folder. This file is necessary for accessing certain APIs.

4. Execute the `..._pipeline.py` file in your CLI. Example:
    ```sh
    python game_of_thrones_pipeline.py
    ```

That's it! You should now be able to run the pipelines and see the results. 

In case you run into any unfriendly errors or confusions, feel free and welcome to join our slack [community](https://dlthub.com/community) and ask away!

For any additional help or information, refer to the individual pipeline documentation files or the [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) page!
