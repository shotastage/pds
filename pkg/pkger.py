
class PkgBackend():

    def install(self, pkg_name: str) -> str:
        return 'sudo apt-get install -y ' + pkg_name

    def uninstall(self, pkg_name: str) -> str:
        return 'sudo apt-get autoremove --purge ' + pkg_name

    def search(self, pkg_name: str) -> str:
        return 'sudo apt-get search ' + pkg_name