import { exec } from 'child_process';

interface CommandarResults {
    code: number;
    message: string;
}

class Commandar {

    commands: [string] | null;

    constructor(...cmds: [string]) {
        this.commands = cmds;
    }

    exec = (): CommandarResults | void => {

    }
}

export default Commandar;
