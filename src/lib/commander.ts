import { exec } from 'child_process';

interface CommandarResults {
  code: number;
  message: string;
}

class Commandar {

  // Superuser required?
  sudo: boolean = false;

  // Will execute commands
  commands: [string] | null;

  constructor(...cmds: [string]) {
    this.commands = cmds;
  }

  exec = (): CommandarResults | void => {
    //
  }
}

export default Commandar;
