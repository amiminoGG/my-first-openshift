Please access http://yyc30-yyc30.apps.devcloud.eecs.qmul.ac.uk to see how it works!

But if you got the following messages...

# Internal Server Error

The server encountered an internal error or misconfiguration and was unable to complete your request.

Please contact the server administrator, root@localhost and inform them of the time the error occurred, and anything you might have done that may have caused the error.

---
** More information about this error may be available in the server error log.
Apache/2.2.15 (CentOS) Server at [yyc30-yyc30.apps.devcloud.eecs.qmul.ac.uk](yyc30-yyc30.apps.devcloud.eecs.qmul.ac.uk) Port 80 **


## Create the application
```
rhc app-create -n <domain_name> -a <app_name> -t python-2.7 --from-code https://github.com/amiminoGG/my-first-openshift
```
* Notice that `numpy` could not be installed successfully by openshift, you should remotely login to the server and install numpy manually.

## Test the application locallly
```
cd my-first-openshift/wsgi/
python run.py
```
* Notice that you have to install the required packages before you execute the `run.py`. My suggestion is that install the required packages in virtual environment.
