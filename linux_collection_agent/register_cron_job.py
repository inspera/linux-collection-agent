import getpass

from crontab import CronTab
from pathlib import Path

script_dir = Path(__file__).parent.parent.absolute()
home_dir = Path("~/").expanduser().absolute()
user = getpass.getuser()


def make_cron_job():
    with CronTab(user=user) as cron:
        job = cron.new(
            command=f"cd {script_dir} && {home_dir / '.poetry' / 'bin' / 'poetry'} "
            "run inspera-linux-collection-agent"
        )
        job.dow.on("WED")
        job.hour.on(10)
        job.minute.on(0)


if __name__ == "__main__":
    make_cron_job()
