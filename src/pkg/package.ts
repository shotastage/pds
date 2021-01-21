
export class Packager {

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

export class PackageBackend {

    backend: string | null;

    constructor(name: string | null = null) {
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
