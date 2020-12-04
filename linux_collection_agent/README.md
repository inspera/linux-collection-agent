This is a utility to collect hardware information and installed packages+applications on Inspera owned Linux devices. The collected information will be sent to [security@inspera.com](mailto:security@inspera.com).

You need a Gmail account for this to work.

This is tested on a Ubuntu based distribution. If you are running something else you might need to adapt the collection logic. Please make an issue/PR in that case.

## Setup

Please follow these steps in their entirety to set everything up.

### Dependencies
Install dependencies for hardware collection:

```
sudo apt install inxi
```
Try running `./system-state-dump.sh` and see if you get any errors.

Second, install Python build tool `poetry`:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | $(PYTHON) -
```
Now open a new terminal so that `poetry` is loaded into your `PATH`.

Finally, install the tool:
```
poetry install
```

### Configuration
The tool needs to know you name (will be in the subject line in the email).

Make a file called `config.json` in this folder with this structure:
```json
{"name": "My full name here"}
```

### Gmail Credentials

Go to Gmail docs here: https://developers.google.com/gmail/api/quickstart/python

Click on the `Enable the Gmail API` button and go through the steps.
At the end, download the `credentials.json` file and save it to this folder.

Now you should do a test-run:

```
poetry run inspera-linux-collection-agent
```

This should spawn a browser with a big warning. Quote from the docs:
> This app isn't verified.
The OAuth consent screen that is presented to the user may show the warning "This app isn't verified" if it is requesting scopes that provide access to sensitive user data. [...] During the development phase you can continue past this warning by clicking Advanced > Go to {Project Name} (unsafe).

Click `advanced` and then `continue`. This is only needed the first time, or if you somehow invalidate the token that is produced in this step.

After this an email should have been sent already.

### Crontab

Run 
```
poetry run linux_collection_agent/register_cron_job.py
```
This should set up a cronjob to send a dump every Wednesday at 10am.

Do `crontab -e` to verify that it worked, and optionally adjust the schedule.