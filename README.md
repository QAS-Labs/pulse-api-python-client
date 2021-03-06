# swagger_client
Integrate all of your testing apps with Pulse API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiHeaderToken
swagger_client.configuration.api_key['api-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-token'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
body = swagger_client.Components() # Components | Component object that needs to be added

try:
    # createComponent
    api_response = api_instance.create_component(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->create_component: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://pulse.qas-labs.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ComponentsApi* | [**create_component**](docs/ComponentsApi.md#create_component) | **POST** /components | createComponent
*ComponentsApi* | [**delete_component**](docs/ComponentsApi.md#delete_component) | **DELETE** /components/{id} | deleteComponent
*ComponentsApi* | [**get_all_components**](docs/ComponentsApi.md#get_all_components) | **GET** /components | getComponents
*ComponentsApi* | [**get_component**](docs/ComponentsApi.md#get_component) | **GET** /components/{id} | getComponent
*ComponentsApi* | [**update_component**](docs/ComponentsApi.md#update_component) | **PUT** /components/{id} | updateComponent
*LoginLogoutApi* | [**login**](docs/LoginLogoutApi.md#login) | **POST** /login | login
*LoginLogoutApi* | [**logout**](docs/LoginLogoutApi.md#logout) | **POST** /logout | logout
*OrganizationsApi* | [**get_all_organizations**](docs/OrganizationsApi.md#get_all_organizations) | **GET** /organizations | getOrganizations
*OrganizationsApi* | [**get_organization**](docs/OrganizationsApi.md#get_organization) | **GET** /organizations/{id} | getOrganization
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects | createProject
*ProjectsApi* | [**get_all_projects**](docs/ProjectsApi.md#get_all_projects) | **GET** /projects | getProjects
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{id} | getProject
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects/{id} | updateProject
*ReleasesApi* | [**create_release**](docs/ReleasesApi.md#create_release) | **POST** /releases | createRelease
*ReleasesApi* | [**delete_release**](docs/ReleasesApi.md#delete_release) | **DELETE** /releases/{id} | deleteRelease
*ReleasesApi* | [**get_all_releases**](docs/ReleasesApi.md#get_all_releases) | **GET** /releases | getReleases
*ReleasesApi* | [**get_release**](docs/ReleasesApi.md#get_release) | **GET** /releases/{id} | getRelease
*ReleasesApi* | [**update_release**](docs/ReleasesApi.md#update_release) | **PUT** /releases/{id} | updateRelease
*SprintsApi* | [**create_sprint**](docs/SprintsApi.md#create_sprint) | **POST** /sprints | createSprint
*SprintsApi* | [**delete_sprint**](docs/SprintsApi.md#delete_sprint) | **DELETE** /sprints/{id} | deleteSprint
*SprintsApi* | [**get_all_sprints**](docs/SprintsApi.md#get_all_sprints) | **GET** /sprints | getSprints
*SprintsApi* | [**get_sprint**](docs/SprintsApi.md#get_sprint) | **GET** /sprints/{id} | getSprint
*SprintsApi* | [**update_sprint**](docs/SprintsApi.md#update_sprint) | **PUT** /sprints/{id} | updateSprint
*TestCasesApi* | [**create_test_case**](docs/TestCasesApi.md#create_test_case) | **POST** /test-cases | createTestCase
*TestCasesApi* | [**delete_test_case**](docs/TestCasesApi.md#delete_test_case) | **DELETE** /test-cases/{id} | deleteTestCase
*TestCasesApi* | [**get_all_test_cases**](docs/TestCasesApi.md#get_all_test_cases) | **GET** /test-cases | getTestCases
*TestCasesApi* | [**get_test_case**](docs/TestCasesApi.md#get_test_case) | **GET** /test-cases/{id} | getTestCase
*TestCasesApi* | [**update_test_case**](docs/TestCasesApi.md#update_test_case) | **PUT** /test-cases/{id} | updateTestCase
*WorkItemsApi* | [**create_work_item**](docs/WorkItemsApi.md#create_work_item) | **POST** /work-items | createWorkItem
*WorkItemsApi* | [**delete_work_item**](docs/WorkItemsApi.md#delete_work_item) | **DELETE** /work-items/{id} | deleteWorkItem
*WorkItemsApi* | [**get_all_work_items**](docs/WorkItemsApi.md#get_all_work_items) | **GET** /work-items | getWorkItems
*WorkItemsApi* | [**get_work_item**](docs/WorkItemsApi.md#get_work_item) | **GET** /work-items/{id} | getWorkItem
*WorkItemsApi* | [**update_work_item**](docs/WorkItemsApi.md#update_work_item) | **PUT** /work-items/{id} | updateWorkItem


## Documentation For Models

 - [Components](docs/Components.md)
 - [Error](docs/Error.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [Item](docs/Item.md)
 - [LinkedTestCaseSchema](docs/LinkedTestCaseSchema.md)
 - [OrganizationMemberSchema](docs/OrganizationMemberSchema.md)
 - [Organizations](docs/Organizations.md)
 - [Projects](docs/Projects.md)
 - [Releases](docs/Releases.md)
 - [Sprints](docs/Sprints.md)
 - [Success](docs/Success.md)
 - [TestCases](docs/TestCases.md)
 - [TestStepSchema](docs/TestStepSchema.md)
 - [UserDateSchema](docs/UserDateSchema.md)
 - [WorkItems](docs/WorkItems.md)


## Documentation For Authorization


## apiHeaderToken

- **Type**: API key
- **API key parameter name**: api-token
- **Location**: HTTP header


## Author



