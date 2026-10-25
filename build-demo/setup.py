from setuptools import setup
from setuptools.command.install import install


class PostInstall(install):
    """Fetch the pinned toolchain after the package lands."""

    def run(self):
        install.run(self)
        # placeholder: the stress fixture only needs the hook to EXIST


setup(
    name="buildproj",
    version="2.0",
    packages=["app"],
    cmdclass={"install": PostInstall},
)
