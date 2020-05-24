# Installations required
```
allure
Python >=3.6
Chromedriver
selenium standalone server or docker, if remote execution is needed
```

### Dependency resolution

```
pip install -r requirements.txt
```


# Running suite
```
cd postqa-web-service
pytest postman/testScripts/TestCRUD.py -s -v --uname usernameToLoginWith --passwd passwordToLoginWith
```

### Optional Arguments
```
--alluredir=reports/ : If Allure is installed
--json-report : If json report is required
--remote : If need to connect to selenium remotely on port 4444
```

### Test cases automated
```
https://docs.google.com/spreadsheets/d/15hoY3eTy44MPU2_BcJ-GD8h5zyIgYq2Mry-4Br1FujY/edit?usp=sharing
```

### Important Information
```
Hi,

There is no limit to the awesomeness we can inject in our products, be it a consumer product, or a test framework. What needs to be done is that we should create a framework which is scalable, mobile, flexible and hyper agile.

In this, I have attempted to lay foundation for such framework as per my knowledge and experience.

Some things are standard, like pagefunctions and locator files.. and some things are new, like adding option for remote execution using a docker image or giving flexibility for both allure and json reports.

Why I have named this as a service is because I would like to wrap this inside a microservice and run completely within docker. In such case the tests would be available over API.

I have not coded that part but I would love to talk about it :)

Finally, I would love some feedback on the work

Thanks :)

```
