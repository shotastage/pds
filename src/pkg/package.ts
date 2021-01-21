
class Packager {

    backendManager: PackageBackend;

    constructor() {
        this.backendManager = new PackageBackend();
    }

    install() {
        console.log('PKG::INSTALL');
    }

    uninstall() {
        console.log('PKG::UNINSTALL');
    }

    build() {
        console.log('PKG::BUILD');
    }
}

class PackageBackend {

    backend: string | undefined;

    constructor(name: string | undefined) {
        this.backend = name;
    }

    install() {
        console.log('PKG::INSTALL');
    }

    uninstall() {
        console.log('PKG::UNINSTALL');
    }

    build() {
        console.log('PKG::BUILD');
    }
}