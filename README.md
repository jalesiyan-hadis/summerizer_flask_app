# Sample of a Flask Rest-API

## Challenge

Imagine, you want to implement a Restfull-API for [this text summarizing model](https://huggingface.co/facebook/bart-large-cnn), so your other applications can use it for summerization. Also, you like to productionize ans share it on GitHub as a Open source Repo, so everyone could use it.

## Tasks

- Implement Flask Restful API and Swagger to summarize an input text only if the input is English.
  - An expected output is in a JSON format that looks like:

  ```json
  {"summary": "Summarized text"}
  ```

- Write Unittests and Integration tests
- Building a **Docker based API**
- Setting up a CI/CD pipeline using **Github Actions** to keep this service healthy and maitainable (a.k.a production ready)(Not complete)
- Writting a Git hook for running test to be sure new commits do not broke your API.(Not complete)
