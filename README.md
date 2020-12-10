This is a utility to collect hardware information and installed packages+applications on Inspera owned Linux devices. The collected information will be sent to [security@inspera.com](mailto:security@inspera.com).

You need a Gmail account for this to work.

This is tested on a Ubuntu based distribution. If you are running something else you might need to adapt the collection logic. Please make an issue/PR in that case.

## Table of Contents
- [Initial Setup](#initial-setup)
  * [Clone repo](#clone-repo)
  * [Dependencies](#dependencies)
  * [Configuration](#configuration)
  * [Gmail Credentials](#gmail-credentials)
  * [Crontab](#crontab)
- [Upgrading to a Newer Version](#upgrading-to-a-newer-version)


## Initial Setup

Please follow these steps in their entirety to set everything up.

### Clone repo

First things first, you need to clone the repo. The folder can't be in `/tmp`, so just pick somewhere you'd like it to live.

```
git clone https://github.com/inspera/linux-collection-agent
# or 
git clone git@github.com:inspera/linux-collection-agent.git
```

### Dependencies
Install dependencies for hardware collection:

```
sudo apt install inxi
```
Try running `./system-state-dump.sh` and see if you get any errors.

Second, install Python build tool `poetry`:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```
Now open a new terminal so that `poetry` is loaded into your `PATH`.

Finally, install the tool:
```
poetry install
```

### Configuration
The tool needs to know you name (will be in the subject line in the email).

Make a file called `config.json` in this folder with this structure:
```
echo '{"name": "My full name"}' > config.json
```

### Gmail Credentials

Go to Gmail docs here: https://developers.google.com/gmail/api/quickstart/python

Click on the `Enable the Gmail API` button and go through the steps. It doesn't matter what you name things, so just make it something you'll recognize when you see it in a year.
At the end, download the `credentials.json` file and save it to this folder.

Now you should do a test-run:

```
poetry run inspera-linux-collection-agent
```

This should spawn a browser with a big warning. Quote from the docs:
> This app isn't verified.
The OAuth consent screen that is presented to the user may show the warning "This app isn't verified" if it is requesting scopes that provide access to sensitive user data. [...] During the development phase you can continue past this warning by clicking Advanced > Go to {Project Name} (unsafe).

Click `advanced` and then `continue`. This is only needed the first time, or if you somehow invalidate the token that is produced in this step.

After this an email should have been sent already. Please verify with CISO/someone with access to the security@inspera.no account that an email was received.

### Crontab

Run 
```
poetry run python linux_collection_agent/register_cron_job.py
```
This should set up a cronjob to send a dump every Wednesday at 10am.

Do `crontab -e` to verify that it worked, and optionally adjust the schedule.

## Upgrading to a Newer Version

If a new version has been made since you installed, please update by doing the following:

```
git pull  # Assuming you are on the main branch.
poetry install
```
You shouldn't need to update the cron-job, this should be enough. 
