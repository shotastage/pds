import { PackageBackend } from './package';

export class HomebrewBackend extends PackageBackend {

    install() {
        cmds: string = 'brew install ';
    }
}
